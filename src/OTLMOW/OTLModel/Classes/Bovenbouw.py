# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.AIMObject import AIMObject
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLMOW.OTLModel.Datatypes.KlDekselKaderType import KlDekselKaderType
from OTLMOW.OTLModel.Datatypes.KlDekselKlasse import KlDekselKlasse
from OTLMOW.OTLModel.Datatypes.KlDekselMateriaal import KlDekselMateriaal
from OTLMOW.OTLModel.Datatypes.KlDekselRegeling import KlDekselRegeling
from OTLMOW.OTLModel.Datatypes.KlDekselVergrendeling import KlDekselVergrendeling
from OTLMOW.OTLModel.Datatypes.KlRioleringVorm import KlRioleringVorm
from OTLMOW.OTLModel.Datatypes.KwantWrdInCentimeter import KwantWrdInCentimeter
from OTLMOW.OTLModel.Datatypes.KwantWrdInVierkanteMeter import KwantWrdInVierkanteMeter
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie
from OTLMOW.GeometrieArtefact.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Bovenbouw(AIMObject, PuntGeometrie, VlakGeometrie):
    """Een combinatie van het riooldeksel met de kader en de regeling."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bovenbouw'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    deprecated_version = '2.1.0-RC2'

    def __init__(self):
        AIMObject.__init__(self)
        PuntGeometrie.__init__(self)
        VlakGeometrie.__init__(self)

        self._breedte = OTLAttribuut(field=KwantWrdInCentimeter,
                                     naam='breedte',
                                     label='breedte',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bovenbouw.breedte',
                                     usagenote='Klasse uit gebruik sinds versie 2.1.0-RC2',
                                     deprecated_version='2.1.0-RC2',
                                     definition='Breedte-afmeting van het deksel in centimeter. Bij vierkante en cirkelvormige deksels is deze waarde gelijk aan de hoogte.',
                                     owner=self)

        self._dekselklasse = OTLAttribuut(field=KlDekselKlasse,
                                          naam='dekselklasse',
                                          label='dekselklasse',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bovenbouw.dekselklasse',
                                          usagenote='Klasse uit gebruik sinds versie 2.1.0-RC2',
                                          deprecated_version='2.1.0-RC2',
                                          definition='Bepaalt de mate waarin het deksel van de bovenbouw belast kan worden door voertuigen.',
                                          owner=self)

        self._dekselvorm = OTLAttribuut(field=KlRioleringVorm,
                                        naam='dekselvorm',
                                        label='dekselvorm',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bovenbouw.dekselvorm',
                                        usagenote='Klasse uit gebruik sinds versie 2.1.0-RC2',
                                        deprecated_version='2.1.0-RC2',
                                        definition='Bepaalt de vorm van het deksel.',
                                        owner=self)

        self._hoogte = OTLAttribuut(field=KwantWrdInCentimeter,
                                    naam='hoogte',
                                    label='hoogte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bovenbouw.hoogte',
                                    usagenote='Klasse uit gebruik sinds versie 2.1.0-RC2',
                                    deprecated_version='2.1.0-RC2',
                                    definition='Hoogte-afmeting van het deksel in centimeter. Bij vierkante en cirkelvormige deksels is deze waarde gelijk aan de breedte.',
                                    owner=self)

        self._isAfgesloten = OTLAttribuut(field=BooleanField,
                                          naam='isAfgesloten',
                                          label='is afgesloten',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bovenbouw.isAfgesloten',
                                          usagenote='Klasse uit gebruik sinds versie 2.1.0-RC2',
                                          deprecated_version='2.1.0-RC2',
                                          definition='Bepaling of de afsluitinrichting vergrendeld is of niet.',
                                          owner=self)

        self._isScharnierend = OTLAttribuut(field=BooleanField,
                                            naam='isScharnierend',
                                            label='is scharnierend',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bovenbouw.isScharnierend',
                                            usagenote='Klasse uit gebruik sinds versie 2.1.0-RC2',
                                            deprecated_version='2.1.0-RC2',
                                            definition='Het deksel is al of niet bevestigd met een scharnier.',
                                            owner=self)

        self._isWaterdichtVergrendeld = OTLAttribuut(field=BooleanField,
                                                     naam='isWaterdichtVergrendeld',
                                                     label='Is waterdicht vergrendeld',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bovenbouw.isWaterdichtVergrendeld',
                                                     usagenote='Klasse uit gebruik sinds versie 2.1.0-RC2',
                                                     deprecated_version='2.1.0-RC2',
                                                     definition='Geeft aan of de bovenbouw al dan niet waterdicht vergrendeld is zodat het water zich niet boven de bovenbouw kan begeven.',
                                                     owner=self)

        self._kader = OTLAttribuut(field=KlDekselKaderType,
                                   naam='kader',
                                   label='kader',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bovenbouw.kader',
                                   usagenote='Klasse uit gebruik sinds versie 2.1.0-RC2',
                                   deprecated_version='2.1.0-RC2',
                                   definition='Bepaalt het type van het dekselkader.',
                                   owner=self)

        self._materiaal = OTLAttribuut(field=KlDekselMateriaal,
                                       naam='materiaal',
                                       label='materiaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bovenbouw.materiaal',
                                       usagenote='Klasse uit gebruik sinds versie 2.1.0-RC2',
                                       deprecated_version='2.1.0-RC2',
                                       definition='Het materiaal waaruit het deksel van de bovenbouw is vervaardigd.',
                                       owner=self)

        self._oppervlakte = OTLAttribuut(field=KwantWrdInVierkanteMeter,
                                         naam='oppervlakte',
                                         label='oppervlakte',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bovenbouw.oppervlakte',
                                         usagenote='Klasse uit gebruik sinds versie 2.1.0-RC2',
                                         deprecated_version='2.1.0-RC2',
                                         definition='De oppervlakte van het zichtbare deel van de bovenbouw in vierkante meter.',
                                         owner=self)

        self._regeling = OTLAttribuut(field=KlDekselRegeling,
                                      naam='regeling',
                                      label='regeling',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bovenbouw.regeling',
                                      usagenote='Klasse uit gebruik sinds versie 2.1.0-RC2',
                                      deprecated_version='2.1.0-RC2',
                                      definition='De wijze hoe de regeling van het deksel is uitgevoerd.',
                                      owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bovenbouw.technischeFiche',
                                             usagenote='Klasse uit gebruik sinds versie 2.1.0-RC2 .Bestanden van het type xlsx of pdf.',
                                             deprecated_version='2.1.0-RC2',
                                             kardinaliteit_max='*',
                                             definition='De technische fiche van de bovenbouw.',
                                             owner=self)

        self._vergrendeling = OTLAttribuut(field=KlDekselVergrendeling,
                                           naam='vergrendeling',
                                           label='vergrendeling',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bovenbouw.vergrendeling',
                                           usagenote='Klasse uit gebruik sinds versie 2.1.0-RC2',
                                           deprecated_version='2.1.0-RC2',
                                           definition='Bepaalt het type sleutel voor het ontgrendelen van het deksel.',
                                           owner=self)

    @property
    def breedte(self):
        """Breedte-afmeting van het deksel in centimeter. Bij vierkante en cirkelvormige deksels is deze waarde gelijk aan de hoogte."""
        return self._breedte.waarde

    @breedte.setter
    def breedte(self, value):
        self._breedte.set_waarde(value, owner=self)

    @property
    def dekselklasse(self):
        """Bepaalt de mate waarin het deksel van de bovenbouw belast kan worden door voertuigen."""
        return self._dekselklasse.waarde

    @dekselklasse.setter
    def dekselklasse(self, value):
        self._dekselklasse.set_waarde(value, owner=self)

    @property
    def dekselvorm(self):
        """Bepaalt de vorm van het deksel."""
        return self._dekselvorm.waarde

    @dekselvorm.setter
    def dekselvorm(self, value):
        self._dekselvorm.set_waarde(value, owner=self)

    @property
    def hoogte(self):
        """Hoogte-afmeting van het deksel in centimeter. Bij vierkante en cirkelvormige deksels is deze waarde gelijk aan de breedte."""
        return self._hoogte.waarde

    @hoogte.setter
    def hoogte(self, value):
        self._hoogte.set_waarde(value, owner=self)

    @property
    def isAfgesloten(self):
        """Bepaling of de afsluitinrichting vergrendeld is of niet."""
        return self._isAfgesloten.waarde

    @isAfgesloten.setter
    def isAfgesloten(self, value):
        self._isAfgesloten.set_waarde(value, owner=self)

    @property
    def isScharnierend(self):
        """Het deksel is al of niet bevestigd met een scharnier."""
        return self._isScharnierend.waarde

    @isScharnierend.setter
    def isScharnierend(self, value):
        self._isScharnierend.set_waarde(value, owner=self)

    @property
    def isWaterdichtVergrendeld(self):
        """Geeft aan of de bovenbouw al dan niet waterdicht vergrendeld is zodat het water zich niet boven de bovenbouw kan begeven."""
        return self._isWaterdichtVergrendeld.waarde

    @isWaterdichtVergrendeld.setter
    def isWaterdichtVergrendeld(self, value):
        self._isWaterdichtVergrendeld.set_waarde(value, owner=self)

    @property
    def kader(self):
        """Bepaalt het type van het dekselkader."""
        return self._kader.waarde

    @kader.setter
    def kader(self, value):
        self._kader.set_waarde(value, owner=self)

    @property
    def materiaal(self):
        """Het materiaal waaruit het deksel van de bovenbouw is vervaardigd."""
        return self._materiaal.waarde

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self)

    @property
    def oppervlakte(self):
        """De oppervlakte van het zichtbare deel van de bovenbouw in vierkante meter."""
        return self._oppervlakte.waarde

    @oppervlakte.setter
    def oppervlakte(self, value):
        self._oppervlakte.set_waarde(value, owner=self)

    @property
    def regeling(self):
        """De wijze hoe de regeling van het deksel is uitgevoerd."""
        return self._regeling.waarde

    @regeling.setter
    def regeling(self, value):
        self._regeling.set_waarde(value, owner=self)

    @property
    def technischeFiche(self):
        """De technische fiche van de bovenbouw."""
        return self._technischeFiche.waarde

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)

    @property
    def vergrendeling(self):
        """Bepaalt het type sleutel voor het ontgrendelen van het deksel."""
        return self._vergrendeling.waarde

    @vergrendeling.setter
    def vergrendeling(self, value):
        self._vergrendeling.set_waarde(value, owner=self)
