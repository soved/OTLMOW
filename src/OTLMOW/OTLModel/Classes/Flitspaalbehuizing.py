# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLMOW.OTLModel.Datatypes.KlFlitspaalbehuizingMerk import KlFlitspaalbehuizingMerk
from OTLMOW.OTLModel.Datatypes.KlFlitspaalbehuizingModelnaam import KlFlitspaalbehuizingModelnaam


# Generated with OTLClassCreator. To modify: extend, do not edit
class Flitspaalbehuizing(AIMNaamObject):
    """Een weersbestendige en vandalismebestendige behuizing waarin een snelheids- en/of roodlichtcamera kan worden bevestigd."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Flitspaalbehuizing'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._merk = OTLAttribuut(field=KlFlitspaalbehuizingMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Flitspaalbehuizing.merk',
                                  definition='Het merk van de flitspaalbehuizing.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlFlitspaalbehuizingModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Flitspaalbehuizing.modelnaam',
                                       definition='Het model of productrange van de flitspaalbehuizing.',
                                       owner=self)

    @property
    def merk(self):
        """Het merk van de flitspaalbehuizing."""
        return self._merk.waarde

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self):
        """Het model of productrange van de flitspaalbehuizing."""
        return self._modelnaam.waarde

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)
