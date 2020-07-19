/**
 * Created by artorias on 2018/12/11.
 */
odoo.define('layui_list_renderer', function (require) {
    'use strict';

    var ListRenderer = require('web.ListRenderer');
    var config = require('web.config');
    var layui_pager = require('layui_pager');
    var AbstractField = require('web.AbstractField');
    var AbstractController = require('web.AbstractController');

    ListRenderer.include({
        /**
         * 添加trigger_up触发事件
         */
        custom_events: _.extend({}, ListRenderer.prototype.custom_events, {
            layui_pager_change: '_layui_pager_change'
        }),
        /**
         * 如果父类是field类型时触发
         */
        field_change_render: function (limit, this_offset) {
            var self = this;
            self.trigger_up('load', {
                id: self.getParent().value.id,
                limit: limit,
                offset: this_offset,
                on_success: function (value) {
                    self.getParent().value = value;
                    self.getParent()._render();
                    self.getParent().pager.state.current_min = this_offset + 1;
                    self.getParent().pager.state.limit = limit;
                    self.getParent().pager.state.size = self.state.count;
                    self.getParent().pager._render()
                },
            });
        },
        /**
         * 如果父类是controller
         * @param limit 每页显示条数
         * @param this_offset 查询偏移量
         */
        controller_change_render: function (limit, this_offset) {
            var self = this;
            this.getParent().reload({limit: limit, offset: this_offset}).then(function () {
                self._renderLayuiPager(self, self.state.count)
            })
        },
        /**
         * 分页栏更改的时候触发
         * @param event
         * @private
         */
        _layui_pager_change: function (event) {
            var self = this;
            var limit = event.data.limit;
            var curr = event.data.curr;
            var this_offset = (curr - 1) * limit - 1 < 0 ? 0 : (curr - 1) * limit;
            // 如果父类是field
            if (self.getParent() instanceof AbstractField) {
                self.field_change_render(limit, this_offset)
            }
            // 如果父类是controller
            else if (self.getParent() instanceof AbstractController) {
                self.controller_change_render(limit, this_offset)
            }
        },
        /**
         * 渲染分页栏
         * @private
         */
        _renderLayuiPager: function () {
            // 页数大于1时才渲染
            if (Math.ceil(this.state.count / this.state.limit) > 1) {
                var pager = new layui_pager(this);
                pager.appendTo(this.$el)
            }
        },
        /**
         * 添加Layui-table的样式, 添加分页栏, group分组的时候不展示分页
         * @returns {*|Promise|PromiseLike<T | never>|Promise<T | never>}
         * @private
         */
        _renderView: function () {
            var self = this;
            return this._super().then(function () {
                self.$('table').removeClass().addClass('layui-table o_list_view');
                if (self.isGrouped === false) {
                    self._renderLayuiPager()
                }
            })
        },
        /**
         * 添加widget的表格头
         * @param node
         * @returns {*}
         * @private
         */
        _renderHeaderCell: function (node) {
            var name = node.attrs.name;
            var order = this.state.orderedBy;
            var isNodeSorted = order[0] && order[0].name === name;
            var field = this.state.fields[name];
            var $th = $('<th>');
            // 添加widget的string表格头
            if (node.tag === "widget" && node.attrs.string && !field) {
                return $th.text(node.attrs.string)
            } else if (!field) {
                return $th;
            }
            var description;
            if (node.attrs.widget) {
                description = this.state.fieldsInfo.list[name].Widget.prototype.description;
            }
            if (description === undefined) {
                description = node.attrs.string || field.string;
            }
            $th.text(description)
                .data('name', name)
                .toggleClass('o-sort-down', isNodeSorted ? !order[0].asc : false)
                .toggleClass('o-sort-up', isNodeSorted ? order[0].asc : false)
                .addClass(field.sortable && 'o_column_sortable');

            if (isNodeSorted) {
                $th.attr('aria-sort', order[0].asc ? 'ascending' : 'descending');
            }

            if (field.type === 'float' || field.type === 'integer' || field.type === 'monetary') {
                $th.css({textAlign: 'right'});
            }

            if (config.debug) {
                var fieldDescr = {
                    field: field,
                    name: name,
                    string: description || name,
                    record: this.state,
                    attrs: node.attrs,
                };
                this._addFieldTooltip(fieldDescr, $th);
            }
            return $th;
        },
        /**
         * footer内容为空时不显示
         * @private
         */
        _renderFooter: function () {
            var aggregates = {};
            _.each(this.columns, function (column) {
                if ('aggregate' in column) {
                    aggregates[column.attrs.name] = column.aggregate;
                }
            });
            var $cells = this._renderAggregateCells(aggregates, false);
            if (this.hasSelectors) {
                $cells.unshift($('<td>'));
            }
            $cells.forEach(function (val, index) {
                if (val.children()) {
                    return $('<tfoot>').append($('<tr>').append($cells));
                }
            });
            return
        },
        /**
         * class有noOpen时不打开tree
         * @param event
         * @returns {boolean}
         * @private
         */
        _onRowClicked: function (event) {
            var self = this;
            if (self.arch.attrs.no_open === "true" || this.$el.hasClass("noOpen")) {
                return false;
            }
            self._super(event)
        }
    })
});