# -*- coding: utf-8 -*-
from odoo import http

# class SiweiWebsite(http.Controller):
#     @http.route('/siwei_website/siwei_website/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/siwei_website/siwei_website/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('siwei_website.listing', {
#             'root': '/siwei_website/siwei_website',
#             'objects': http.request.env['siwei_website.siwei_website'].search([]),
#         })

#     @http.route('/siwei_website/siwei_website/objects/<model("siwei_website.siwei_website"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('siwei_website.object', {
#             'object': obj
#         })