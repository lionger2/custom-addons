# -*- coding: utf-8 -*-
# from odoo import http


# class SiweiDev(http.Controller):
#     @http.route('/siwei_dev/siwei_dev/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/siwei_dev/siwei_dev/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('siwei_dev.listing', {
#             'root': '/siwei_dev/siwei_dev',
#             'objects': http.request.env['siwei_dev.siwei_dev'].search([]),
#         })

#     @http.route('/siwei_dev/siwei_dev/objects/<model("siwei_dev.siwei_dev"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('siwei_dev.object', {
#             'object': obj
#         })
