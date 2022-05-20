import os
import unittest
from unittest import mock
from unittest.mock import patch

from OTLMOW.ModelGenerator.OSLOCollector import OSLOCollector
from OTLMOW.ModelGenerator.OSLODatatypeUnion import OSLODatatypeUnion
from OTLMOW.ModelGenerator.OSLODatatypeUnionAttribuut import OSLODatatypeUnionAttribuut
from OTLMOW.ModelGenerator.OSLOInMemoryCreator import OSLOInMemoryCreator
from OTLMOW.ModelGenerator.OSLOTypeLink import OSLOTypeLink
from OTLMOW.ModelGenerator.OTLUnionDatatypeCreator import OTLUnionDatatypeCreator
from OTLMOW.ModelGenerator.SQLDbReader import SQLDbReader

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class UnionDatatypeOSLOCollector(OSLOCollector):
    def __init__(self, reader):
        super().__init__(reader)

        self.unionDatatypes = [
            OSLODatatypeUnion('DtuLichtmastMasthoogte',
                              'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuLichtmastMasthoogte',
                              'Union datatype om een standaard of afwijkende masthoogte te bepalen.', 'Masthoogte', '', '')
        ]
        self.unionDatatypeAttributen = [
            OSLODatatypeUnionAttribuut('afwijkendeHoogte', 'afwijkende hoogte', 'De afwijkende hoogte van de mast in meter.',
                                       'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuLichtmastMasthoogte', '0', '1',
                                       'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuLichtmastMasthoogte.afwijkendeHoogte',
                                       'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInMeter', 0,
                                       '', 0, '', ''),
            OSLODatatypeUnionAttribuut('standaardHoogte', 'standaard hoogte', 'Bepaling van de standaard hoogte van een mast.',
                                       'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuLichtmastMasthoogte', '0', '1',
                                       'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuLichtmastMasthoogte.standaardHoogte',
                                       'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLichtmastMasthoogte', 0, '',
                                       0, '', '')
        ]

        self.typeLinks = [
            OSLOTypeLink("https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInMeter",
                         "OSLODatatypePrimitive", ""),
            OSLOTypeLink("https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLichtmastMasthoogte", "OSLOEnumeration", "")
        ]

        self.expectedDtu = ["# coding=utf-8",
                            "from OTLMOW.OTLModel.BaseClasses.AttributeInfo import AttributeInfo",
                            "from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut",
                            "from OTLMOW.OTLModel.Datatypes.KlLichtmastMasthoogte import KlLichtmastMasthoogte",
                            "from OTLMOW.OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter",
                            "from OTLMOW.OTLModel.Datatypes.UnionTypeField import UnionTypeField",
                            "from OTLMOW.OTLModel.Datatypes.UnionWaarden import UnionWaarden",
                            "",
                            "",
                            "# Generated with OTLUnionDatatypeCreator. To modify: extend, do not edit",
                            "class DtuLichtmastMasthoogteWaarden(AttributeInfo, UnionWaarden):",
                            "    def __init__(self, parent=None):",
                            "        AttributeInfo.__init__(self, parent)",
                            "        UnionWaarden.__init__(self)",
                            "        self._afwijkendeHoogte = OTLAttribuut(field=KwantWrdInMeter,",
                            "                                              naam='afwijkendeHoogte',",
                            "                                              label='afwijkende hoogte',",
                            "                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuLichtmastMasthoogte.afwijkendeHoogte',",
                            "                                              kardinaliteit_min='0',",
                            "                                              definition='De afwijkende hoogte van de mast in meter.',",
                            "                                              owner=self)",
                            "",
                            "        self._standaardHoogte = OTLAttribuut(field=KlLichtmastMasthoogte,",
                            "                                             naam='standaardHoogte',",
                            "                                             label='standaard hoogte',",
                            "                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuLichtmastMasthoogte.standaardHoogte',",
                            "                                             kardinaliteit_min='0',",
                            "                                             definition='Bepaling van de standaard hoogte van een mast.',",
                            "                                             owner=self)",
                            "",
                            "    @property",
                            "    def afwijkendeHoogte(self):",
                            '        """De afwijkende hoogte van de mast in meter."""',
                            "        return self._afwijkendeHoogte.get_waarde()",
                            "",
                            "    @afwijkendeHoogte.setter",
                            "    def afwijkendeHoogte(self, value):",
                            "        self._afwijkendeHoogte.set_waarde(value, owner=self._parent)",
                            "        if value is not None:",
                            "            self.clear_other_props('_afwijkendeHoogte')",
                            "",
                            "    @property",
                            "    def standaardHoogte(self):",
                            '        """Bepaling van de standaard hoogte van een mast."""',
                            "        return self._standaardHoogte.get_waarde()",
                            "",
                            "    @standaardHoogte.setter",
                            "    def standaardHoogte(self, value):",
                            "        self._standaardHoogte.set_waarde(value, owner=self._parent)",
                            "        if value is not None:",
                            "            self.clear_other_props('_standaardHoogte')",
                            "",
                            "",
                            "# Generated with OTLUnionDatatypeCreator. To modify: extend, do not edit",
                            "class DtuLichtmastMasthoogte(UnionTypeField, AttributeInfo):",
                            '    """Union datatype om een standaard of afwijkende masthoogte te bepalen."""',
                            "    naam = 'DtuLichtmastMasthoogte'",
                            "    label = 'Masthoogte'",
                            "    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuLichtmastMasthoogte'",
                            "    definition = 'Union datatype om een standaard of afwijkende masthoogte te bepalen.'",
                            "    waardeObject = DtuLichtmastMasthoogteWaarden",
                            "",
                            "    def __str__(self):",
                            "        return UnionTypeField.__str__(self)",
                            ""]


class TestOTLUnionDatatypeCreator(OTLUnionDatatypeCreator):
    def __init__(self, collector):
        super().__init__(collector)


class OTLUnionDatatypeCreatorTests(unittest.TestCase):
    def test_InvalidOSLODatatypeUnionEmptyUri(self):
        collector = OSLOCollector(mock)
        creator = OTLUnionDatatypeCreator(collector)
        osloDatatypeUnion = OSLODatatypeUnion(name='name', objectUri='', definition='', label='', usagenote='',
                                              deprecated_version='')

        with self.assertRaises(ValueError) as exception_empty_uri:
            creator.CreateBlockToWriteFromUnionTypes(osloDatatypeUnion)
        self.assertEqual(str(exception_empty_uri.exception), "OSLODatatypeUnion.objectUri is invalid. Value = ''")

    def test_InvalidOSLODatatypeUnionBadUri(self):
        collector = OSLOCollector(mock)
        creator = OTLUnionDatatypeCreator(collector)
        osloDatatypeUnion = OSLODatatypeUnion(name='name', objectUri='Bad objectUri', definition='', label='',
                                              usagenote='',
                                              deprecated_version='')

        with self.assertRaises(ValueError) as exception_bad_uri:
            creator.CreateBlockToWriteFromUnionTypes(osloDatatypeUnion)
        self.assertEqual(str(exception_bad_uri.exception), "OSLODatatypeUnion.objectUri is invalid. Value = 'Bad objectUri'")

    def test_InvalidOSLODatatypeUnionEmptyName(self):
        collector = OSLOCollector(mock)
        creator = OTLUnionDatatypeCreator(collector)
        osloDatatypeUnion = OSLODatatypeUnion(name='',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuLichtmastMasthoogte',
                                              definition='', label='', usagenote='',
                                              deprecated_version='')

        with self.assertRaises(ValueError) as exception_bad_name:
            creator.CreateBlockToWriteFromUnionTypes(osloDatatypeUnion)
        self.assertEqual(str(exception_bad_name.exception), "OSLODatatypeUnion.name is invalid. Value = ''")

    def test_InValidType(self):
        bad_Union = True
        collector = OSLOCollector(mock)
        creator = OTLUnionDatatypeCreator(collector)
        with self.assertRaises(ValueError) as exception_bad_name:
            creator.CreateBlockToWriteFromUnionTypes(bad_Union)
        self.assertEqual(str(exception_bad_name.exception), "Input is not a OSLODatatypeUnion")

    def test_DtuLichtmastMasthoogteOSLODatatypeUnion(self):
        collector = UnionDatatypeOSLOCollector(mock)
        creator = OTLUnionDatatypeCreator(collector)
        DtuLichtmastMasthoogte = collector.find_union_datatype_by_uri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuLichtmastMasthoogte')
        dataToWrite = creator.CreateBlockToWriteFromUnionTypes(DtuLichtmastMasthoogte)

        self.assertEqual(collector.expectedDtu, dataToWrite)

    def test_WriteToFileDtcAdresOSLODatatypeUnion(self):
        file_location = os.path.abspath(os.path.join(os.sep, ROOT_DIR, 'src/OTLMOW/InputFiles/OTL 2.3.db'))
        sql_reader = SQLDbReader(file_location)
        oslo_creator = OSLOInMemoryCreator(sql_reader)
        collector = OSLOCollector(oslo_creator)
        collector.collect()

        creator = OTLUnionDatatypeCreator(collector)
        DtuLichtmastMasthoogte = collector.find_union_datatype_by_uri(
            'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuLichtmastMasthoogte')
        dataToWrite = creator.CreateBlockToWriteFromUnionTypes(DtuLichtmastMasthoogte)
        creator.writeToFile(DtuLichtmastMasthoogte, 'Datatypes', dataToWrite, '../../src/OTLMOW/')

        filelocation = os.path.abspath(os.path.join(os.sep, ROOT_DIR, 'src/OTLMOW/OTLModel/Datatypes/DtuLichtmastMasthoogte.py'))
        self.assertTrue(os.path.isfile(filelocation))
