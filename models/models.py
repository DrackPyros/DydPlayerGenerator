# -*- coding: utf-8 -*-
# Marcar modulos como carpeta root
from modulos.odoo import models, fields, api
import random

class Generator(models.Model):
     _name = 'dy_d.generator'
#     _description = 'dy_d.dy_d'

     clases = [
          "Bárbaro",
          "Bardo",
          "Clérigo",
          "Druida",
          "Explorador",
          "Guerrero",
          "Hechicero",
          "Mago",
          "Monje",
          "Paladín",
          "Pícaro"
     ]
     razas = ["Humano", "Elfo", "Enano", "Semielfo", "Semiorco", "Gnomo", "Mediano"]
     atributos = ["Fuerza", "Destreza", "Constitución", "Inteligencia", "Sabiduria", "Carisma"]

     rasgos = {
          atributos[0]: fields.Integer(string='Fuerza', required=True),
          atributos[1]: fields.Integer(string='Destreza', required=True),
          atributos[2]: fields.Integer(string='Constitucion', required=True),
          atributos[3]: fields.Integer(string='Inteligencia', required=True),
          atributos[4]: fields.Integer(string='Sabiduria', required=True),
          atributos[5]: fields.Integer(string='Carisma', required=True),

          "pg": fields.Integer(string='Puntos de golpe', required=True),
          "ca": fields.Integer(string='Clase de armadura', required=True),

          "nombre": fields.Char(string='Nombre de personaje', required=True),
          "jugador": fields.Char(string='Nombre de jugador', required=True),
          "clase": fields.Char(string='Clase', required=True),
          "nivel": fields.Integer(string='Nivel', required=True),
          "raza": fields.Char(string='Raza', required=True),
          "alineamiento": fields.Char(string='Alineamiento', required=True),

          "deidad": fields.Char(string='Deidad'),
          "tamano": fields.Char(string='Tamanyo'),
          "edad": fields.Integer(string='Edad'),
          "sexo": fields.Char(string='Sexo'),
          "altura": fields.Integer(string='Altura (cm)'),
          "peso": fields.Float(string='Peso'),
          "ojos": fields.Char(string='Color de ojos'),
          "cabello": fields.Char(string='Color del cabello'),
          "piel": fields.Char(string='Tono de piel')
     }


     vecestotales = 7
     veces = 4
     dados = 6


     # quitando el dado más bajo en cada tirada. e suman los dados de cada tirada, se elimina la tirada más baja y se reparten pseudo-aleatoriamente, teniendo más probabilidad de asignar la tirada más alta al atributo principal del personaje

     bufos = {
          razas[0]: [0, 0, 0, 0, 0, 0],
          razas[1]: [0, 2, -2, 0, 0, 0],
          razas[2]: [0, 0, 2, 0, 0, -2],
          razas[3]: [0, 0, 0, 0, 0, 0],
          razas[4]: [2, 0, 0, -2, 0, -2],
          razas[5]: [-2, 0, 2, 0, 0, 0],
          razas[6]: [-2, 2, 0, 0, 0, 0]
     }
     sobrenombresRazas = {
          razas[0]:
               [
                    "el hijo del herrero",
                    "el hijo del posadero",
                    "el huérfano",
                    "el vagabundo",
                    "el extranjero"
               ],
          razas[1]:
               [
                    "orejas picudas",
                    "el estirado",
                    "el silvano",
                    "el eterno",
                    "de las montañas nubladas"
               ],
          razas[2]:
               [
                    "de las montañas azules",
                    "el minero",
                    "barba roja",
                    "hijo de la montaña",
                    "el bajo"
               ],
          razas[3]:
               [
                    "el barbudo",
                    "el bastardo",
                    "de las nieves",
                    "sin tierra",
                    "el sintecho"
               ],
          razas[4]:
               [
                    "Machacacráneos",
                    "Hachachunga",
                    "Puñohierro",
                    "el orco",
                    "el paria de Mordor"
               ],
          razas[5]:
               [
                    "el loco",
                    "Gnometoques",
                    "el pequeño",
                    "el hijo del joyero",
                    "Kabum"
               ],
          razas[6]:
               [
                    "el medio-hombre",
                    "el Hobbit",
                    "de la Comarca",
                    "el fumador en pipa",
                    "el hijo del molinero"
               ]
     }
     sobrenombresAtributomayor = {
          atributos[0]:
               [
                    "el fuerte",
                    "el herrero",
                    "el bocadillo de nudillos"
               ],
          atributos[1]:
               [
                    "el ágil",
                    "el rápido",
                    "el ojo",
                    "del halcón",
               ],
          atributos[2]:
               [
                    "el gordo",
                    "la roca",
                    "la piedra del molino",
               ],
          atributos[3]:
               [
                    "el listo",
                    "el inteligente",
                    "Fistandantilus",
               ],
          atributos[4]:
               [
                    "el sabio",
                    "el vividor",
                    "el conocedor de secretos",
               ],
          atributos[5]:
               [
                    "el guapo",
                    "el imponente",
                    "pico de oro"
               ]
     }
     sobrenombresAtributomenor = {
          atributos[0]:
               [
                    "el flojo",
                    "caricias",
                    "dedos de papel"
               ],
          atributos[1]:
               [
                    "el torpe",
                    "el lento",
                    "manos de mantequilla"
               ],
          atributos[2]:
               [
                    "el casi-inconsciente",
                    "el fofo",
                    "el flan"
               ],
          atributos[3]:
               [
                    "el tonto",
                    "el incoherente",
                    "el corto de miras"
               ],
          atributos[4]:
               [
                    "el ignorante",
                    "el perdido",
                    "no-sabe-ni-contesta"
               ],
          atributos[5]:
               [
                    "el feo",
                    "cara-de-pez",
                    "el difícil de mirar"
               ]
     }


     def tirarDados(self, total, times, dados):
          final = []
          for i in range(total):
               nums = []
               for j in times:
                    nums.append(random.randint(0, dados)+1)
               comparardados = dados
               excluir = 0
               for aux in dados: #sacar el menor
                    if nums[aux] < comparardados:
                         excluir = aux
                         comparardados = nums[aux]
               resultado = 0
               for j in dados:
                    if not j == excluir:
                         resultado += nums[j]
               final.append(resultado)

          comparardados = final[0]
          excluir = 0
          resultado = 0
          """
          for aux in final:  # sacar el menor
               if final[aux] < comparardados:
                    excluir = aux
                    comparardados = final[aux]

          for j in final:
               if not j == excluir:
                    resultado = final[j]
          """


     def calcularModificador(self, atributo):
          atributo = (atributo - 10) // 2
          return atributo

     # def sobrenombre(self):
          # Dependiendo de la clase tendrán 5 sobrenombres posibles.
          # Dependiendo de la raza tendrán 5 sobrenombres posibles.
          # Si tienen algún atributo mayor o igual a 18 tendrán 3 sobrenombres por atributo.
          # Si tienen algún atributo menor o igual a 5 tendrán 3 sobrenombres por atributo.
     
     
     
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
