# -*- coding:utf-8 -*-

from mediawiki import MediaWikiGenerator  # Dictionary generators.
from mediawiki import EntryGenerator  # Entry generators.
from mediawiki import PageLoader, CategoryBrowser  # Page generators.
from mediawiki import TitleParser, FirstSentenceParser, LineParser  # Page parsers.
from mediawiki import EntryParser  # Page parsers.


# Wikipedia generator.

class WikipediaGenerator(MediaWikiGenerator):

    def __init__(self, languageCode, resource, partOfSpeech, entryGenerators):
        super(WikipediaGenerator, self).__init__(
                siteName=u"wikipedia",
                languageCode=languageCode,
                resource=resource,
                partOfSpeech=partOfSpeech,
                entryGenerators=entryGenerators,
            )




# Language-specific Wikipedia generators.

class GalipediaGenerator(WikipediaGenerator):

    def __init__(self, resource, partOfSpeech, entryGenerators):
        super(GalipediaGenerator, self).__init__(
                "gl",
                resource,
                partOfSpeech,
                entryGenerators=entryGenerators,
            )



class WikipediaEnGenerator(WikipediaGenerator):

    def __init__(self, resource, partOfSpeech, entryGenerators):
        super(WikipediaEnGenerator, self).__init__(
                "en",
                resource,
                partOfSpeech,
                entryGenerators=entryGenerators,
            )


class WikipediaEsGenerator(WikipediaGenerator):

    def __init__(self, resource, partOfSpeech, entryGenerators):
        super(WikipediaEsGenerator, self).__init__(
                "es",
                resource,
                partOfSpeech,
                entryGenerators=entryGenerators,
            )


class WikipediaHuGenerator(WikipediaGenerator):

    def __init__(self, resource, partOfSpeech, entryGenerators):
        super(WikipediaHuGenerator, self).__init__(
                "hu",
                resource,
                partOfSpeech,
                entryGenerators=entryGenerators,
            )


class WikipediaPtGenerator(WikipediaGenerator):

    def __init__(self, resource, partOfSpeech, entryGenerators):
        super(WikipediaPtGenerator, self).__init__(
                "pt",
                resource,
                partOfSpeech,
                entryGenerators=entryGenerators,
            )




# Helpers.

class GalipediaLocalidadesGenerator(GalipediaGenerator):

    def __init__(self, countryName, categoryNames = [u"Cidades de {name}"], pageParser=None):

        parsedCategoryNames = []
        for categoryName in categoryNames:
            parsedCategoryNames.append(categoryName.format(name=countryName))

        pattern = u"(Alcaldes|Arquitectura|Capitais|Comunas|Concellos|Festas?|Imaxes|Igrexa|Galería|Historia|Listas?|Localidades|Lugares|Municipios|Parroquias|Principais cidades) "
        categoryBrowser = CategoryBrowser(
            categoryNames=parsedCategoryNames,
            invalidPagePattern = u"(?i)^(Wikipedia:|{pattern}[a-z])".format(pattern=pattern),
            validCategoryPattern = u"(?i)^(Antig[ao]s )?(Cidades|Comunas|Concellos|Municipios|Parroquias|Vilas) ",
            invalidCategoryPattern = u"(?i){pattern}[a-z]|.+sen imaxes$".format(pattern=pattern),
        )

        entryParser = EntryParser()
        if countryName == u"España":
            entryParser = EntryParser(basqueFilter=True)

        super(GalipediaLocalidadesGenerator, self).__init__(
            resource = u"onomástica/toponimia/localidades/{name}.dic".format(name=countryName.lower().replace(" ", "-")),
            partOfSpeech = u"topónimo",
            entryGenerators=[
                EntryGenerator(
                    pageGenerators=[categoryBrowser,],
                    pageParser=pageParser,
                    entryParser=entryParser,
                )
            ],
        )



class GalipediaRexionsGenerator(GalipediaGenerator):

    def __init__(self, countryName, categoryNames = [u"Rexións de {name}"], pageParser=None):

        parsedCategoryNames = []
        for categoryName in categoryNames:
            parsedCategoryNames.append(categoryName.format(name=countryName))

        categoryPattern = u"Áreas municipais|Comarcas|Condados|Departamentos|Distritos|Divisións|Estados|Partidos xudiciais|Periferias|Provincias|Rexións|Subdivisións|Subrexións"
        categoryBrowser = CategoryBrowser(
            categoryNames=parsedCategoryNames,
            invalidPagePattern = u"^((Batalla|Lista|{}) |Comunidade autónoma)".format(categoryPattern),
            validCategoryPattern = u"^({}) ".format(categoryPattern),
            invalidCategoryPattern = u"^(Capitais|Categorías|Deporte|Gobernos|Nados|Parlamentos|Personalidades|Políticas|Presidentes) ",
        )

        super(GalipediaRexionsGenerator, self).__init__(
            resource = u"onomástica/toponimia/rexións/{name}.dic".format(name=countryName.lower().replace(" ", "-")),
            partOfSpeech = u"topónimo",
            entryGenerators=[
                EntryGenerator(
                    pageGenerators=[categoryBrowser,],
                    pageParser=pageParser,
                )
            ],
        )



class GalipediaNamesGenerator(GalipediaGenerator):

    def __init__(self):

        pageNames = [u"Lista de nomes masculinos en galego", u"Lista de nomes femininos en galego"]
        pageLoader = PageLoader(pageNames=pageNames)

        categoryBrowser = CategoryBrowser(
            categoryNames = [u"Antroponimia",],
            invalidPagePattern = u"^(Antroponimia$|Lista )"
        )

        namePattern = u"^\* *\'\'\' *(\[\[)? *([^]|]+\| *)?(?P<entry>[^]|]+) *(\]\])? *\'\'\'"
        lineParser = LineParser(namePattern, )

        super(GalipediaNamesGenerator, self).__init__(
            resource = u"onomástica/antroponimia/xeral.dic",
            partOfSpeech = u"antropónimo",
            entryGenerators = [
                EntryGenerator(
                    pageGenerators=[pageLoader,],
                    pageParser=lineParser,
                ),
                EntryGenerator(
                    pageGenerators=[categoryBrowser,],
                    pageParser=FirstSentenceParser(),
                ),
            ]
        )



def loadGeneratorList():

    generators = []


    # Galipedia

    generators.append(GalipediaGenerator(
        resource = u"onomástica/antroponimia/países/españa.dic",
        partOfSpeech = u"antropónimo",
        entryGenerators=[
            EntryGenerator(
                pageGenerators = [
                    CategoryBrowser(
                        categoryNames = [u"Finados en 1975", u"Reis de Galicia"],
                        invalidPagePattern = u"^(Dinastía|Lista d)",
                        validCategoryPattern = u"^(Reis|Dinastía)",
                        invalidCategoryPattern = u"^(Lista d)",
                    ),
                ],
                pageParser = FirstSentenceParser(),
            )
        ],
    ))

    pattern = u"(Arquitectura relixiosa|Basílicas|Capelas|Catedrais|Colexiatas|Conventos|Ermidas|Igrexas|Mosteiros|Mosteiros e conventos|Pórticos|Santuarios|Templos) "
    generators.append(GalipediaGenerator(
        resource = u"onomástica/arquitectura/relixión.dic",
        partOfSpeech = u"nome propio",
        entryGenerators=[
            EntryGenerator(
                pageGenerators = [
                    CategoryBrowser(
                        categoryNames = [u"Arquitectura relixiosa por países"],
                        invalidPagePattern = u"^({pattern}|Galería de imaxes)".format(pattern=pattern),
                        validCategoryPattern = u"^{pattern}".format(pattern=pattern),
                        invalidCategoryPattern = u"^(Imaxes) ",
                    ),
                ],
            )
        ],
    ))

    generators.append(GalipediaGenerator(
        resource = u"onomástica/arte/escultura/relixión.dic",
        partOfSpeech = u"nome propio",
        entryGenerators=[
            EntryGenerator(
                pageGenerators = [
                    CategoryBrowser(
                        categoryNames = [u"Escultura relixiosa de Galicia"],
                        validCategoryPattern = u"^(Baldaquinos d|Cruceiros d)",
                        invalidCategoryPattern = u"^Imaxes d",
                    ),
                ],
            )
        ],
    ))

    generators.append(GalipediaGenerator(
        resource = u"onomástica/astronomía/planetas.dic",
        partOfSpeech = u"nome propio",
        entryGenerators=[
            EntryGenerator(
                pageGenerators = [
                    CategoryBrowser(
                        categoryNames = [u"Planetas"],
                        invalidPagePattern = u"^(Lista d|Planeta anano$|Planeta($| ))",
                        validCategoryPattern = u"^(Candidatos a planeta|Planetas |Plutoides$)",
                        invalidCategoryPattern = u"^Sistemas planetarios$",
                    ),
                ],
            )
        ],
    ))

    generators.append(GalipediaGenerator(
        resource = u"onomástica/historia/civilizacións.dic",
        partOfSpeech = u"nome propio",
        entryGenerators=[
            EntryGenerator(
                pageGenerators = [
                    CategoryBrowser(
                        categoryNames = [u"Civilizacións"],
                        invalidPagePattern = u"^((Lista|Pobos) |(Civilización|Cultura dos Campos de Urnas|Sala do hidromel)$)",
                        validCategoryPattern = u"^(Pobos|Reinos) ",
                        invalidCategoryPattern = u"^(Arquitectura|Xeografía) ",
                    ),
                ],
                pageParser=FirstSentenceParser(),
            )
        ],
    ))

    generators.append(GalipediaGenerator(
        resource = u"onomástica/toponimia/accidentes/baías.dic",
        partOfSpeech = u"topónimo",
        entryGenerators=[
            EntryGenerator(
                pageGenerators = [
                    CategoryBrowser(
                        categoryNames = [u"Golfos e baías"],
                        invalidPagePattern = u"^Baía$",
                        validCategoryPattern = u"^Golfos e baías d",
                    ),
                ],
                pageParser=FirstSentenceParser(),
            )
        ],
    ))

    generators.append(GalipediaGenerator(
        resource = u"onomástica/toponimia/accidentes/desertos.dic",
        partOfSpeech = u"topónimo",
        entryGenerators=[
            EntryGenerator(
                pageGenerators = [
                    CategoryBrowser(
                        categoryNames = [u"Desertos"],
                        invalidPagePattern = u"^(Desertos d|(Deserto|Serir)$)",
                        validCategoryPattern = u"^Desertos d",
                    ),
                ],
                pageParser=FirstSentenceParser(),
            )
        ],
    ))

    generators.append(GalipediaGenerator(
        resource = u"onomástica/toponimia/accidentes/illas.dic",
        partOfSpeech = u"topónimo",
        entryGenerators=[
            EntryGenerator(
                pageGenerators = [
                    CategoryBrowser(
                        categoryNames = [
                            u"Illas e arquipélagos",
                            u"Arquipélagos",
                            u"Atois",
                            u"Illas",
                            u"Illas das Illas Baleares",
                            u"Illas de Asturias",
                            u"Illas de Canarias",
                            u"Illas de Galicia",
                            u"Illas de Asia",
                            u"Illas de Marrocos",
                            u"Illas galegas",
                            u"Illas dos Grandes Lagos"
                        ],
                        invalidPagePattern = u"^((Batalla|Lista) |Illote Motu|Illas de Galicia)",
                        invalidCategoryPattern = u"^(Arquipélagos|Illas|Illas da baía d.*|Illas de Alasca|Illas de Asia|Illas de Galicia|Illas de Marrocos|Illas do arquipélago d.*|Illas do Xapón|Illas dos Grandes Lagos|Illas e arquipélagos .*|Illas galegas|Illas por mar|Illas por países|Illas por continente)$",
                        categoryOfCategoriesNames = [u"Illas e arquipélagos por localización‎", u"Illas por continente", u"Illas por mar", u"Illas por países"],
                    ),
                ],
                pageParser=FirstSentenceParser(),
            )
        ],
    ))

    generators.append(GalipediaGenerator(
        resource = u"onomástica/toponimia/accidentes/mares.dic",
        partOfSpeech = u"topónimo",
        entryGenerators=[
            EntryGenerator(
                pageGenerators = [
                    CategoryBrowser(
                        categoryNames = [u"Mares e océanos"],
                        invalidPagePattern = u"^(Instituto|(Mar|Océano mundial|Zona económica exclusiva)$)",
                        validCategoryPattern = u"^(Mares|Océanos)",
                        invalidCategoryPattern = u"^(Cidades|Estreitos) ",
                    ),
                ],
                pageParser=FirstSentenceParser(),
            )
        ],
    ))

    generators.append(GalipediaGenerator(
        resource = u"onomástica/toponimia/accidentes/montañas.dic",
        partOfSpeech = u"topónimo",
        entryGenerators=[
            EntryGenerator(
                pageGenerators = [
                    CategoryBrowser(
                        categoryNames = [u"Montañas"],
                        validCategoryPattern = u"^(Cordilleiras|Montañas|Montes)",
                    ),
                ],
            )
        ],
    ))

    generators.append(GalipediaGenerator(
        resource = u"onomástica/toponimia/accidentes/penínsulas.dic",
        partOfSpeech = u"topónimo",
        entryGenerators=[
            EntryGenerator(
                pageGenerators = [
                    CategoryBrowser(
                        categoryNames = [u"Penínsulas"],
                        validCategoryPattern = u"^Penínsulas (a|d|por |n)",
                    ),
                ],
                pageParser=FirstSentenceParser(),
            )
        ],
    ))

    pattern = u"(Praias) "
    generators.append(GalipediaGenerator(
        resource = u"onomástica/toponimia/accidentes/praias.dic",
        partOfSpeech = u"topónimo",
        entryGenerators=[
            EntryGenerator(
                pageGenerators = [
                    CategoryBrowser(
                        categoryNames = [u"Praias"],
                        invalidPagePattern = u"^({pattern}|Bandeira Azul$|Galería de imaxes|Praia$|Praia nudista$)".format(pattern=pattern),
                        validCategoryPattern = u"^{pattern}".format(pattern=pattern),
                        invalidCategoryPattern = u"^(Imaxes) ",
                    ),
                ],
            )
        ],
    ))

    pattern = u"(Rexións) "
    generators.append(GalipediaGenerator(
        resource = u"onomástica/toponimia/accidentes/rexións.dic",
        partOfSpeech = u"topónimo",
        entryGenerators=[
            EntryGenerator(
                pageGenerators = [
                    PageLoader(
                        [
                            u"Cisxordania",
                            u"Cochinchina",
                            u"Dalmacia",
                            u"Faixa de Gaza",
                        ]
                    ),
                    CategoryBrowser(
                        categoryNames = [u"Rexións de Europa"],
                        invalidPagePattern = u"^({pattern}|Galería de imaxes)".format(pattern=pattern),
                        validCategoryPattern = u"^{pattern}".format(pattern=pattern),
                        invalidCategoryPattern = u"^(Imaxes) ",
                    ),
                ],
                pageParser=FirstSentenceParser(),
            )
        ],
    ))

    pattern = u"(Afluentes|Regatos|Ríos) "
    generators.append(GalipediaGenerator(
        resource = u"onomástica/toponimia/accidentes/ríos.dic",
        partOfSpeech = u"topónimo",
        entryGenerators=[
            EntryGenerator(
                pageGenerators = [
                    CategoryBrowser(
                        invalidPagePattern = u"^({pattern}|(Galería de imaxes|Hidrografía|Lista) |(Caneiro \(muíño\)|Pasadoiro|Pontella \(pasaxe\))$)".format(pattern=pattern),
                        validCategoryPattern = u"^{pattern}".format(pattern=pattern),
                        invalidCategoryPattern = u"^({pattern}|Imaxes)".format(pattern=pattern),
                        categoryOfCategoriesNames = [u"Ríos"],
                    ),
                ],
                pageParser=FirstSentenceParser(),
            )
        ],
    ))

    generators.append(GalipediaLocalidadesGenerator(u"Desaparecidas", [u"Cidades desaparecidas"])) # Localidades desaparecidas.
    generators.append(GalipediaLocalidadesGenerator(u"Alemaña", pageParser=FirstSentenceParser()))
    generators.append(GalipediaLocalidadesGenerator(u"Alxeria"))
    generators.append(GalipediaLocalidadesGenerator(u"Austria", pageParser=FirstSentenceParser()))
    generators.append(GalipediaLocalidadesGenerator(u"Bangladesh"))
    generators.append(GalipediaLocalidadesGenerator(u"Barbados"))
    generators.append(GalipediaLocalidadesGenerator(u"Bélxica", pageParser=FirstSentenceParser()))
    generators.append(GalipediaLocalidadesGenerator(u"Bolivia"))
    generators.append(GalipediaLocalidadesGenerator(u"Brasil", [u"Cidades do {name}"]))
    generators.append(GalipediaLocalidadesGenerator(u"Burkina Faso", pageParser=FirstSentenceParser()))
    generators.append(GalipediaLocalidadesGenerator(u"Cambodja", pageParser=FirstSentenceParser()))
    generators.append(GalipediaLocalidadesGenerator(u"Canadá", [u"Cidades do {name}"], pageParser=FirstSentenceParser()))
    generators.append(GalipediaLocalidadesGenerator(u"China", [u"Cidades da {name}"], pageParser=FirstSentenceParser()))
    generators.append(GalipediaLocalidadesGenerator(u"Colombia", [u"Cidades de {name}", u"Concellos de {name}", u"Correxementos de {name}"]))
    generators.append(GalipediaLocalidadesGenerator(u"Congo", [u"Cidades da República do {name}"]))
    generators.append(GalipediaLocalidadesGenerator(u"Corea do Norte", pageParser=FirstSentenceParser()))
    generators.append(GalipediaLocalidadesGenerator(u"Cuba"))
    generators.append(GalipediaLocalidadesGenerator(u"Dinamarca"))
    generators.append(GalipediaLocalidadesGenerator(u"Dominica", pageParser=FirstSentenceParser()))
    generators.append(GalipediaLocalidadesGenerator(u"Emiratos Árabes Unidos", [u"Cidades dos {name}"], pageParser=FirstSentenceParser()))
    generators.append(GalipediaLocalidadesGenerator(u"Eslovaquia"))
    generators.append(GalipediaLocalidadesGenerator(u"España", [u"Concellos de {name}", u"Cidades de {name}", u"Parroquias de España"], pageParser=FirstSentenceParser()))
    generators.append(GalipediaLocalidadesGenerator(u"Estados Unidos de América", [u"Cidades dos {name}"]))
    generators.append(GalipediaLocalidadesGenerator(u"Etiopía"))
    generators.append(GalipediaLocalidadesGenerator(u"Exipto"))
    generators.append(GalipediaLocalidadesGenerator(u"Finlandia", pageParser=FirstSentenceParser()))
    generators.append(GalipediaLocalidadesGenerator(u"Francia", [u"Cidades de {name}", u"Comunas de {name}"]))
    generators.append(GalipediaLocalidadesGenerator(u"Grecia", pageParser=FirstSentenceParser()))
    generators.append(GalipediaLocalidadesGenerator(u"Grecia antiga", [u"Antigas cidades gregas"]))
    generators.append(GalipediaLocalidadesGenerator(u"Guatemala", [u"Cidades de {name}", u"Municipios de {name}"]))
    generators.append(GalipediaLocalidadesGenerator(u"Guinea-Bisau"))
    generators.append(GalipediaLocalidadesGenerator(u"Hungría"))
    generators.append(GalipediaLocalidadesGenerator(u"Iemen"))
    generators.append(GalipediaLocalidadesGenerator(u"India", [u"Cidades da {name}"]))
    generators.append(GalipediaLocalidadesGenerator(u"Indonesia"))
    generators.append(GalipediaLocalidadesGenerator(u"Iraq"))
    generators.append(GalipediaLocalidadesGenerator(u"Irlanda"))
    generators.append(GalipediaLocalidadesGenerator(u"Islandia", pageParser=FirstSentenceParser()))
    generators.append(GalipediaLocalidadesGenerator(u"Israel"))
    generators.append(GalipediaLocalidadesGenerator(u"Italia", [u"Cidades de {name}", u"Comunas de {name}"]))
    generators.append(GalipediaLocalidadesGenerator(u"Kenya", pageParser=FirstSentenceParser()))
    generators.append(GalipediaLocalidadesGenerator(u"Líbano", [u"Cidades do {name}"]))
    generators.append(GalipediaLocalidadesGenerator(u"Malaisia"))
    generators.append(GalipediaLocalidadesGenerator(u"Malí"))
    generators.append(GalipediaLocalidadesGenerator(u"Marrocos", pageParser=FirstSentenceParser()))
    generators.append(GalipediaLocalidadesGenerator(u"México", [u"Cidades de {name}", u"Cidades prehispánicas de {name}", u"Concellos de {name}"]))
    generators.append(GalipediaLocalidadesGenerator(u"Mozambique", pageParser=FirstSentenceParser()))
    generators.append(GalipediaLocalidadesGenerator(u"Nepal", [u"Cidades do {name}"]))
    generators.append(GalipediaLocalidadesGenerator(u"Oceanía"))
    generators.append(GalipediaLocalidadesGenerator(u"Omán", pageParser=FirstSentenceParser()))
    generators.append(GalipediaLocalidadesGenerator(u"Países Baixos", [u"Cidades dos {name}"]))
    generators.append(GalipediaLocalidadesGenerator(u"Paquistán"))
    generators.append(GalipediaLocalidadesGenerator(u"Perú", [u"Cidades do {name}"]))
    generators.append(GalipediaLocalidadesGenerator(u"Polonia"))
    generators.append(GalipediaLocalidadesGenerator(u"Portugal", [u"Cidades de {name}", u"Municipios de {name}", u"Vilas de {name}"]))
    generators.append(GalipediaLocalidadesGenerator(u"Qatar"))
    generators.append(GalipediaLocalidadesGenerator(u"Reino Unido", [u"Cidades do {name}"]))
    generators.append(GalipediaLocalidadesGenerator(u"Romanía"))
    generators.append(GalipediaLocalidadesGenerator(u"Rusia", pageParser=FirstSentenceParser()))
    generators.append(GalipediaLocalidadesGenerator(u"Serbia"))
    generators.append(GalipediaLocalidadesGenerator(u"Siria"))
    generators.append(GalipediaLocalidadesGenerator(u"Sudán do Sur", [u"Localidades de {name}"]))
    generators.append(GalipediaLocalidadesGenerator(u"Suecia"))
    generators.append(GalipediaLocalidadesGenerator(u"Suráfrica"))
    generators.append(GalipediaLocalidadesGenerator(u"Suíza"))
    generators.append(GalipediaLocalidadesGenerator(u"Timor Leste"))
    generators.append(GalipediaLocalidadesGenerator(u"Turquía"))
    generators.append(GalipediaLocalidadesGenerator(u"Ucraína", pageParser=FirstSentenceParser()))
    generators.append(GalipediaLocalidadesGenerator(u"Venezuela"))
    generators.append(GalipediaLocalidadesGenerator(u"Xapón", [u"Concellos do {name}"], pageParser=FirstSentenceParser()))
    generators.append(GalipediaLocalidadesGenerator(u"Xordania"))

    generators.append(GalipediaGenerator(
        resource = u"onomástica/toponimia/lugares/galicia.dic",
        partOfSpeech = u"topónimo",
        entryGenerators=[
            EntryGenerator(
                pageGenerators = [
                    CategoryBrowser(
                        categoryNames = [u"Lugares de Galicia", u"Parroquias de Galicia"],
                        invalidPagePattern = u"^(Lugares d|Parroquias d)",
                        validCategoryPattern = u"^(Lugares d|Parroquias d)",
                    ),
                ],
            )
        ],
    ))

    generators.append(GalipediaGenerator(
        resource = u"onomástica/toponimia/países.dic",
        partOfSpeech = u"topónimo",
        entryGenerators=[
            EntryGenerator(
                pageGenerators = [
                    CategoryBrowser(
                        categoryNames = [
                            u"Estados desaparecidos",
                            u"Países con recoñecemento limitado",
                            u"Países de América",
                            u"Países de Asia",
                            u"Países de Europa",
                            u"Países de Oceanía",
                            u"Países de África"
                        ],
                        invalidPagePattern = u"^(Concellos |Galería d|Historia d|Lista d|Principais cidades )",
                        validCategoryPattern = u"^(Estados desaparecidos d|Imperios|Países d)",
                        invalidCategoryPattern = u"^(Capitais d|Emperadores$)",
                    ),
                ],
                pageParser=FirstSentenceParser(),
                entryParser=EntryParser(commaFilter=False),
            )
        ],
    ))

    generators.append(GalipediaRexionsGenerator(u"Alemaña", [u"Estados de {name}", u"Rexións de {name}"]))
    generators.append(GalipediaRexionsGenerator(u"Bélxica", [u"Provincias da {name}", u"Rexións de {name}"], pageParser=FirstSentenceParser()))
    generators.append(GalipediaRexionsGenerator(u"Brasil", [u"Estados do {name}"]))
    generators.append(GalipediaRexionsGenerator(u"Chile"))
    generators.append(GalipediaRexionsGenerator(u"Colombia", [u"Departamentos de {name}", u"Provincias de {name}"]))
    generators.append(GalipediaRexionsGenerator(u"España", [u"Comarcas de {name}", u"Comunidades autónomas de {name}", u"Provincias de {name}"]))
    generators.append(GalipediaRexionsGenerator(u"Estados Unidos de América", [u"Estados dos {name}", u"Distritos de Nova York"]))
    generators.append(GalipediaRexionsGenerator(u"Finlandia"))
    generators.append(GalipediaRexionsGenerator(u"Francia", [u"Departamentos de {name}", u"Rexións de {name}"]))
    generators.append(GalipediaRexionsGenerator(u"Grecia", [u"Periferias de {name}"]))
    generators.append(GalipediaRexionsGenerator(u"Guatemala", [u"Departamentos de {name}"]))
    generators.append(GalipediaRexionsGenerator(u"India", [u"Subdivisións da {name}"]))
    generators.append(GalipediaRexionsGenerator(u"Italia", [u"Rexións de {name}", u"Provincias de {name}"]))
    generators.append(GalipediaRexionsGenerator(u"México", [u"Estados de {name}"]))
    generators.append(GalipediaRexionsGenerator(u"Países Baixos", [u"Provincias dos {name}"]))
    generators.append(GalipediaRexionsGenerator(u"Portugal", [
        u"Antigas provincias portuguesas",
        u"Distritos e rexións autónomas de Portugal",
        u"NUTS I portuguesas",
        u"NUTS II portuguesas",
        u"NUTS III portuguesas",
        u"Rexións autónomas de Portugal"
    ]))
    generators.append(GalipediaRexionsGenerator(u"Reino Unido", [u"Condados de Inglaterra", u"Condados de Irlanda", u"Divisións de Escocia", u"Rexións de Inglaterra"]))
    generators.append(GalipediaRexionsGenerator(u"Rusia", [u"Repúblicas de {name}"]))

    generators.append(GalipediaGenerator(
        resource = u"onomástica/toponimia/zonas/españa.dic",
        partOfSpeech = u"topónimo",
        entryGenerators=[
            EntryGenerator(
                pageGenerators = [
                    CategoryBrowser(
                        categoryNames = [u"Barrios de España", u"Distritos de España"],
                        invalidPagePattern = u"^(Barrios|Distritos) ",
                        validCategoryPattern = u"^(Barrios|Distritos) "
                    ),
                ],
            )
        ],
    ))

    generators.append(GalipediaGenerator(
        resource = u"onomástica/toponimia/zonas/mónaco.dic",
        partOfSpeech = u"topónimo",
        entryGenerators=[
            EntryGenerator(
                pageGenerators = [
                    CategoryBrowser(
                        categoryNames = [u"Barrios de Mónaco"],
                        invalidPagePattern = u"^Barrios ",
                        validCategoryPattern = u"^Barrios "
                    ),
                ],
            )
        ],
    ))

    generators.append(GalipediaNamesGenerator())


    # Wikipedia en castelán.

    generators.append(WikipediaEsGenerator(
        resource = u"antroponimia.dic",
        partOfSpeech = u"antropónimo",
        entryGenerators=[
            EntryGenerator(
                pageGenerators = [
                    CategoryBrowser(
                        categoryNames = [u"Nombres por género"],
                        validCategoryPattern = u"^Nombres ",
                        invalidCategoryPattern = u"^Puranas$",
                    ),
                ],
            )
        ],
    ))


    # Wikipedia en inglés.

    generators.append(WikipediaEnGenerator(
        resource = u"antroponimia/xeral.dic",
        partOfSpeech = u"antropónimo",
        entryGenerators=[
            EntryGenerator(
                pageGenerators = [
                    CategoryBrowser(
                        categoryNames = [u"Given names by gender"],
                        validCategoryPattern = u".* (god(desse)?s|names)",
                        invalidPagePattern = u"^(Consorts of Ganesha|Forms of Parvati|Ganges in Hinduism|.* Temple)$",
                    ),
                ],
            ),
            EntryGenerator(
                pageGenerators = [
                    CategoryBrowser(
                        categoryNames = [u"Basque given names"],
                        validCategoryPattern = u".* names",
                    ),
                ],
                pageParser=FirstSentenceParser(),
            )
        ],
    ))

    generators.append(WikipediaEnGenerator(
        resource = u"antroponimia/países/brasil.dic",
        partOfSpeech = u"antropónimo",
        entryGenerators=[
            EntryGenerator(
                pageGenerators = [
                    CategoryBrowser(
                        categoryNames = [u"People by state in Brazil"],
                        validCategoryPattern = u".*",
                    ),
                ],
            )
        ],
    ))

    generators.append(WikipediaEnGenerator(
        resource = u"antroponimia/países/italia.dic",
        partOfSpeech = u"antropónimo",
        entryGenerators=[
            EntryGenerator(
                pageGenerators = [
                    CategoryBrowser(
                        categoryNames = [u"Italian sculptors"],
                        validCategoryPattern = u".* (sculptors|stubs)",
                    ),
                ],
            )
        ],
    ))

    # Wikipedia en húngaro.

    generators.append(WikipediaHuGenerator(
        resource = u"antroponimia.dic",
        partOfSpeech = u"antropónimo",
        entryGenerators=[
            EntryGenerator(
                pageGenerators = [
                    CategoryBrowser(
                        categoryOfCategoriesNames = [u"Férfikeresztnevek", u"Női keresztnevek"],
                    ),
                ],
            )
        ],
    ))

    # Wikipedia en portugués.

    generators.append(WikipediaPtGenerator(
        resource = u"antroponimia/países/españa.dic",
        partOfSpeech = u"antropónimo",
        entryGenerators=[
            EntryGenerator(
                pageGenerators = [
                    CategoryBrowser(
                        categoryNames = [u"Reis de Leão",],
                        invalidPagePattern = u"^Anexo:",
                    ),
                ],
            )
        ],
    ))


    return generators