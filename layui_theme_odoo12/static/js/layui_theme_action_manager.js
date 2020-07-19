/**
 * Created by artorias on 2018/12/13.
 */
odoo.define('layui_theme_sidebar_ext', function (require) {
    "use strict";

    var Widget = require('web.Widget');
    var core = require('web.core');
    var QWeb = core.qweb;

    var SidebarExt = Widget.extend({
        events: {
            'click': '_click_tree_buttons'
        },
        init: function (parent, options) {
            this._super.apply(this, arguments);
            this.tree_buttons = options.tree_buttons;
        },
        start: function () {
            this._super.apply(this, arguments);
            this.render_tree_buttons()
        },
        render_tree_buttons: function () {
            this._replaceElement($(QWeb.render('layui_tree_button',
                {tree_buttons: this.tree_buttons})));
        },
        /**
         * 重置tree_buttons
         * @param controlPanel
         */
        reset_tree_buttons: function (controlPanel) {
            if (controlPanel.sidebar_ext) {
                controlPanel.sidebar_ext.destroy()
            }
            this.appendTo(controlPanel.$('div.o_list_buttons[role=toolbar]'));
            controlPanel.sidebar_ext = this;
        },
        /**
         * 绑定click事件, 执行对应action
         * @param event
         * @private
         */
        _click_tree_buttons: function (event) {
            this.do_action($(event.target).attr('action'))
        }
    });

    return SidebarExt

});


odoo.define('layui_theme_action_manager', function (require) {
    "use strict";

    var ActionManager = require('web.ActionManager');
    var dom = require('web.dom');
    var SidebarExt = require('layui_theme_sidebar_ext');

    ActionManager.include({
        _executeAction: function (action, options) {
            var self = this;
            this.actions[action.jsID] = action;

            if (action.target === 'new') {
                return this._executeActionInDialog(action, options);
            }
            return this.clearUncommittedChanges()
                .then(function () {
                    var controller = self.controllers[action.controllerID];
                    // 添加bind_tree_buttons
                    controller.bind_tree_buttons = action.bind_tree_buttons ? JSON.parse(action.bind_tree_buttons.replace(/'/g, '"')) : false;
                    var widget = controller.widget;
                    // AAB: this will be moved to the Controller
                    if (widget.need_control_panel) {
                        // set the ControlPanel bus on the controller to allow it to
                        // communicate its status
                        widget.set_cp_bus(self.controlPanel.get_bus());
                    }
                    return self.dp.add(self._startController(controller));
                })
                .then(function (controller) {
                    if (self.currentDialogController) {
                        self._closeDialog({silent: true});
                    }

                    // store the optional 'on_reverse_breadcrumb' handler
                    // AAB: store it on the AbstractAction instance, and call it
                    // automatically when the action is restored
                    if (options.on_reverse_breadcrumb) {
                        var currentAction = self.getCurrentAction();
                        if (currentAction) {
                            currentAction.on_reverse_breadcrumb = options.on_reverse_breadcrumb;
                        }
                    }

                    // update the internal state and the DOM
                    self._pushController(controller, options);

                    // toggle the fullscreen mode for actions in target='fullscreen'
                    self._toggleFullscreen();

                    // store the action into the sessionStorage so that it can be
                    // fully restored on F5
                    self.call('session_storage', 'setItem', 'current_action', action._originalAction);

                    return action;
                })
                .fail(function () {
                    self._removeAction(action.jsID);
                });
        },
        _appendController: function (controller) {
            //
            var self = this;
            var this_rpc = function () {
                return self._rpc({
                    model: 'ir.actions.actions',
                    method: 'get_action_id',
                    args: [controller.bind_tree_buttons]
                })
            };
            var rpc_then = function () {
                dom.append(self.$el, controller.widget.$el, {
                    in_DOM: self.isInDOM,
                    callbacks: [{widget: controller.widget}],
                });

                if (controller.scrollPosition) {
                    self.trigger_up('scrollTo', controller.scrollPosition);
                }

                if (!controller.widget.need_control_panel) {
                    self.controlPanel.do_hide();
                } else {
                    self.controlPanel.update({
                        breadcrumbs: self._getBreadcrumbs(),
                    }, {clear: false});
                }
            };
            // 判断是否有绑定tree_button，有的话则添加到头部
            if (controller.bind_tree_buttons && controller.bind_tree_buttons !== false) {
                this_rpc().then(function (button_list) {
                    var sidebar_ext = new SidebarExt(self, {tree_buttons: button_list});
                    sidebar_ext.reset_tree_buttons(self.controlPanel);
                    rpc_then()
                })
            } else {
                rpc_then()
            }
        },
    })

});