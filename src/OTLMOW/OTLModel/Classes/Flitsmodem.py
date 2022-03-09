# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.AIMObject import AIMObject
from OTLMOW.OTLModel.Datatypes.KlFlitsmodemMerk import KlFlitsmodemMerk
from OTLMOW.OTLModel.Datatypes.KlFlitsmodemModelnaam import KlFlitsmodemModelnaam
from OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class Flitsmodem(AIMObject):
    """Communicatiemodem van het snelheids- roodlichtcamera's systeem dat via het (extern) netwerk communiceert. """

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Flitsmodem'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._merk = OTLAttribuut(field=KlFlitsmodemMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Flitsmodem.merk',
                                  definition='Het merk van de flitsmodem.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlFlitsmodemModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Flitsmodem.modelnaam',
                                       definition='Het model of productrange van de flitsmodem.',
                                       owner=self)

        self._serienummer = OTLAttribuut(field=StringField,
                                         naam='serienummer',
                                         label='serienummer',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Flitsmodem.serienummer',
                                         definition='Het unieke nummer waarmee het toestel door de fabrikant geïdentificeerd is.',
                                         owner=self)

    @property
    def merk(self):
        """Het merk van de flitsmodem."""
        return self._merk.waarde

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self):
        """Het model of productrange van de flitsmodem."""
        return self._modelnaam.waarde

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def serienummer(self):
        """Het unieke nummer waarmee het toestel door de fabrikant geïdentificeerd is."""
        return self._serienummer.waarde

    @serienummer.setter
    def serienummer(self, value):
        self._serienummer.set_waarde(value, owner=self)
