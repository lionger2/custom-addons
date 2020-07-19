# -*- coding: utf-8 -*-
import json
import base64

from odoo import http, exceptions
from odoo.http import request

from odoo.addons.web.controllers.main import Home, ensure_db


# 重写登录页面接口
class UserLogin(Home):
    @http.route('/web/login', type='http', auth="public", csrf=False)
    def web_login(self, redirect=None, **kw):
        res = http.request.env.ref('layui_theme_odoo12.funenc_layui_theme_login', False)
        if res is not False:
            ensure_db()
            request.params['login_success'] = False
            if request.httprequest.method == 'GET' and redirect and request.session.uid:
                return http.redirect_with_hash(redirect)
            else:
                values = request.env['layui_theme_odoo12.config'].sudo().get_values()
                return http.request.render('layui_theme_odoo12.funenc_layui_theme_login', values)
        else:
            return super().web_login(redirect, **kw)


class LayuiTheme(http.Controller):
    @http.route('/layui_theme_odoo12/admin_login', type='http', auth="public", methods=['POST'],
                csrf=False)
    def admin_login(self, **kwargs):
        '''
        登录函数
        :param kwargs:
        :return: {isLogin: 是否成功登录(Bool), msg: [Message](str), url: 跳转地址(str)}
        '''
        ensure_db()
        login_uid = kwargs['login']
        login_pwd = kwargs['password']
        try:
            request.session.authenticate(request.session.db, login_uid, login_pwd)
            # 退出登录函数
            # request.session.logout()
            res = {
                "isLogin": True,
                "msg": "login success!",
                "url": "/web" if kwargs['location_search'] == '' else "/web{}".format(kwargs['location_search'])
            }
        except exceptions.AccessDenied as e:
            res = {
                "isLogin": False
            }
        return json.dumps(res)

    # 获取logo
    @http.route('/layui_theme_odoo12/logo', auth='user', type='http', methods=['GET'])
    def get_logo(self):
        values = request.env['layui_theme_odoo12.config'].sudo().get_values()
        image_content = base64.b64decode(values['logo'])
        headers = [('Content-Type', 'image/png'), ('Content-Length', len(image_content))]
        response = request.make_response(image_content, headers)
        response.status_code = 200
        return response

    # 获取logo_mini
    @http.route('/layui_theme_odoo12/logo_mini', auth='user', type='http', methods=['GET'])
    def get_logo_mini(self):
        values = request.env['layui_theme_odoo12.config'].sudo().get_values()
        image_content = base64.b64decode(values['logo_mini'])
        headers = [('Content-Type', 'image/png'), ('Content-Length', len(image_content))]
        response = request.make_response(image_content, headers)
        response.status_code = 200
        return response


