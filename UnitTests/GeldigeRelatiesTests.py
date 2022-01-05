import unittest

from ModelGenerator.BaseClasses.GeldigeRelatie import GeldigeRelatie
from OTLModel.Classes.Aftakking import Aftakking
from OTLModel.Classes.EnergiemeterAWV import EnergiemeterAWV
from OTLModel.Classes.Voedt import Voedt


class GeldigeRelatiesTests(unittest.TestCase):
    def test_GeldigeRelatieAttrOk(self):
        instance = GeldigeRelatie(EnergiemeterAWV, Aftakking, Voedt)
        self.assertTrue(instance is not None)

    def test_GeldigeRelatieAttr2Fout(self):
        with self.assertRaises(TypeError):
            GeldigeRelatie(EnergiemeterAWV, Voedt, Voedt)

    def test_GeldigeRelatieAttr3Fout(self):
        with self.assertRaises(TypeError):
            GeldigeRelatie(EnergiemeterAWV, Aftakking, Aftakking)

    def test_GeldigeRelatieAttr1Fout(self):
        with self.assertRaises(TypeError):
            GeldigeRelatie(Voedt, Aftakking, Voedt)
