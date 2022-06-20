# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod
from OTLMOW.OTLModel.Classes.Abstracten.Voedingspunt import Voedingspunt
from OTLMOW.OTLModel.Datatypes.DateField import DateField
from OTLMOW.OTLModel.Datatypes.DtcAdres import DtcAdres
from OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLMOW.OTLModel.Datatypes.DtcRechtspersoon import DtcRechtspersoon
from OTLMOW.OTLModel.Datatypes.KwantWrdInKiloVoltAmpere import KwantWrdInKiloVoltAmpere
from OTLMOW.OTLModel.Datatypes.StringField import StringField
from OTLMOW.GeometrieArtefact.GeenGeometrie import GeenGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class DNB(Voedingspunt, GeenGeometrie):
    """Een abstracte die de gegevens van de distributienetbeheerder bevat die bij een aansluiting horen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#DNB'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        Voedingspunt.__init__(self)
        GeenGeometrie.__init__(self)

        self._aansluitvermogen = OTLAttribuut(field=KwantWrdInKiloVoltAmpere,
                                              naam='aansluitvermogen',
                                              label='aansluitvermogen',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#DNB.aansluitvermogen',
                                              definition='Vermogen van de aansluiting.',
                                              owner=self)

        self._adresVolgensDNB = OTLAttribuut(field=DtcAdres,
                                             naam='adresVolgensDNB',
                                             label='adres volgens DNB',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#DNB.adresVolgensDNB',
                                             definition='Het adres van de aansluiting volgens de distributienetbeheerder.',
                                             owner=self)

        self._datumEnergieleveringscontract = OTLAttribuut(field=DateField,
                                                           naam='datumEnergieleveringscontract',
                                                           label='datum energieleveringscontract',
                                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#DNB.datumEnergieleveringscontract',
                                                           definition='De datum waarop het energieleveringscontract afgesloten is.',
                                                           owner=self)

        self._datumOprichting = OTLAttribuut(field=DateField,
                                             naam='datumOprichting',
                                             label='datum oprichting',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#DNB.datumOprichting',
                                             definition='Datum waarop de DNB het voedingsbord koppelt met het net.',
                                             owner=self)

        self._datumStartEnergielevering = OTLAttribuut(field=DateField,
                                                       naam='datumStartEnergielevering',
                                                       label='datum start energielevering',
                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#DNB.datumStartEnergielevering',
                                                       definition='De datum waarop de energielevering effectief aanvangt. Dit gebeurt zodra zowel de aansluiting op het DNB-net als het energieleveringscontract in orde zijn.',
                                                       owner=self)

        self._eanNummer = OTLAttribuut(field=StringField,
                                       naam='eanNummer',
                                       label='ean nummer',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#DNB.eanNummer',
                                       definition='Uniek identificatienummer van de elektrische aansluiting, bestaande uit 18 cijfers.',
                                       owner=self)

        self._energieleverancier = OTLAttribuut(field=DtcRechtspersoon,
                                                naam='energieleverancier',
                                                label='energieleverancier',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#DNB.energieleverancier',
                                                definition='Leverancier van de energie.',
                                                owner=self)

        self._netbeheerder = OTLAttribuut(field=DtcRechtspersoon,
                                          naam='netbeheerder',
                                          label='netbeheerder',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#DNB.netbeheerder',
                                          definition='Lokale instantie die instaat voor het beheer van het elektriciteitsnet.',
                                          owner=self)

        self._referentieDNB = OTLAttribuut(field=StringField,
                                           naam='referentieDNB',
                                           label='referentie distributienetbeheerder',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#DNB.referentieDNB',
                                           definition='De wijze waarop, de referentie waarmee de aansluiting gekend is bij de distributienetbeheerder.',
                                           owner=self)

        self._risicoAnalyse = OTLAttribuut(field=DtcDocument,
                                           naam='risicoAnalyse',
                                           label='risico analyse',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#DNB.risicoAnalyse',
                                           definition='Document met de risicoanalyse.',
                                           owner=self)

    @property
    def aansluitvermogen(self):
        """Vermogen van de aansluiting."""
        return self._aansluitvermogen.get_waarde()

    @aansluitvermogen.setter
    def aansluitvermogen(self, value):
        self._aansluitvermogen.set_waarde(value, owner=self)

    @property
    def adresVolgensDNB(self):
        """Het adres van de aansluiting volgens de distributienetbeheerder."""
        return self._adresVolgensDNB.get_waarde()

    @adresVolgensDNB.setter
    def adresVolgensDNB(self, value):
        self._adresVolgensDNB.set_waarde(value, owner=self)

    @property
    def datumEnergieleveringscontract(self):
        """De datum waarop het energieleveringscontract afgesloten is."""
        return self._datumEnergieleveringscontract.get_waarde()

    @datumEnergieleveringscontract.setter
    def datumEnergieleveringscontract(self, value):
        self._datumEnergieleveringscontract.set_waarde(value, owner=self)

    @property
    def datumOprichting(self):
        """Datum waarop de DNB het voedingsbord koppelt met het net."""
        return self._datumOprichting.get_waarde()

    @datumOprichting.setter
    def datumOprichting(self, value):
        self._datumOprichting.set_waarde(value, owner=self)

    @property
    def datumStartEnergielevering(self):
        """De datum waarop de energielevering effectief aanvangt. Dit gebeurt zodra zowel de aansluiting op het DNB-net als het energieleveringscontract in orde zijn."""
        return self._datumStartEnergielevering.get_waarde()

    @datumStartEnergielevering.setter
    def datumStartEnergielevering(self, value):
        self._datumStartEnergielevering.set_waarde(value, owner=self)

    @property
    def eanNummer(self):
        """Uniek identificatienummer van de elektrische aansluiting, bestaande uit 18 cijfers."""
        return self._eanNummer.get_waarde()

    @eanNummer.setter
    def eanNummer(self, value):
        self._eanNummer.set_waarde(value, owner=self)

    @property
    def energieleverancier(self):
        """Leverancier van de energie."""
        return self._energieleverancier.get_waarde()

    @energieleverancier.setter
    def energieleverancier(self, value):
        self._energieleverancier.set_waarde(value, owner=self)

    @property
    def netbeheerder(self):
        """Lokale instantie die instaat voor het beheer van het elektriciteitsnet."""
        return self._netbeheerder.get_waarde()

    @netbeheerder.setter
    def netbeheerder(self, value):
        self._netbeheerder.set_waarde(value, owner=self)

    @property
    def referentieDNB(self):
        """De wijze waarop, de referentie waarmee de aansluiting gekend is bij de distributienetbeheerder."""
        return self._referentieDNB.get_waarde()

    @referentieDNB.setter
    def referentieDNB(self, value):
        self._referentieDNB.set_waarde(value, owner=self)

    @property
    def risicoAnalyse(self):
        """Document met de risicoanalyse."""
        return self._risicoAnalyse.get_waarde()

    @risicoAnalyse.setter
    def risicoAnalyse(self, value):
        self._risicoAnalyse.set_waarde(value, owner=self)
