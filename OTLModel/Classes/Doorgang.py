from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlLEGCOpeningType import KlLEGCOpeningType


# Generated with OTLClassCreator. To modify: extend, do not edit
class Doorgang(AIMObject):
    """Doorgangen voorzien een vluchtmogelijkheid. Deze bezitten dezelfde akoestische kwaliteitseisen als de voorgestelde schermen."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Doorgang"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
