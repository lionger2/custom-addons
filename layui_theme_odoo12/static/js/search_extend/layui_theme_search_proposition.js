odoo.define('layui_search_proposition', function (require) {
    "use strict";

    var core = require('web.core');
    var Widget = require('web.Widget');
    var datepicker = require('web.datepicker');

    var _t = core._t;
    var _lt = core._lt;

    var Field = Widget.extend({
        init: function (parent, field, option) {
            this._super(parent);
            this.field = field;
            this.option = option
        },
        get_label: function (field, operator) {
            var format;
            switch (operator.value) {
                case '∃':
                case '∄':
                    format = _t('%(field)s %(operator)s');
                    break;
                default:
                    format = _t('%(field)s %(operator)s "%(value)s"');
                    break;
            }
            return this.format_label(format, field, operator);
        },
        format_label: function (format, field, operator) {
            return _.str.sprintf(format, {
                field: field.string,
                // According to spec, HTMLOptionElement#label should return
                // HTMLOptionElement#text when not defined/empty, but it does
                // not in older Webkit (between Safari 5.1.5 and Chrome 17) and
                // Gecko (pre Firefox 7) browsers, so we need a manual fallback
                // for those
                operator: operator.label || operator.text,
                value: this
            });
        },
        get_domain: function (field, operator) {
            switch (operator.value) {
                case '∃':
                    return [[field.name, '!=', false]];
                case '∄':
                    return [[field.name, '=', false]];
                default:
                    return [[field.name, operator.value, this.get_value()]];
            }
        },
        show_inputs: function ($operator) {
            var $value = this.$el.parent();
            switch ($operator.val()) {
                case '∃':
                case '∄':
                    $value.hide();
                    break;
                default:
                    $value.show();
            }
        },
        /**
         * Returns a human-readable version of the value, in case the "logical"
         * and the "semantic" values of a field differ (as for selection fields,
         * for instance).
         *
         * The default implementation simply returns the value itself.
         *
         * @return {String} human-readable version of the value
         */
        toString: function () {
            return this.get_value();
        }
    });

    var LayMany2One = Field.extend({
        template: 'lay_selection',
        selection: [],
        operators: [
            {value: "=", text: _lt("is")},
            {value: "!=", text: _lt("is not")},
            {value: "∃", text: _lt("is set")},
            {value: "∄", text: _lt("is not set")}
        ],

        willStart: function () {
            this._super();
            var self = this;
            var def = $.Deferred();
            this._rpc({
                model: this.field.relation,
                method: 'name_search'
            }).then(function (results) {
                self.selection = results;
                self.selection.unshift([0, '']);
                def.resolve()
            });
            return def
        },

        toString: function () {
            var select = this.$el[0];
            var option = select.options[select.selectedIndex];
            return option.label || option.text;
        },

        get_domain: function (field, operator) {
            return [[field.name, operator.value, this.get_value()]];
        },

        get_value: function () {
            var select = this.$el[0];
            var option = select.options[select.selectedIndex];
            return option.text;
        }
    });

    var LayAutoCompelete = Field.extend({
        template: 'lay_selection',
        selection: [],
        operators: [
            {value: "=", text: _lt("is")},
            {value: "!=", text: _lt("is not")},
            {value: "∃", text: _lt("is set")},
            {value: "∄", text: _lt("is not set")}
        ],

        toString: function () {
            var select = this.$el[0];
            var option = select.options[select.selectedIndex];
            return option.label || option.text;
        },

        get_domain: function (field, operator) {
            return [[field.name, operator.value, this.get_value()]];
        },

        get_value: function () {
            var select = this.$el[0];
            var option = select.options[select.selectedIndex];
            return option.text;
        }
    });

    var Lay_DateTime = Field.extend({
        tagName: 'span',
        attributes: {
            type: 'datetime'
        },

        operators: [
            {value: "between", text: _lt("is between")},
            {value: "=", text: _lt("is equal to")},
            {value: "!=", text: _lt("is not equal to")},
            {value: ">=", text: _lt("is after")},
            {value: "<=", text: _lt("is before")},
            {value: "∃", text: _lt("is set")},
            {value: "∄", text: _lt("is not set")}
        ],

        get_value: function (operator, index) {
            // retrieve the datepicker value
            var value = this["datewidget"].getValue();
            if (operator.value == 'between') {
                var ar = value.split('~');
                if (index == 0) {
                    value = ar[0]
                } else {
                    value = ar[1]
                }
                // 转换为utc时间
                return moment(value).add(-this.getSession().getTZOffset(value), 'minutes').format();
            } else {
                // 转换为utc时间
                value = moment(value).add(-this.getSession().getTZOffset(value), 'minutes')
                return value.format();
            }
        },

        get_domain: function (field, operator) {
            switch (operator.value) {
                case '∃':
                    return [[field.name, '!=', false]];
                case '∄':
                    return [[field.name, '=', false]];
                case 'between':
                    var value = this["datewidget"].getValue();
                    if (!value || value == '') {
                        return false
                    } else {
                        return [[field.name, '>=', this.get_value(operator, 0)], [field.name, '<=', this.get_value(operator, 1)]];
                    }
                default:
                    return [[field.name, operator.value, this.get_value(operator, 0)]];
            }
        },

        toString: function () {
            return this["datewidget"].getValue();
        },

        start: function () {
            return $.when(
                this._super.apply(this, arguments),
                this._create_new_widget("datewidget")
            );
        },

        _create_new_widget: function (name) {
            this[name] = new (this._get_widget_class())(this, this.option);
            return this[name].appendTo(this.$el).then((function () {
                // 如果是时间范围则不设置值
                if (this.option && this.option.range) {
                    return
                }
                this[name].setValue(moment(new Date()));
            }).bind(this));
        },

        _get_widget_class: function () {
            return datepicker.DateTimeWidget;
        }
    });

    var Lay_date = Lay_DateTime.extend({
        attributes: {
            type: 'date'
        },

        _get_widget_class: function () {
            return datepicker.DateWidget;
        },

        get_value: function (operator, index) {
            // retrieve the datepicker value
            var value = this["datewidget"].getValue();
            value = moment(value).add(-this.getSession().getTZOffset(value), 'minutes');
            return value.format('YYYY-MM-DD');
        },
    });

    // check box 以key val的形式给出
    var LayMany2OneCheckBox = LayMany2One.extend({
        template: 'lay_many2one_checkbox',
        check_boxs: [],
        domain: [],
        init: function () {
            this._super.apply(this, arguments);
            this.domain = this.option.domain || []
        },

        willStart: function () {
            this._super();
            var self = this;
            var def = $.Deferred();
            this._rpc({
                model: this.field.relation,
                method: 'search_read',
                domain: this.domain,
                fields: ['id', 'name']
            }).then(function (results) {
                self.selection = results;
                def.resolve()
            });
            return def
        },

        toString: function () {
            return this.get_value();
        },

        get_domain: function (field, operator) {
            return [[field.name, 'in', this.get_value()]];
        },

        get_value: function () {
            var vals = [];
            var sels = this.$("input:checked");
            $.each(sels, function () {
                vals.push(parseInt($(this).val()))
            });
            return vals
        }
    });

    // check box 以key val的形式给出
    var LaySelectionCheckBox = Field.extend({
        template: 'lay_selection_checkbox',
        check_boxs: [],
        domain: [],
        init: function () {
            this._super.apply(this, arguments);
            this.selections = this.option.selections || []
        },

        toString: function () {
            return this.get_value();
        },

        get_domain: function (field, operator) {
            return [[field.name, 'in', this.get_value()]];
        },

        get_value: function () {
            var vals = [];
            var sels = this.$("input:checked");
            $.each(sels, function () {
                vals.push($(this).val())
            });
            return vals
        }
    });

    core.search_filters_registry.add('Lay_DateTime', Lay_DateTime);
    core.search_filters_registry.add('LayAutoComplete', LayAutoCompelete);
    core.search_filters_registry.add('LayMany2One', LayMany2One);
    core.search_filters_registry.add('LayMany2OneCheckBox', LayMany2OneCheckBox);
    core.search_filters_registry.add('LaySelectionCheckBox', LaySelectionCheckBox);

    var layui_search_proposition = Widget.extend({
        field: undefined,
        options: {range: false},
        init: function (parent, field, options) {
            this._super(parent);
            this.field = field;
            this.options = options
        },

        needShowRange: function () {
            if (this.options && this.options.range) {
                return true
            }
            return false
        },

        start: function () {
            var type = this.field.type;
            // 根据option进使用特定的组件
            if (this.options.filed_type) {
                type = this.options.filed_type
            }
            var Field = core.search_filters_registry.getAny([type, "char"]);
            if (type == 'date') {
                this.value = new Lay_date(this, this.field, {
                    range: this.needShowRange()
                });
            } else if (type == 'datetime') {
                this.value = new Lay_DateTime(this, this.field, {
                    range: this.needShowRange()
                });
            } else if (type == 'many2one' && this.options.many2one) {
                this.value = new LayMany2One(this, this.field);
            } else {
                this.value = new Field(this, this.field, this.options);
            }

            this.value.appendTo(this.$el);
            if (type == 'selection') {
                this.$('select').prepend('<option value="" selected="selected">全部</option>')
            }
            this.value.show_inputs({
                val: function () {
                    return ''
                },
                range: this.needShowRange
            });
        },

        get_domain: function () {
            var field = this.field;
            var operator = this.value.operators[0];
            if (this.needShowRange() && (field.type == 'date_time' || field.type == 'date')) {
                return this.value.get_domain(field, {
                    value: 'between'
                })
            } else if (field.type == 'date_time' || field.type == 'date') {
                return this.value.get_domain(field, {
                    value: '='
                })
            } else {
                return this.value.get_domain(field, operator)
            }
        },

        get_filter: function () {
            var field = this.field;
            var operator = this.value.operators[0];
            return {
                attrs: {
                    domain: this.value.get_domain(field, operator),
                    string: this.value.get_label(field, operator),
                },
                children: [],
                tag: 'filter'
            };
        },
    });

    return {
        layui_search_proposition: layui_search_proposition,
        Field: Field,
        Lay_DateTime: Lay_DateTime,
        Lay_date: Lay_date
    };
});