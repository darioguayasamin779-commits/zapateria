from odoo import models, fields

class Garantia(models.Model):
    _name = 'zapateria.garantia'
    _description = 'Garantías'

    codigo = fields.Char(string='Código')

    fecha_inicio = fields.Date(string='Fecha Inicio')

    fecha_fin = fields.Date(string='Fecha Fin'
    )

    descripcion = fields.Text(string='Descripción')

    estado = fields.Selection([
        ('activa', 'Activa'),
        ('vencida', 'Vencida')], 
        string='Estado')

    zapato_id = fields.Many2one('zapatos.zapato', string='Zapato',required=True)