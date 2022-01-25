# -*- coding: utf-8 -*-
# Marcar modulos como carpeta root
from modulos.odoo import models, fields, api


class Generator(models.Model):
     _name = 'dy_d.generator'
#     _description = 'dy_d.dy_d'

     fue = fields.Integer(string='Fuerza', required=True)
     des = fields.Integer(string='Destreza', required=True)
     con = fields.Integer(string='Constitucion', required=True)
     int = fields.Integer(string='Inteligencia', required=True)
     sab = fields.Integer(string='Sabiduria', required=True)
     car = fields.Integer(string='Carisma', required=True)

     pg = fields.Integer(string='Puntos de golpe', required=True)
     ca = fields.Integer(string='Clase de armadura', required=True)

     nombre = fields.Char(string='Nombre de personaje', required=True)
     jugador = fields.Char(string='Nombre de jugador', required=True)
     clase = fields.Char(string='Clase', required=True)
     nivel = fields.Integer(string='Nivel', required=True)
     raza = fields.Char(string='Raza', required=True)
     alineamiento = fields.Char(string='Alineamiento', required=True)

     deidad = fields.Char(string='Deidad')
     tamano = fields.Char(string='Tamanyo')
     edad = fields.Integer(string='Edad')
     sexo = fields.Char(string='Sexo')
     altura = fields.Integer(string='Altura (cm)')
     peso = fields.Float(string='Peso')
     ojos = fields.Char(string='Color de ojos')
     cabello = fields.Char(string='Color del cabello')
     piel = fields.Char(string='Tono de piel')

#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
