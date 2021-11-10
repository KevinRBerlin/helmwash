# -*- coding: utf-8 -*-
# from odoo import http


# class CuciHelm(http.Controller):
#     @http.route('/cuci_helm/cuci_helm/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cuci_helm/cuci_helm/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('cuci_helm.listing', {
#             'root': '/cuci_helm/cuci_helm',
#             'objects': http.request.env['cuci_helm.cuci_helm'].search([]),
#         })

#     @http.route('/cuci_helm/cuci_helm/objects/<model("cuci_helm.cuci_helm"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cuci_helm.object', {
#             'object': obj
#         })
