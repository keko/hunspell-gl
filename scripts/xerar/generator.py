# -*- coding:utf-8 -*-

from __future__ import print_function

import codecs, os, sys

import common


def createFoldersIfNeeded(path):
    try:
        os.makedirs(path)
    except:
        pass


def output(text):
    print(text, end="")
    sys.stdout.flush()


def writeToResource(content, resource):
    targetPath = os.path.join(common.getModulesSourcePath(), resource)
    createFoldersIfNeeded(os.path.dirname(targetPath))
    with codecs.open(targetPath, u"w", u"utf-8") as fileObject:
        fileObject.write(content)


class Generator(object):

    def generateFileContent(self):
        raise Exception("Abstract method")


    def run(self):
        writeToResource(self.generateFileContent(), self.resource)


tupleOfWordsToIgnore = (
    # Nexos comúns.
    u"A", u"As", u"O", u"Os",
    u"Á", u"Ás", u"Ao", u"Aos", u"Ó", u"Ós",
    u"Da", u"Das", u"De", u"Do", u"Dos",
    u"E",
    u"En", u"Na", u"Nas", u"No", u"Nos",
    u"Entre",
    u"Para",
    u"Pola", u"Polas", u"Polo", u"Polos", u"Por",
    u"Tras",
    u"Un", u"Unha", u"Unhas", "Uns",

    # Outros termos comúns correctos en galego.
    u"Abadía", u"Abadías",
    u"Abaixo",
    u"Abril",
    u"Acción", u"Accións",
    u"Agosto",
    u"Agrupación",
    u"Aldea", u"Aldeas",
    u"Alianza", u"Alianzas",
    u"Alta", u"Altas", u"Alto", u"Altos",
    u"Alternativa", "Alternativas", u"Alternativo", u"Alternativos",
    u"Alzamento", u"Alzamentos",
    u"Ano", u"Anos",
    u"Arquipélago", u"Arquipélagos",
    u"Arrecife", u"Arrecifes",
    u"Arriba",
    u"Arroio", u"Arroios",
    u"Antiga", u"Antigas", u"Antigo", u"Antigos",
    u"Asasinato", u"Asasinatos",
    u"Asociación", u"Asociacións",
    u"Asunto", u"Asuntos",
    u"Ataque", u"Ataques",
    u"Atentado", u"Atentados",
    u"Atol", u"Atois",
    u"Australiana", u"Australianas", u"Australiano", u"Australianos",
    u"Autónoma", u"Autónomas", u"Autónomo", u"Autónomos",
    u"Axencia", u"Axencias",
    u"Baía", u"Baías",
    u"Baixa", u"Baixas", u"Baixo", u"Baixos",
    u"Baldaquino", u"Baldaquinos",
    u"Baloncesto",
    u"Balonmán",
    u"Barrio", u"Barrios",
    u"Basílica", u"Basílicas",
    u"Batalla", u"Batallas",
    u"Bloque", u"Bloques",
    u"Branca", u"Brancas", u"Branco", u"Brancos",
    u"Británica", u"Británicas", u"Británico", u"Británicos",
    u"Beira", u"Beiras",
    u"Cabo",
    u"Camiño", u"Camiños",
    u"Campo", u"Campos",
    u"Candidatura", u"Candidaturas",
    u"Capela", u"Capelas",
    u"Casa", u"Casas",
    u"Castelo", u"Castelos",
    u"Castilla",
    u"Castiñeiro", u"Castiñeiros",
    u"Castro", u"Castros",
    u"Catedral", u"Catedrais",
    u"Católica", u"Católicas", u"Católico", u"Católicos",
    u"Central", u"Centrais",
    u"Centro", u"Centros",
    u"Cidade", u"Cidades",
    u"Cima", u"Cimas",
    u"Civilización", u"Civilizacións",
    u"Colexiata", u"Colexiatas",
    u"Colonia", u"Colonias",
    u"Comarca", u"Comarcas",
    u"Comercial", u"Comerciais",
    u"Comunista", u"Comunistas",
    u"Concello", u"Concellos",
    u"Condado", u"Condados",
    u"Confederación", u"Confederacións",
    u"Continental", u"Continentais", # «Portugal continental».
    u"Continente", u"Continentes",
    u"Convento", u"Conventos",
    u"Coroa", u"Coroas",
    u"Costa", u"Costas",
    u"Cova", u"Covas",
    u"Cruceiro", u"Cruceiros",
    u"Cruz", u"Cruces",
    u"Decembro",
    u"Demócrata", u"Demócratas",
    u"Democrática", u"Democráticas", u"Democrático", u"Democráticos",
    u"Delta", u"Deltas",
    u"Departamento", u"Departamentos",
    u"Deserto", u"Desertos",
    u"Día", u"Días",
    u"Distrito", u"Distritos",
    u"Ducado", u"Ducados",
    u"Enseada", u"Enseadas",
    u"Era", u"Eras",
    u"Ermida", u"Ermidas",
    u"Española", u"Españolas", u"Español", u"Españois",
    u"Estado", u"Estados",
    u"Estreito", u"Estreitos",
    u"Estrela", u"Estrelas",
    u"Europea", u"Europeas", u"Europeo", u"Europeos",
    u"Exterior", u"Exteriores",
    u"Fachada", u"Fachadas",
    u"Faro", u"Faros",
    u"Febreiro",
    u"Federación", u"Federacións",
    u"Federada", u"Federadas", u"Federado", u"Federados",
    u"Federal", u"Federais",
    u"Feira", u"Feiras",
    u"Fonte", u"Fontes",
    u"Fórmula", u"Fórmulas",
    u"Fútbol",
    u"Galega", u"Galegas", u"Galego", u"Galegos",
    u"Galicia", u"Galiza",
    u"Golfo", u"Golfos",
    u"Gran", u"Grande", u"Grandes",
    u"Idade", u"Idades",
    u"Igrexa", u"Igrexas",
    u"Illa", u"Illas",
    u"Illote", u"Illotes",
    u"Imperio", u"Imperios",
    u"Incidente", u"Incidentes",
    u"Índice", u"Índices",
    u"Insua", u"Insuas",
    u"Intelixencia", u"Intelixencias",
    u"Interior", u"Interiores",
    u"Interna", u"Internas", u"Interno", u"Internos",
    u"Internacional", u"Internacionais",
    u"Islámica", u"Islámicas", u"Islámico", u"Islámicos",
    u"Leste",
    u"Liberación", u"Liberacións",
    u"Liberal", u"Liberais",
    u"Libre", u"Libres",
    u"Liga", u"Ligas",
    u"Litoral", u"Litorais",
    u"Lombo", u"Lombos",
    u"Lugar", u"Lugares",
    u"Madeira", u"Madeiras",
    u"Maio",
    u"Maior", u"Maiores",
    u"Mar", u"Mares",
    u"Marzo",
    u"Masacre", u"Masacres",
    u"Matanza", u"Matanzas",
    u"Menor", u"Menores",
    u"Meridional", u"Meridionais",
    u"Mes", u"Meses",
    u"Metro", u"Metros",
    u"Monte", u"Montes",
    u"Mosteiro", u"Mosteiros",
    u"Mundial", u"Mundiais",
    u"Nacional", u"Nacionais",
    u"Nacionalista", u"Nacionalistas",
    u"Nosa", u"Nosas", u"Noso", u"Nosos",
    u"Nova", u"Novas", u"Novo", u"Novos",
    u"Novembro",
    u"Norte",
    u"Occidental", u"Occidentais",
    u"Océano", u"Océanos",
    u"Oeste",
    u"Oliveira", u"Oliveiras",
    u"Operación", u"Operacións",
    u"Oriental", u"Orientais",
    u"Outeiro", u"Outeiros",
    u"Outubro",
    u"Pacto", u"Pactos",
    u"País", u"Países",
    u"Parada", u"Paradas",
    u"Partido", u"Partidos",
    u"Pazo", u"Pazos",
    u"Pena", u"Penas",
    u"Península", u"Penínsulas",
    u"Pequena", u"Pequenas", u"Pequeno", u"Pequenos",
    u"Perla", u"Perlas",
    u"Pobo", u"Pobos",
    u"Ponte", u"Pontes",
    u"Popular", u"Populares",
    u"Porta", u"Portas",
    u"Pórtico", u"Pórticos",
    u"Porto", u"Portos",
    u"Prado", u"Prados",
    u"Praia", u"Praias",
    u"Praza", u"Prazas",
    u"Princesa", u"Princesas", u"Príncipe", u"Príncipes",
    u"Principado", u"Principados",
    u"Progresista", u"Progresistas",
    u"Protesta", u"Protestas",
    u"Provincia", u"Provincias",
    u"Radical", u"Radicais",
    u"Raíña", u"Raíñas", u"Rei", u"Reis",
    u"Real", u"Reais",
    u"Rebelión", u"Rebelións",
    u"Refuxio", u"Refuxios",
    u"Regato", u"Regatos",
    u"Rego", u"Regos",
    u"Regueiro", u"Regueiros",
    u"Reino", u"Reinos",
    u"Reitoral", u"Reitorais",
    u"Remedio", u"Remedios",
    u"República", u"Repúblicas",
    u"Republicana", u"Republicanas", u"Republicano", u"Republicanos",
    u"Rexión", u"Rexións",
    u"Ribeira", u"Ribeiras",
    u"Río", u"Ríos",
    u"Rúa", u"Rúas",
    u"Ruína", u"Ruínas",
    u"San", u"Santa", u"Santas", u"Santo", u"Santos",
    u"Santuario", u"Santuarios",
    u"Secreta", u"Secretas", u"Secreto", u"Secretos",
    u"Secuestro", u"Secuestros",
    u"Señor", u"Señora", u"Señoras", u"Señores",
    u"Señorío", u"Señoríos",
    u"Serra", u"Serras",
    u"Servizo", u"Servizos",
    u"Setembro",
    u"Silva", u"Silvas",
    u"Socialista", u"Socialistas",
    u"Sol", u"Soles",
    u"Souto", u"Soutos",
    u"Soviética", u"Soviéticas", u"Soviético", u"Soviéticos",
    u"Subrexión", u"Subrexións",
    u"Sur",
    u"Templo", u"Templos",
    u"Tiroteo", u"Tiroteos",
    u"Torre", u"Torres",
    u"Tradicionalista", u"Tradicionalistas",
    u"Unida", u"Unidas", u"Unido", u"Unidos",
    u"Unión", u"Unións",
    u"Val", u"Vales",
    u"Veiga", u"Veigas",
    u"Vella", u"Vellas", u"Vello", u"Vellos",
    u"Verde", u"Verdes",
    u"Vila", u"Vilas",
    u"Vilar", u"Vilares",
    u"Virxe", u"Virxes",
    u"Xadrez",
    u"Xaneiro",
    u"Xenocidio", u"Xenocidios",
    u"Xuño",
    u"Xullo",

    # Ordinais. Por exemplo, «Cuarta República».
    u"Primeira", u"Primeiras", u"Primeiro", u"Primeiros",
    u"Segunda", u"Segundas", u"Segundo", u"Segundos",
    u"Terceira", u"Terceiras", u"Terceiro", u"Terceiros",
    u"Cuarta", u"Cuartas", u"Cuarto", u"Cuartos",
    u"Quinta", u"Quintas", u"Quinto", u"Quintos",
    u"Sexta", u"Sextas", u"Sexto", u"Sextos",
    u"Sétima", u"Sétimas", u"Sétimo", u"Sétimos",
    u"Oitava", u"Oitavas", u"Oitavo", u"Oitavos",
    u"Novena", u"Novenas", u"Noveno", u"Novenos",
    u"Décima", u"Décimas", u"Décimo", u"Décimos",

    # Multiplicadores. Por exemplo: «Cuádrupla Alianza».
    u"Dupla", u"Duplas", u"Cuádruplo", u"Cuádruplos",
    u"Tripla", u"Triplas", u"Triplo", u"Triplos",
    u"Cuádrupla", u"Cuádruplas", u"Cuádruplo", u"Cuádruplos",
    u"Quíntupla", u"Quíntuplas", u"Quíntuplo", u"Quíntuplos",
    u"Séxtupla", u"Séxtuplas", u"Séxtuplo", u"Séxtuplos",
    u"Séptupla", u"Séptuplas", u"Séptuplo", u"Séptuplos",
)
wordsToIgnore = set()
for word in tupleOfWordsToIgnore:
    wordsToIgnore.add(word)
    wordsToIgnore.add(word.lower())