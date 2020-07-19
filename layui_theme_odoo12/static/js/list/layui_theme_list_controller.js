/**
 * Created by artorias on 2018/12/18.
 */
odoo.define('funenc_layui_theme_list', function (require) {
    "use strict";

    var ListController = require('web.ListController');
    var searchExt = require('layui_search_extend');

    ListController.include({
        customSearch: undefined,

        renderCustomArea: function ($node) {
            var self = this;
            var attrs = self.renderer.arch.attrs;
            if (attrs.search_ex_template) {
                if (!this.customSearch) {
                    this.customSearch = new searchExt(this, self.renderer.state.fields,
                        attrs.search_ex_template, attrs.search_pannel_js_class, self.searchview);
                    console.log($node)
                    this.customSearch.appendTo($node)
                }
            }
        },
    })

});