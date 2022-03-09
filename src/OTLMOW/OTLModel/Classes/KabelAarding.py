# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod, ABC
from OTLMOW.OTLModel.Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class KabelAarding(ABC):
    """Abstracte voor eigenschappen van verschillende types kabel gebruikt voor aardingen"""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelAarding'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        self._buitenmantelDiameter = OTLAttribuut(field=KwantWrdInMillimeter,
                                                  naam='buitenmantelDiameter',
                                                  label='buitenmantel diameter',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelAarding.buitenmantelDiameter',
                                                  definition='De buitenste afmeting van de kabel in millimeter.',
                                                  owner=self)

    @property
    def buitenmantelDiameter(self):
        """De buitenste afmeting van de kabel in millimeter."""
        return self._buitenmantelDiameter.waarde

    @buitenmantelDiameter.setter
    def buitenmantelDiameter(self, value):
        self._buitenmantelDiameter.set_waarde(value, owner=self)
