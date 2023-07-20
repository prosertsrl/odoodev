# -*- coding: utf-8 -*-
# from odoo import http


# class Votantes(http.Controller):
#     @http.route('/votantes/votantes', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/votantes/votantes/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('votantes.listing', {
#             'root': '/votantes/votantes',
#             'objects': http.request.env['votantes.votantes'].search([]),
#         })

#     @http.route('/votantes/votantes/objects/<model("votantes.votantes"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('votantes.object', {
#             'object': obj
#         })
