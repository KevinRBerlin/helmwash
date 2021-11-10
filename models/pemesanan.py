# -*- coding: utf-8 -*-
 
from odoo import models, fields, api
 
class Pemesanan(models.Model):
    # ini akan berbentuk tabel nanti
    _name = 'cuci_helm.pemesanan'
    _description = 'Daftar Pemesanan'
   
    tanggal_pesan = fields.Datetime(string='Tanggal Pesanan', default=fields.Datetime.now)
    detailcucian_ids = fields.One2many('cuci_helm.detailpesanan', 'pesan_id', string='Detail pesan')
    jumlah_pesanan = fields.Integer(compute='_compute_jumlah_pesanan', string='Jumlah Pesanan')
    total_harga = fields.Char(compute='_compute_total_harga', string='Total Tagihan')

    @api.model
    def _compute_total_harga(self):
        # mapped = untuk mengambil satu atribunt saja
        # self.env---.mapped = mengembalikan suatu list
        for record in self:
            total = sum(self.env['cuci_helm.detailpesanan'].search([('pesan_id','=',record.id)]).mapped('jumlah_harga'))
            record.total_harga = total
   
    @api.depends('detailcucian_ids')
    def _compute_jumlah_pesanan(self):
        for record in self:
            record.jumlah_pesanan = len(record.detailcucian_ids)
 
class detailPesanan(models.Model):
    _name = 'cuci_helm.detailpesanan'
    _description = 'Detail Pesanan Cuci'
 
    name = fields.Char(string='Kode pesan')
    pesan_id = fields.Many2one('cuci_helm.pemesanan', string='Pemesanan')
    models_id = fields.Many2one('cuci_helm.jeniscucihelm', string='Jenis Helm')
    harga = fields.Integer(compute='_compute_harga', string='Harga (per helm)')
    jumlah = fields.Integer(string='Jumlah helm')
    jumlah_harga = fields.Integer(compute='_compute_jumlah_harga', string='Jumlah Harga')
   
    @api.depends('jumlah')
    def _compute_jumlah_harga(self):
        for record in self:
            record.jumlah_harga = record.harga * record.jumlah
   
    @api.depends('models_id')
    def _compute_harga(self):
        for record in self:
            record.harga = record.models_id.harga
