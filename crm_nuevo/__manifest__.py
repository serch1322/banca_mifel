# -*- coding: utf-8 -*-
{
    'name': 'CRM BANCA MIFEL',
    'author': 'IT REINGENIERIAS',
    'summary': 'Modulo para manejar 3 productos con diferentes procesos de venta dentro de la vista de CRM',
    'version': '0.1',
    'data': [
        'data/crm_mail_vendedor_pendiente.xml',
        'data/crm_mail_data.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/view_crm_banca_mifel.xml',

    ],
    'depends': [
        'base',
        'crm',
        'mail',
    ],
}