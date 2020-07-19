odoo.define('layui_theme_basic_controller', function (require) {
    "use strict";

    var AbstractController = require('web.AbstractController');

    AbstractController.include({
        renderCustomArea: function () {
            console.log('render custom area');
            // 渲染自定义区域
        },

        renderCustomTopArea: function () {
            // 渲染top区域
            console.log('render top area');
        },

        renderCustomBottomArea: function () {
            // 渲染buttom区域
            console.log('render bottom area');
        },

        _renderControlPanelElements: function () {
            var elements = {};

            if (this.withControlPanel) {
                elements = {
                    $buttons: $('<div>'),
                    $sidebar: $('<div>'),
                    $pager: $('<div>'),
                    $customArea: $('<div id="test-customArea">'),
                };

                this.renderButtons(elements.$buttons);
                this.renderSidebar(elements.$sidebar);
                this.renderPager(elements.$pager);
                this.renderCustomArea(elements.$customArea);
                // remove the unnecessary outer div
                elements = _.mapObject(elements, function ($node) {
                    return $node && $node.contents();
                });
                elements.$switch_buttons = this._renderSwitchButtons();
            }
            return elements;
        },

        is_action_enabled: function (action) {
            var context = this.model.get(this.handle).getContext();
            return this.activeActions[action] | context[action];
        },
    })
});