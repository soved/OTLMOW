# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod
from OTLMOW.OTLModel.Classes.ConstructieElement import ConstructieElement
from OTLMOW.OTLModel.Datatypes.KwantWrdInCentimeter import KwantWrdInCentimeter
from OTLMOW.OTLModel.Datatypes.KwantWrdInMeterTAW import KwantWrdInMeterTAW


# Generated with OTLClassCreator. To modify: extend, do not edit
class Fundering(ConstructieElement):
    """Abstracte voor verschillende manieren om er voor te zorgen dat het eigen gewicht van het object dat de fundering krijgt en de krachten uitgeoefend op dat object, zoals nuttige belasting, sneeuw, winddruk, enzovoorts, worden overgedragen op de draagkrachtige ondergrond. Een fundering zit hoofdzakelijk onder het maaiveld en heeft tot doel het stabiliseren van een ander object."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Fundering'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self._aanzetpeil = OTLAttribuut(field=KwantWrdInMeterTAW,
                                        naam='aanzetpeil',
                                        label='aanzetpeil',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Fundering.aanzetpeil',
                                        definition='De hoogte van het laagste punt van de onderkant van een element, ten opzichte van gemiddeld laagwaterpeil te Oostende (TAWpeil).',
                                        owner=self)

        self._hoogte = OTLAttribuut(field=KwantWrdInCentimeter,
                                    naam='hoogte',
                                    label='hoogte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Fundering.hoogte',
                                    usagenote='Attribuut uit gebruik sinds versie 2.0.0-RC4',
                                    deprecated_version='2.0.0-RC4',
                                    definition='De afstand tussen het laagste punt van de onderkant en hoogste punt van de bovenkant van de fundering.',
                                    owner=self)

    @property
    def aanzetpeil(self):
        """De hoogte van het laagste punt van de onderkant van een element, ten opzichte van gemiddeld laagwaterpeil te Oostende (TAWpeil)."""
        return self._aanzetpeil.waarde

    @aanzetpeil.setter
    def aanzetpeil(self, value):
        self._aanzetpeil.set_waarde(value, owner=self)

    @property
    def hoogte(self):
        """De afstand tussen het laagste punt van de onderkant en hoogste punt van de bovenkant van de fundering."""
        return self._hoogte.waarde

    @hoogte.setter
    def hoogte(self, value):
        self._hoogte.set_waarde(value, owner=self)
