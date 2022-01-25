# -*- coding: utf-8 -*-
# from odoo import http


# class DyD(http.Controller):
#     @http.route('/dy_d/dy_d/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dy_d/dy_d/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('dy_d.listing', {
#             'root': '/dy_d/dy_d',
#             'objects': http.request.env['dy_d.dy_d'].search([]),
#         })

#     @http.route('/dy_d/dy_d/objects/<model("dy_d.dy_d"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dy_d.object', {
#             'object': obj
#         })
