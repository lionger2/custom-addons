/**
 * Created by artorias on 2018/12/6.
 */
var url = 'http://' + window.location.host;

function loginOn(field) {
    var login = field.username;
    var password = field.password;
    var location_search = window.location.search;
    $.ajax({
        url: url + '/layui_theme_odoo12/admin_login',
        type: 'post',
        data: {
            login: login,
            password: password,
            location_search: location_search
        },
        success: (res) => {
            res = JSON.parse(res);
            if (res.isLogin) {
                layui.layer.msg('登入成功！加载中...', {
                    offset: '15px'
                    , icon: 1
                    , time: 1000
                }, function () {
                    window.location.href = url + res.url; //后台主页
                });
            } else {
                layui.layer.msg('账号或密码错误,登录失败！', {
                    offset: '15px'
                    , icon: 2
                    , time: 2000
                });
            }
        }
    })
}

layui.use(['form'], function () {
    var form = layui.form;
    //提交
    form.on('submit(LAY-user-login-submit)', function (data) {
        loginOn(data.field);
        return false;
    });
});