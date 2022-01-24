# coding=utf-8
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.Geluidsschermelement import Geluidsschermelement
from OTLModel.Datatypes.KlVGOpstelling import KlVGOpstelling
from OTLModel.Datatypes.KlVGSchermelementtype import KlVGSchermelementtype
from OTLModel.Datatypes.KlVormSchermelement import KlVormSchermelement


# Generated with OTLClassCreator. To modify: extend, do not edit
class VlakGeluidsschermelement(Geluidsschermelement):
    """Een vlak scherm zijn alle schermtypes die getest kunnen worden volgens de normen NBN EN 1793-1 NBN EN 1793-2."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VlakGeluidsschermelement'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._opstelling = OTLAttribuut(field=KlVGOpstelling,
                                        naam='opstelling',
                                        label='opstelling',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VlakGeluidsschermelement.opstelling',
                                        definition='Dit attribuut beschrijft de oriëntatie van het geplaatste schermelement t.o.v. de weg. De oriëntatie van vlakke schermen kan naast loodrecht op het maaiveld ook schuin naar achter hellend of schuin naar voor hellend zijn.')

        self._schermelementtype = OTLAttribuut(field=KlVGSchermelementtype,
                                               naam='schermelementtype',
                                               label='schermelementtype',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VlakGeluidsschermelement.schermelementtype',
                                               definition='Het type vlak-schermelement.')

        self._vorm = OTLAttribuut(field=KlVormSchermelement,
                                  naam='vorm',
                                  label='vorm',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VlakGeluidsschermelement.vorm',
                                  definition='Dit attribuut geeft aan of het schermelement recht of gebogen is.')

    @property
    def opstelling(self):
        """Dit attribuut beschrijft de oriëntatie van het geplaatste schermelement t.o.v. de weg. De oriëntatie van vlakke schermen kan naast loodrecht op het maaiveld ook schuin naar achter hellend of schuin naar voor hellend zijn."""
        return self._opstelling.waarde

    @opstelling.setter
    def opstelling(self, value):
        self._opstelling.set_waarde(value, owner=self)

    @property
    def schermelementtype(self):
        """Het type vlak-schermelement."""
        return self._schermelementtype.waarde

    @schermelementtype.setter
    def schermelementtype(self, value):
        self._schermelementtype.set_waarde(value, owner=self)

    @property
    def vorm(self):
        """Dit attribuut geeft aan of het schermelement recht of gebogen is."""
        return self._vorm.waarde

    @vorm.setter
    def vorm(self, value):
        self._vorm.set_waarde(value, owner=self)
