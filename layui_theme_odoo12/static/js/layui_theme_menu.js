/**
 * Created by artorias on 2018/11/30.
 */
odoo.define('layui_theme_menu', function (require) {
    "use strict";

    var SystrayMenu = require('web.SystrayMenu');
    var Menu = require('web.Menu');

    Menu.include({
        template: '',
        bind_click: function () {
            var self = this;
            this.$el.on('click', 'a[action][menu_id]', function (event) {
                event.preventDefault();
                self.do_action($(event.currentTarget).attr('action'), {clear_breadcrumbs: true})
            });
        },
        open_menu: function (menu_id, action) {
            this.$(".layui-this").removeClass("layui-this");
            var $clicked_menu = this.$('a[action=' + action + ']');
            $clicked_menu.parents('dd,li').addClass('layui-nav-itemed');
            $clicked_menu.parent().addClass("layui-this");
        },
        start: function () {
            var self = this;
            //绑定点击事件
            this.bind_click();
            // Systray Menu
            this.systray_menu = new SystrayMenu(this);
            this.systray_menu.attachTo(this.$el.parents('#LAY_app').find('.layui-header .layui-layout-right'));
            return $.when();
        },
        change_menu_section: function (primary_menu_id) {
            this.current_primary_menu = primary_menu_id;
            var action = this.getParent()._current_state.action;
            var menu_id = this.getParent()._current_state.menu_id;
            if (action && menu_id) {
                this.open_menu(menu_id, action)
            }
        },
        openFirstApp: function () {
            return
        }
    })

});