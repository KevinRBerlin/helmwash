# -*- coding: utf-8 -*-
 
from odoo import models, fields, api
 
class cuci_helm(models.Model):
    # ini akan berbentuk tabel nanti
    _name = 'cuci_helm.jeniscuci'
    _description = 'Daftar Jenis Pencucian'
    
    # ini merupakan field yang dibutuhkan untuk suatu record
    name = fields.Selection(string='Nama Jenis', selection=[('hanya luar','Hanya Luar'),('hanya dalam','Hanya Dalam'),('luar dalam','Luar Dalam'),('kilat','Kilat')])
    air = fields.Selection(string='Jenis Air',
                            selection=[('hot water', 'Hot Water'), ('cold water', 'Cold Water'), ('normal water', 'Normal Water'), ('special water', 'Special Water')],
                            required=True
    )
    
    kotoran =  fields.Selection(string='Tipe Kotoran',
                            selection=[('ringan', 'Ringan'), ('sedang', 'Sedang'), ('berat', 'Berat')],
                            required=True
    )
    
    tersedia = fields.Boolean(string='tersedia',
                             default=True
    )
    
    deskripsi = fields.Char(string='deskripsi',
                            help='isi dengan alat yang digunakan untuk mencuci')
    models_id = fields.One2many(string="jenis_helm", inverse_name='jenis_id',comodel_name='cuci_helm.jeniscucihelm')