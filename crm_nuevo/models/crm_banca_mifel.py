# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime

class CrmInherit(models.Model):
    _inherit = ['crm.lead']

    subcatalog = fields.Selection([ ('call','Llamada') , ('visit','Visita')],string="Tipo de Contacto", required=True)
    origen_prospecto = fields.Selection([('broker','Broker'),('own','Prospección Propia'),('reference','Referenciado')], string="Origen de Prospecto", required=True)
    status_etapa1 = fields.Selection([('rejected', 'Rechazo'), ('accepted', 'Aceptado'), ('pending', 'Pendiente')],string="Estatus de Etapa", default='pending')
    status_etapa2 = fields.Selection([('rejected', 'Rechazo'), ('accepted', 'Aceptado'), ('pending', 'Pendiente')],string="Estatus de Etapa", default='pending')
    status_etapa3 = fields.Selection([('rejected', 'Rechazo'), ('accepted', 'Aceptado'), ('pending', 'Pendiente')],string="Estatus de Etapa", default='pending')
    status_etapa4 = fields.Selection([('rejected', 'Rechazo'), ('accepted', 'Aceptado'), ('pending', 'Pendiente')],string="Estatus de Etapa", default='pending')
    status_etapa5 = fields.Selection([('rejected', 'Rechazo'), ('accepted', 'Aceptado'), ('pending', 'Pendiente')],string="Estatus de Etapa", default='pending')
    state = fields.Selection([('stage_1', 'Primer Contacto Cliente'),('stage_2','Solicitud de Estados Financieros'), ('stage_3','Elaboración de Deal Screen'),('stage_4','Revisión con Dirección'),('stage_5','Pre-Comite'), ('accepted','Aceptado'), ('rejected','Rechazado')],string="Etapa Producto 1", default='stage_1')
    solicitud_financiera = fields.Binary(string="Solicitud Financiera", attachment=False, store=True)
    deal_screen = fields.Binary(string="Deal Screen", attachment=False, store=True)
    fecha_actualizada = fields.Datetime(string="Última Actualización", default=fields.Datetime.now, readonly=True)

    #Actualizar fecha de registro
    @api.onchange('state')
    def onchage_fecha_actualizada(self):
        self.fecha_actualizada = datetime.datetime.now()
    #Botones para cambiar de Etapa
    def action_stage_2(self):
        self.state = 'stage_2'

    def action_stage_3(self):
        self.state = 'stage_3'

    def action_stage_4(self):
        self.state = 'stage_4'

    def action_stage_5(self):
        self.state = 'stage_5'

    def action_won(self):
        self.state = 'accepted'

    def action_lost(self):
        self.state = 'rejected'

    #Mandar Correo a Vendedor Atrasado
    @api.model
    def notificar_vendedor(self):
        prospectos = self.env['crm.lead'].search([])
        now = datetime.datetime.now()
        for prospecto in prospectos:
            if prospecto.state == 'stage_4' or prospecto.state == 'stage_5':
                return True
            elif now >= prospecto.fecha_actualizada + datetime.timedelta(days=3) or not prospecto.state == 'won' or not prospecto.state == 'lost':
                 template = self.env.ref('crm_nuevo.crm_vendedor_correo_recordatorio')
                 template.send_mail('crm.model_crm_lead', force_send=True)
        return True

    # Mandar Correo a Vendedor Atrasado
    @api.model
    def notificar_vendedor(self):
        prospectos = self.env['crm.lead'].search([])
        now = datetime.datetime.now()
        for prospecto in prospectos:
            if prospecto.state == 'stage_4' or prospecto.state == 'stage_5':
                return True
            elif now >= prospecto.fecha_actualizada + datetime.timedelta(
                    days=3) or not prospecto.state == 'won' or not prospecto.state == 'lost':
                template = self.env.ref('crm_nuevo.crm_vendedor_correo_recordatorio')
                template.send_mail('crm.model_crm_lead', force_send=True)
        return True


