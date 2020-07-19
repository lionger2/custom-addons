/**
 * Created by artorias on 2018/11/30.
 */
odoo.define('layui_theme_web_client', function (require) {
    "use strict";

    var Menu = require('web.Menu');
    var WebClient = require('web.WebClient');
    var session = require('web.session');

    WebClient.include({
        show_application: function () {
            var self = this;
            this.set_title();

            return this.instanciate_menu_widgets().then(function () {
                $(window).bind('hashchange', self.on_hashchange);
                // If the url's state is empty, we execute the user's home action if there is one (we
                // show the first app if not)
                if (_.isEmpty($.bbq.getState(true))) {
                    return self._rpc({
                        model: 'res.users',
                        method: 'read',
                        args: [session.uid, ["action_id"]],
                    })
                        .then(function (result) {
                            var data = result[0];
                            if (data.action_id) {
                                self.menu.change_menu_section(self.menu.action_id_to_primary_menu_id(data.action_id[0]));
                                return self.do_action(data.action_id[0]);
                            } else {
                                self.menu.openFirstApp();
                            }
                        });
                } else {
                    return self.on_hashchange();
                }
            });
        },

        instanciate_menu_widgets: function () {
            var self = this;
            // var defs = [];
            return this.load_menus().then(function (menuData) {
                self.menu_data = menuData;

                // Here, we instanciate every menu widgets and we immediately append them into dummy
                // document fragments, so that their `start` method are executed before inserting them
                // into the DOM.
                if (self.menu) {
                    self.menu.destroy();
                }
                self.menu = new Menu(self, menuData);
                self.menu.setElement(self.$el.parents().find('#LAY-system-side-menu'));
                return $.when().then(function () {
                    self.menu.start();
                });
            });
        },
    })

});