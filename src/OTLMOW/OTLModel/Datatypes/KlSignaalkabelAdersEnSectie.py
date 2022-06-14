# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSignaalkabelAdersEnSectie(KeuzelijstField):
    """Lijst van mogelijke waarden volgens de catalogusposten van het standaardbestek voor de samenstelling van een signalisatiekabel volgens het aantal aders en hun sectie in vierkante millimeter."""
    naam = 'KlSignaalkabelAdersEnSectie'
    label = 'Voedingskabel aders specificaties'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSignaalkabelAdersEnSectie'
    definition = 'Lijst van mogelijke waarden volgens de catalogusposten van het standaardbestek voor de samenstelling van een signalisatiekabel volgens het aantal aders en hun sectie in vierkante millimeter.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSignaalkabelAdersEnSectie'
    options = {
        '10-x-1.5-mm2': KeuzelijstWaarde(invulwaarde='10-x-1.5-mm2',
                                         label='10 x 1.5 mm²',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignaalkabelAdersEnSectie/10-x-1.5-mm2'),
        '10-x-2.5-mm2': KeuzelijstWaarde(invulwaarde='10-x-2.5-mm2',
                                         label='10 x 2.5 mm²',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignaalkabelAdersEnSectie/10-x-2.5-mm2'),
        '12-x-1.5-mm2': KeuzelijstWaarde(invulwaarde='12-x-1.5-mm2',
                                         label='12 x 1.5 mm²',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignaalkabelAdersEnSectie/12-x-1.5-mm2'),
        '14-x-1.5-mm2': KeuzelijstWaarde(invulwaarde='14-x-1.5-mm2',
                                         label='14 x 1.5 mm²',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignaalkabelAdersEnSectie/14-x-1.5-mm2'),
        '14-x-2.5-mm2': KeuzelijstWaarde(invulwaarde='14-x-2.5-mm2',
                                         label='14 x 2.5 mm²',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignaalkabelAdersEnSectie/14-x-2.5-mm2'),
        '16-x-1.5-mm2': KeuzelijstWaarde(invulwaarde='16-x-1.5-mm2',
                                         label='16 x 1.5 mm²',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignaalkabelAdersEnSectie/16-x-1.5-mm2'),
        '16-x-2.5-mm2': KeuzelijstWaarde(invulwaarde='16-x-2.5-mm2',
                                         label='16 x 2.5 mm²',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignaalkabelAdersEnSectie/16-x-2.5-mm2'),
        '19-x-1.5-mm2': KeuzelijstWaarde(invulwaarde='19-x-1.5-mm2',
                                         label='19 x 1.5 mm²',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignaalkabelAdersEnSectie/19-x-1.5-mm2'),
        '19-x-2.5-mm2': KeuzelijstWaarde(invulwaarde='19-x-2.5-mm2',
                                         label='19 x 2.5 mm²',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignaalkabelAdersEnSectie/19-x-2.5-mm2'),
        '21-x-1.5-mm2': KeuzelijstWaarde(invulwaarde='21-x-1.5-mm2',
                                         label='21 x 1.5 mm²',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignaalkabelAdersEnSectie/21-x-1.5-mm2'),
        '21-x-2.5-mm2': KeuzelijstWaarde(invulwaarde='21-x-2.5-mm2',
                                         label='21 x 2.5 mm²',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignaalkabelAdersEnSectie/21-x-2.5-mm2'),
        '24-x-1.5-mm2': KeuzelijstWaarde(invulwaarde='24-x-1.5-mm2',
                                         label='24 x 1.5 mm²',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignaalkabelAdersEnSectie/24-x-1.5-mm2'),
        '24-x-2.5-mm2': KeuzelijstWaarde(invulwaarde='24-x-2.5-mm2',
                                         label='24 x 2.5 mm²',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignaalkabelAdersEnSectie/24-x-2.5-mm2'),
        '27-x-1.5-mm2': KeuzelijstWaarde(invulwaarde='27-x-1.5-mm2',
                                         label='27 x 1.5 mm²',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignaalkabelAdersEnSectie/27-x-1.5-mm2'),
        '27-x-2.5-mm2': KeuzelijstWaarde(invulwaarde='27-x-2.5-mm2',
                                         label='27 x 2.5 mm²',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignaalkabelAdersEnSectie/27-x-2.5-mm2'),
        '30-x-1.5-mm2': KeuzelijstWaarde(invulwaarde='30-x-1.5-mm2',
                                         label='30 x 1.5 mm²',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignaalkabelAdersEnSectie/30-x-1.5-mm2'),
        '30-x-2.5-mm2': KeuzelijstWaarde(invulwaarde='30-x-2.5-mm2',
                                         label='30 x 2.5 mm²',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignaalkabelAdersEnSectie/30-x-2.5-mm2'),
        '33-x-1.5-mm2': KeuzelijstWaarde(invulwaarde='33-x-1.5-mm2',
                                         label='33 x 1.5 mm²',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignaalkabelAdersEnSectie/33-x-1.5-mm2'),
        '33-x-2.5-mm2': KeuzelijstWaarde(invulwaarde='33-x-2.5-mm2',
                                         label='33 x 2.5 mm²',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignaalkabelAdersEnSectie/33-x-2.5-mm2'),
        '37-x-1.5-mm2': KeuzelijstWaarde(invulwaarde='37-x-1.5-mm2',
                                         label='37 x 1.5 mm²',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignaalkabelAdersEnSectie/37-x-1.5-mm2'),
        '37-x-2.5-mm2': KeuzelijstWaarde(invulwaarde='37-x-2.5-mm2',
                                         label='37 x 2.5 mm²',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignaalkabelAdersEnSectie/37-x-2.5-mm2'),
        '40-x-1.5-mm2': KeuzelijstWaarde(invulwaarde='40-x-1.5-mm2',
                                         label='40 x 1.5 mm²',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignaalkabelAdersEnSectie/40-x-1.5-mm2'),
        '40-x-2.5-mm2': KeuzelijstWaarde(invulwaarde='40-x-2.5-mm2',
                                         label='40 x 2.5 mm²',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignaalkabelAdersEnSectie/40-x-2.5-mm2'),
        '44-x-1.5-mm2': KeuzelijstWaarde(invulwaarde='44-x-1.5-mm2',
                                         label='44 x 1.5 mm²',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignaalkabelAdersEnSectie/44-x-1.5-mm2'),
        '44-x-2.5-mm2': KeuzelijstWaarde(invulwaarde='44-x-2.5-mm2',
                                         label='44 x 2.5 mm²',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignaalkabelAdersEnSectie/44-x-2.5-mm2'),
        '48-x-1.5-mm2': KeuzelijstWaarde(invulwaarde='48-x-1.5-mm2',
                                         label='48 x 1.5 mm²',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignaalkabelAdersEnSectie/48-x-1.5-mm2'),
        '48-x-2.5-mm2': KeuzelijstWaarde(invulwaarde='48-x-2.5-mm2',
                                         label='48 x 2.5 mm²',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignaalkabelAdersEnSectie/48-x-2.5-mm2'),
        '5-x-1.5-mm2': KeuzelijstWaarde(invulwaarde='5-x-1.5-mm2',
                                        label='5 x 1.5 mm²',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignaalkabelAdersEnSectie/5-x-1.5-mm2'),
        '5-x-2.5-mm2': KeuzelijstWaarde(invulwaarde='5-x-2.5-mm2',
                                        label='5 x 2.5 mm²',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignaalkabelAdersEnSectie/5-x-2.5-mm2'),
        '61-x-1.5-mm2': KeuzelijstWaarde(invulwaarde='61-x-1.5-mm2',
                                         label='61 x 1.5 mm²',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignaalkabelAdersEnSectie/61-x-1.5-mm2'),
        '61-x-2.5-mm2': KeuzelijstWaarde(invulwaarde='61-x-2.5-mm2',
                                         label='61 x 2.5 mm²',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignaalkabelAdersEnSectie/61-x-2.5-mm2'),
        '7-x-1.5-mm2': KeuzelijstWaarde(invulwaarde='7-x-1.5-mm2',
                                        label='7 x 1.5 mm²',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignaalkabelAdersEnSectie/7-x-1.5-mm2'),
        '7-x-2.5-mm2': KeuzelijstWaarde(invulwaarde='7-x-2.5-mm2',
                                        label='7 x 2.5 mm²',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignaalkabelAdersEnSectie/7-x-2.5-mm2'),
        '8-x-1.5-mm2': KeuzelijstWaarde(invulwaarde='8-x-1.5-mm2',
                                        label='8 x 1.5 mm²',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignaalkabelAdersEnSectie/8-x-1.5-mm2'),
        '8-x-2.5-mm2': KeuzelijstWaarde(invulwaarde='8-x-2.5-mm2',
                                        label='8 x 2.5 mm²',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignaalkabelAdersEnSectie/8-x-2.5-mm2'),
        'zonder-bijkomende-specificatie': KeuzelijstWaarde(invulwaarde='zonder-bijkomende-specificatie',
                                                           label='zonder bijkomende specificatie',
                                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignaalkabelAdersEnSectie/zonder-bijkomende-specificatie')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlSignaalkabelAdersEnSectie.get_dummy_data()

