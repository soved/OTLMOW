# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod
from OTLMOW.OTLModel.Classes.Draagconstructie import Draagconstructie
from OTLMOW.OTLModel.Datatypes.KlEMDraagconstructieElekBeveiliging import KlEMDraagconstructieElekBeveiliging


# Generated with OTLClassCreator. To modify: extend, do not edit
class EMDraagconstructie(Draagconstructie):
    """Abstracte voor een elektromechanisch (EM) dragend element (bv. paal, kolom, seinbrug, galgpaal, mast) waaraan EM-toestellen bevestigd kunnen worden."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#EMDraagconstructie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self._elektrischeBeveiliging = OTLAttribuut(field=KlEMDraagconstructieElekBeveiliging,
                                                    naam='elektrischeBeveiliging',
                                                    label='elektrische beveiliging',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#EMDraagconstructie.elektrischeBeveiliging',
                                                    definition='Type elektrische beveiliging aanwezig in de draagconstructie.',
                                                    owner=self)

    @property
    def elektrischeBeveiliging(self):
        """Type elektrische beveiliging aanwezig in de draagconstructie."""
        return self._elektrischeBeveiliging.waarde

    @elektrischeBeveiliging.setter
    def elektrischeBeveiliging(self, value):
        self._elektrischeBeveiliging.set_waarde(value, owner=self)
