# -*- coding: utf-8 -*-
# Marcar modulos como carpeta root
from odoo import models, fields, api
import random
import json

from odoo.modules import get_module_resource


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
    sex = ["Masculino", "Femenino"]
    tamanyo = ["Pequeño", "Medio", "Grande"]
    alineamiento = [
        "LB (Legal-Bueno)",
        "NB (Neutral-Bueno)",
        "CB (Caotico-Bueno)",
        "LN (Legal-Neutral)",
        "N (Neutral)",
        "CN (Caotico-Neutral)",
        "LM (Legal-Maligno)",
        "NM (Neutral-Maligno)",
        "CM (Caotico-Maligno)"
    ]
    afinidad = {
        clases[0]: atributos[0],
        clases[1]: atributos[5],
        clases[2]: atributos[4],
        clases[3]: atributos[4],
        clases[4]: atributos[1],
        clases[5]: atributos[0],
        clases[6]: atributos[5],
        clases[7]: atributos[3],
        clases[8]: atributos[4],
        clases[9]: atributos[5],
        clases[10]: atributos[2],
    }
    salvacion = {
        clases[0]: [12, 1, 2, 0, 0],
        clases[1]: [6, 0, 0, 2, 2],
        clases[2]: [8, 0, 2, 0, 2],
        clases[3]: [8, 0, 2, 0, 2],
        clases[4]: [8, 1, 2, 2, 0],
        clases[5]: [10, 1, 2, 0, 0],
        clases[6]: [4, 0, 0, 0, 2],
        clases[7]: [4, 0, 0, 0, 2],
        clases[8]: [8, 0, 2, 2, 2],
        clases[9]: [10, 1, 2, 0, 0],
        clases[10]: [6, 0, 0, 2, 0],
    }
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
                "el de las montañas nubladas"
            ],
        razas[2]:
            [
                "el de las montañas azules",
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
                "el ojo del halcón",
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
    sobrenombresRazasFem = {
        razas[0]:
            [
                "la hija del herrero",
                "la hija del posadero",
                "la huérfana",
                "la vagabunda",
                "la extranjera"
            ],
        razas[1]:
            [
                "orejas picudas",
                "la estirada",
                "la silvana",
                "la eterna",
                "la de las montañas nubladas"
            ],
        razas[2]:
            [
                "la de las montañas azules",
                "la minera",
                "hija de la montaña",
                "Pulga"
            ],
        razas[3]:
            [
                "la bastarda",
                "de las nieves",
                "sin tierra",
                "la sintecho"
            ],
        razas[4]:
            [
                "Machacacráneos",
                "Hachachunga",
                "Puñohierro",
                "la orco",
                "la paria de Mordor"
            ],
        razas[5]:
            [
                "la loca",
                "Gnometoques",
                "la pequeña",
                "la hija del joyero",
                "Kabum"
            ],
        razas[6]:
            [
                "la medio-hombre",
                "la Hobbit",
                "de la Comarca",
                "la fumadora en pipa",
                "la hija del molinero"
            ]
    }
    sobrenombresAtributomayorFem = {
        atributos[0]:
            [
                "la fuerte",
                "la herrera",
                "la bocadillo de nudillos"
            ],
        atributos[1]:
            [
                "la ágil",
                "la rápida",
                "la ojo de halcón",
            ],
        atributos[2]:
            [
                "la gorda",
                "la roca",
                "la piedra del molino",
            ],
        atributos[3]:
            [
                "la lista",
                "la inteligente",
                "Fistandantilus",
            ],
        atributos[4]:
            [
                "la sabia",
                "la vividora",
                "la conocedora de secretos",
            ],
        atributos[5]:
            [
                "la guapa",
                "la imponente",
                "pico de oro"
            ]
    }
    sobrenombresAtributomenorFem = {
        atributos[0]:
            [
                "la floja",
                "caricias",
                "dedos de papel"
            ],
        atributos[1]:
            [
                "la torpe",
                "la lenta",
                "manos de mantequilla"
            ],
        atributos[2]:
            [
                "la casi-inconsciente",
                "la fofa",
                "la flan"
            ],
        atributos[3]:
            [
                "la tonta",
                "la incoherente",
                "la corta de miras"
            ],
        atributos[4]:
            [
                "la ignorante",
                "la sin rumbo",
                "no-sabe-ni-contesta"
            ],
        atributos[5]:
            [
                "la fea",
                "cara-de-pez",
                "la difícil de mirar"
            ]
    }

    Raza = fields.Selection(string='Raza',
                            selection=[
                                (razas[0], razas[0]),
                                (razas[1], razas[1]),
                                (razas[2], razas[2]),
                                (razas[3], razas[3]),
                                (razas[4], razas[4]),
                                (razas[5], razas[5]),
                                (razas[6], razas[6])
                            ], required=True, default=razas[0])
    Clase = fields.Selection(string='Clase',
                             selection=[
                                 (clases[0], clases[0]),
                                 (clases[1], clases[1]),
                                 (clases[2], clases[2]),
                                 (clases[3], clases[3]),
                                 (clases[4], clases[4]),
                                 (clases[5], clases[5]),
                                 (clases[6], clases[6]),
                                 (clases[7], clases[7]),
                                 (clases[8], clases[8]),
                                 (clases[9], clases[9]),
                             ], required=True, default=clases[0])

    Jugador = fields.Char(string='Nombre de jugador')
    Fuerza = fields.Integer(string='Fuerza', compute='selectorAtributo', store=True)

    Nombre = fields.Char(string='Nombre de personaje', compute='selectorNombre', store=True)
    Destreza = fields.Integer(string='Destreza', compute='selectorAtributo', store=True)

    Nivel = fields.Integer(string='Nivel', compute='selectorAtributo', store=True)
    Constitucion = fields.Integer(string='Constitucion', compute='selectorAtributo', store=True)

    Alineamiento = fields.Char(string='Alineamiento', compute='selectorEspecial', store=True)
    Inteligencia = fields.Integer(string='Inteligencia', compute='selectorAtributo', store=True)

    PG = fields.Integer(string='Puntos de golpe', compute='selectorModificador', store=True)
    Sabiduria = fields.Integer(string='Sabiduria', compute='selectorAtributo', store=True)

    CA = fields.Integer(string='Clase de armadura', compute='selectorModificador', store=True)
    Carisma = fields.Integer(string='Carisma', compute='selectorAtributo', store=True)

    Tamaño = fields.Char(string='Tamaño', compute='selectorEspecial', store=True)
    Sexo = fields.Char(string='Sexo', compute='selectorEspecial', store=True)

    ModificadorAtaque = fields.Char(string='Modificador de Ataque', compute='selectorModificador', store=True)
    SalvacionFortaleza = fields.Char(string='Salvacion de Fortaleza', compute='selectorModificador', store=True)
    SalvacionReflejos = fields.Char(string='Salvacion de Reflejos', compute='selectorModificador', store=True)
    SalvacionVolutad = fields.Char(string='Salvacion de Volutad', compute='selectorModificador', store=True)

    """ 
    Deidad = fields.Char(string='Deidad')
    Edad = fields.Integer(string='Edad')
    Altura = fields.Integer(string='Altura (cm)')
    Peso = fields.Float(string='Peso')
    Ojos = fields.Char(string='Color de ojos')
    Cabello = fields.Char(string='Color del cabello')
    Piel = fields.Char(string='Tono de piel')
    """
    claseOld = ""
    razaOld = ""

    def tirarDados(self):
        veces = 7
        ndados = 4
        tdados = 6
        tiradasFinales = []
        for i in range(veces):
            nums = []
            for j in range(ndados):  # generar tiradas
                nums.append(random.randint(0, tdados) + 1)  # 1 a 6

            # sacar el menor
            comparardados = tdados
            excluir = 0
            for aux in range(ndados):
                if nums[aux] < comparardados:
                    excluir = aux
                    comparardados = nums[aux]

            # quitar el menor
            resultado = 0
            for l in range(ndados):
                if not l == excluir:
                    resultado += nums[l]

            tiradasFinales.append(resultado)

        excluir = tiradasFinales[0]
        for i in range(len(tiradasFinales)):
            for j in range(len(tiradasFinales)):
                if excluir > tiradasFinales[j]:
                    excluir = tiradasFinales[j]
        tiradasFinales.remove(excluir)
        print(tiradasFinales)
        return tiradasFinales

    def calcularModificador(self, atributo):
        atributo = (atributo - 10) // 2
        return atributo

    def generador(self):
        json_file_path = get_module_resource('dy_d', 'models/', 'nombres.json')
        f = open(json_file_path)
        data = json.load(f)
        nombre = ""
        for persona in self.filtered('Clase'):
            r = persona.Raza
            if r != self.razas[3] and r != self.razas[4]:
                nombre = data["nombres"][r][persona.Sexo][random.randint(0, len(data["nombres"][r][persona.Sexo]) - 1)]
                nombre += " " + data["nombres"][r]["Apellidos"][
                    random.randint(0, len(data["nombres"][r]["Apellidos"]) - 1)]
            else:
                if r == self.razas[3]:
                    r = self.razas[random.randint(0, 1)]
                    nombre = data["nombres"][r][persona.Sexo][
                        random.randint(0, len(data["nombres"][r][persona.Sexo]) - 1)]
                    nombre += " " + data["nombres"][r]["Apellidos"][
                        random.randint(0, len(data["nombres"][r]["Apellidos"]) - 1)]
                else:
                    nombre = data["nombres"][r][persona.Sexo][
                        random.randint(0, len(data["nombres"][r][persona.Sexo]) - 1)]
        return nombre

    @api.depends('Clase', 'Raza')
    def selectorAtributo(self):
        for persona in self.filtered('Clase'):
            # if self.claseOld != persona.Clase and self.razaOld != persona.Raza:
            clasePrueba = persona.Clase
            razaPrueba = persona.Raza
            atributos = self.tirarDados()

            att = {
                self.atributos[0]: 0,
                self.atributos[1]: 0,
                self.atributos[2]: 0,
                self.atributos[3]: 0,
                self.atributos[4]: 0,
                self.atributos[5]: 0
            }
            attMax = self.afinidad[clasePrueba]
            att[attMax] = max(atributos)
            atributos.remove(max(atributos))
            num = 0
            # Ya los generamos aleatoriamente por tanto no es necesario hacer otro random
            for m in att.keys():
                if m != attMax:
                    att[m] = atributos[num]
                    num += 1

            persona.Fuerza = att[self.atributos[0]] + self.bufos[razaPrueba][0]
            persona.Destreza = att[self.atributos[1]] + self.bufos[razaPrueba][1]
            persona.Constitucion = att[self.atributos[2]] + self.bufos[razaPrueba][2]
            persona.Inteligencia = att[self.atributos[3]] + self.bufos[razaPrueba][3]
            persona.Sabiduria = att[self.atributos[4]] + self.bufos[razaPrueba][4]
            persona.Carisma = att[self.atributos[5]] + self.bufos[razaPrueba][5]
            persona.Nivel = 1
            if razaPrueba == self.razas[4] and persona.Inteligencia < 3:
                persona.Inteligencia = 3
            # self.claseOld = persona.Clase
            # self.razaOld = persona.Raza

    @api.depends('Clase', 'Raza')
    def selectorNombre(self):
        for persona in self.filtered('Clase'):
            att = {
                self.atributos[0]: persona.Fuerza,
                self.atributos[1]: persona.Destreza,
                self.atributos[2]: persona.Constitucion,
                self.atributos[3]: persona.Inteligencia,
                self.atributos[4]: persona.Sabiduria,
                self.atributos[5]: persona.Carisma,
            }
            nombre = self.generador()
            if persona.Sexo == self.sex[0]:
                nombrePosible = self.sobrenombresRazas[persona.Raza]
                for i in range(len(att)):
                    if att[self.atributos[i]] >= 18:
                        nombrePosible += self.sobrenombresAtributomayor[self.atributos[i]]
                    if att[self.atributos[i]] <= 5:
                        nombrePosible += self.sobrenombresAtributomenor[self.atributos[i]]
            else:
                nombrePosible = self.sobrenombresRazasFem[persona.Raza]
                for i in range(len(att)):
                    if att[self.atributos[i]] >= 18:
                        nombrePosible += self.sobrenombresAtributomayorFem[self.atributos[i]]
                    if att[self.atributos[i]] <= 5:
                        nombrePosible += self.sobrenombresAtributomenorFem[self.atributos[i]]
            persona.Nombre = nombre + " '" + nombrePosible[random.randint(0, len(nombrePosible)-1)] + "'"

    @api.depends('Clase', 'Raza')
    def selectorEspecial(self):
        for persona in self.filtered('Clase'):
            persona.Sexo = self.sex[random.randint(0, len(self.sex)-1)]
            if persona.Raza == self.razas[2] or persona.Raza == self.razas[5]:
                persona.Tamaño = self.tamanyo[random.randint(0, len(self.tamanyo) - 2)]
            else:
                persona.Tamaño = self.tamanyo[random.randint(0, len(self.tamanyo) - 1)]
            persona.Alineamiento = self.alineamiento[random.randint(0, len(self.alineamiento)-1)]

    @api.depends('Clase', 'Raza')
    def selectorModificador(self):
        for persona in self.filtered('Clase'):
            persona.ModificadorAtaque = "+" + str(self.salvacion[persona.Clase][1])
            persona.SalvacionVolutad = "+" + str(self.calcularModificador(persona.Sabiduria) + self.salvacion[persona.Clase][4])
            persona.SalvacionReflejos = "+" + str(self.calcularModificador(persona.Destreza) + self.salvacion[persona.Clase][3])
            persona.SalvacionFortaleza = "+" + str(self.calcularModificador(persona.Constitucion) + self.salvacion[persona.Clase][2])
            persona.CA = 10
            #persona.PG = self.salvacion[persona.Clase][1] en D&D cuando creas un pj lvl 1 los PG son el valor maximo del dado no hay que calcularlo
            persona.PG = random.randint(1, self.salvacion[persona.Clase][0]-1) + self.calcularModificador(persona.Constitucion)


#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
