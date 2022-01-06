from abc import abstractmethod, ABC


# Generated with OTLClassCreator. To modify: extend, do not edit
class Verankering(ABC):
    """Abstracte voor verschillende soorten ankers waarmee objecten aan elkaar gefixeerd worden. Ankers worden typisch vastgezet in een of alle betrokken objecten."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verankering"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
