from odoo import models, fields, api
 
class ZapatosZapato(models.Model):
    _inherit = 'zapatos.zapato'
 
    codigo = fields.Char(string='codigo')
    marca = fields.Char(string='marca')
    color = fields.Char(string='color')
    material = fields.Char(string='material')
    descripcion = fields.Text(string='descripcion')
    stock_minimo = fields.Integer(string='stock_minimo', default=5)
    descuento = fields.Boolean(string='descuento', default=False) 
    genero = fields.Selection([
        ('hombre', 'Hombre'),
        ('mujer', 'Mujer'),
        ('unisex', 'Unisex'),
        ('nino', 'Niño'),
    ], string='Género')
    tipo_calzado = fields.Selection([
        ('deportivo', 'Deportivo'),
        ('formal', 'Formal'),
        ('casual', 'Casual'),
        ('sandalia', 'Sandalia'),
        ('bota', 'Bota'),
    ], string='Tipo de calzado') 
    porcentaje_descuento = fields.Float(string='Porcentaje de descuento (%)') 
    valor_inventario = fields.Float(string='valor_inventario', compute='_compute_valor_inventario', store=True) 
    precio_final = fields.Float(string='Precio final', compute='_compute_precio_final', store=True)
    @api.depends('precio', 'stock')
    def _compute_valor_inventario(self):
        for barrido in self:
            barrido.valor_inventario = barrido.precio * barrido.stock
    @api.depends('precio', 'descuento', 'porcentaje_descuento')
    def _compute_precio_final(self):
        for registro in self:
            if registro.descuento and registro.porcentaje_descuento:
                registro.precio_final = registro.precio * (1 - registro.porcentaje_descuento / 100)
            else:
                registro.precio_final = registro.precio
    