# !user/bin/env python3
# -*- coding: utf-8 -*-
# Author: Artorias
'''
继承原有的密码检查方法，并添加了新的绕过密码自定义验证方法，只要后续开发的模块依赖layui_theme，并在_inherit = res.users的模块中
重写check_login_source即可，函数若return True则可跳过密码直接登录，若return False则进行原有的密码验证
'''
from odoo import models, api


class ThemeUsers(models.Model):

    _inherit = 'res.users'

    @staticmethod
    def check_login_source(password):
        '''
        添加的自定义验证函数，在odoo自带验证的基础上加入自定的验证规则，可以继承res.users并改写这个方法，
        验证成功返回True，验证失败返回False
        :param password:
        :return:
        '''
        return False

    @api.model
    def _check_credentials(self, password):
        '''
        改写了原有的_check_credentials函数，原有方法检查成功，则不抛错，直接return，所以通过是否抛错来绕过验证。
        在验证之前加入了一个自定的验证函数
        :param password: 传入的密码
        :return:
        '''
        check_result = self.check_login_source(password)
        if check_result is True:
            return
        else:
            super()._check_credentials(password)
