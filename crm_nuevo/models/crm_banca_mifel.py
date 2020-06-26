# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CrmInherit(models.Model):
    _inherit = 'crm'

    subcatalog = fields.Selection([ ('call','Llamada') , ('visit','Visita')],string="Tipo de Contacto", required=True)
    status_etapa1 = fields.Selection([('rejected', 'Rechazo'), ('accepted', 'Aceptado'), ('pending', 'Pendiente')],string="Estatus de Etapa", default='pending')
    status_etapa2 = fields.Selection([('rejected', 'Rechazo'), ('accepted', 'Aceptado'), ('pending', 'Pendiente')],string="Estatus de Etapa", default='pending')
    status_etapa3 = fields.Selection([('rejected', 'Rechazo'), ('accepted', 'Aceptado'), ('pending', 'Pendiente')],string="Estatus de Etapa", default='pending')
    status_etapa4 = fields.Selection([('rejected', 'Rechazo'), ('accepted', 'Aceptado'), ('pending', 'Pendiente')],string="Estatus de Etapa", default='pending')
    status_etapa5 = fields.Selection([('rejected', 'Rechazo'), ('accepted', 'Aceptado'), ('pending', 'Pendiente')],string="Estatus de Etapa", default='pending')
    solicitud_financiera = fields.Binary(string="Solicitud Financiera", required=True)
    deal_screen = fields.Binary(string="Deal Screen", required=True)
