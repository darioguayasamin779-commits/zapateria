from odoo import models, fields

class Devolucion(models.Model):
    _name = 'zapateria.devolucion'
    _description = 'Devoluciones'

    codigo = fields.Char(string='Código',required=True)

    fecha = fields.Date(string='Fecha')

    motivo = fields.Text(string='Motivo')

    estado = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('aprobada', 'Aprobada'),
        ('rechazada', 'Rechazada') ], string='Estado')

    zapato_id = fields.Many2one('zapatos.zapato',string='Zapato',required=True)