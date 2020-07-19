odoo.define('layui_search_panel', function (require) {
    "use strict";

    var core = require('web.core');
    var Widget = require('web.Widget');
    var proposition = require('layui_search_proposition');
    var layui_search_proposition = proposition.layui_search_proposition;
    var pyeval = require('web.py_utils');
    var widgetRegistry = require('web.widget_registry');

    var search_panel_default = Widget.extend({
        propositions: [],
        events: {
            'click .search_extend_reset': 'reset_search',
            'click .search_extend_apply': 'commit_search',
            'keyup .o_searchview_extended_prop_value': function (ev) {
                if (ev.which === $.ui.keyCode.ENTER) {
                    this.commit_search();
                }
            },
        },

        init: function (parent, fields, pannel_template, search_view) {
            this.fields = fields;
            this.pannel_template = pannel_template;
            this.search_view = search_view;
            this._super(parent, arguments);
        },

        reset_search: function () {
            // flag中没有search_view的时候不显示搜索
            if (this.search_view) {
                this.search_view.query.reset();
            }
            this.$('input').val("");
            this.$('select[class="o_input"]').find('option').removeAttr("selected");
            this.$('select[class="o_input"]').find('option').first().attr("selected", "selected")
        },

        // 读取模板，同时读取属性并构造搜索对象
        renderElement: function () {
            var $el;
            var bHaveExt = false;
            if (this.pannel_template) {
                this.propositions = [];
                $el = $(core.qweb.render(this.pannel_template, { widget: this }).trim());
                var fields_place_holders = $el.find("[for]");
                for (var i = 0; i < fields_place_holders.length; i++) {
                    var holder = fields_place_holders[i];
                    var filed_name = $(holder).attr('for');
                    var option = $(holder).attr('option') || '{"range": true}';
                    option = pyeval.py_eval(option);
                    var field = this.fields[filed_name];
                    if (field) {
                        var prop = new layui_search_proposition(this, field, option);
                        prop.appendTo(holder);
                        this.propositions.push(prop);
                        bHaveExt = true
                    }
                }
            } else {
                $el = this._make_descriptive();
            }

            this._replaceElement($el);
            if (bHaveExt) {
                this.do_show();
            } else {
                this.do_hide();
            }
        },

        commit_search: function () {
            var domains = [];
            _.each(this.propositions, function (proposition) {
                var domain = proposition.get_domain();
                if (!domain) {
                    return
                }
                // 针对时间做特别处理
                if (proposition.field.type == 'date' || proposition.field.type == 'datetime') {
                    if (domain.length == 2) {
                        var d1 = domain[0];
                        var d2 = domain[1];

                        if (!d1[2] || d1[2] == '' || !d2[2] || d2[2] == '') {
                            return
                        } else {
                            domains.push(domain)
                        }
                        return
                    }
                }

                domain = domain[0];
                if (domain[2] == '' || domain[2] == undefined) {
                    return
                } else {
                    domains.push([domain])
                }
            });
            this.trigger_up('search', {
                domains: domains
            });
        }
    });

    widgetRegistry.add("search_panel_default", search_panel_default);

    return search_panel_default
});