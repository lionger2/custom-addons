odoo.define('layui_search_extend', function (require) {
    "use strict";

    var Widget = require('web.Widget');
    var widgetRegistry = require('web.widget_registry');

    var search_extend = Widget.extend({
        search_view: undefined,
        init: function (parent, fields, template, search_pannel_js_class, search_view) {
            this.propositions = [];
            this.custom_filters_open = false;
            this.fields = fields;
            // 不直接使用template，这样会闪烁
            this.pannel_template = template;
            this.search_pannel_js_class = search_pannel_js_class;
            this.search_view = search_view;
            this._super(parent);
        },

        start: function () {
            this.props = [];
            var js_class = this.search_pannel_js_class;
            if (!js_class || js_class === '') {
                js_class = 'search_panel_default'
            }
            var search_widget = widgetRegistry.get(js_class);
            if (search_widget) {
                var pannel = new search_widget(this, this.fields, this.pannel_template, this.search_view);
                pannel.appendTo(this.$el)
            } else {
                console.log("can not find the search widget");
            }
        }
    });

    return search_extend
});