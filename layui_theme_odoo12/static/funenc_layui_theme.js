/**
 * Created by artorias on 2018/11/28.
 */
$(document).ready(function () {
    layui.config({
        base: '/layui_theme_odoo12/static/layui_admin/' //你存放新模块的目录，注意，不是layui的模块目录
    });

    layui.extend({
        index: 'index'
    });

    layui.use('index');
});