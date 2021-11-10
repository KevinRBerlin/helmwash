# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ModelDasar(models.Model):
    _name = 'cuci_helm.base'
    _description = 'model dasar cuci helm'
 
    ukuran = fields.Char(string="ukuran helm", required=True)
    tipe = fields.Selection(string="tipe/jenis helm", selection=[('standart', 'Standart'),
    ('full face','Full Face'), ('bogo','Bogo'),('mips','MIPS'),('off-road','Off-Road')])


class cuci_helm(models.Model):
    _name = 'cuci_helm.jeniscucihelm'
    _description = 'Daftar jenis jenis pencucian'
    _inherit = "cuci_helm.base"
    
    name = fields.Char(string='jenis Pencucian', required=True)
    harga = fields.Integer(string='Harga pencucian', required=True)
    active = fields.Boolean(default=True)
    jenis_id = fields.Many2one(comodel_name="cuci_helm.jeniscuci", string='jenis pencucian',required=True, delegate=True )

    @api.constrains('name')
    def _constrains_name(self):
        for rec in self:
            duplicate = self.env['cuci_helm.jeniscucihelm'].search([('name','=',rec.name)])
            if len(duplicate)>1:
                raise ValidationError("helm Cucian %s Sudah Ada di Daftar!! %s" % (str(rec.name).upper(),str(len(duplicate))))
 
    @api.onchange('tipe')
    def _onchange_tipe(self):
        # jika atribut 'tipe' berubah maka akan muncul suatu warning
        if self.tipe == 'standar':
            return {
                'warning': {
                    'title' : 'Jenis Cuci',
                    'message' : 'Jenis Cuci harus golongan B'
                }
            }
        elif self.tipe == 'bogo':
            return {
                'warning': {
                    'title' : 'Jenis Cuci',
                    'message' : 'Jenis Cuci harus golongan A'
                }
            }
