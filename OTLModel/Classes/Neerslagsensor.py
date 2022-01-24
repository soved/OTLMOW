# coding=utf-8
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLModel.Datatypes.KlNeerslagsensorMerk import KlNeerslagsensorMerk
from OTLModel.Datatypes.KlNeerslagsensorModelnaam import KlNeerslagsensorModelnaam
from OTLModel.Datatypes.KlNeerslagsensorType import KlNeerslagsensorType


# Generated with OTLClassCreator. To modify: extend, do not edit
class Neerslagsensor(AIMNaamObject):
    """Detectie van neerslag(hoeveelheid/intensiteit)."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Neerslagsensor'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._merk = OTLAttribuut(field=KlNeerslagsensorMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Neerslagsensor.merk',
                                  definition='Het merk van de neerslagsensor.')

        self._modelnaam = OTLAttribuut(field=KlNeerslagsensorModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Neerslagsensor.modelnaam',
                                       definition='De modelnaam van de neerslagsensor.')

        self._type = OTLAttribuut(field=KlNeerslagsensorType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Neerslagsensor.type',
                                  definition='Het type van de neerslagsensor.')

    @property
    def merk(self):
        """Het merk van de neerslagsensor."""
        return self._merk.waarde

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self):
        """De modelnaam van de neerslagsensor."""
        return self._modelnaam.waarde

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def type(self):
        """Het type van de neerslagsensor."""
        return self._type.waarde

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
