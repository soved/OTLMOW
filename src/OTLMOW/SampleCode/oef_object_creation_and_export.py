from datetime import datetime

from OTLMOW.Facility.EMInfraImporter import EMInfraImporter
from OTLMOW.Facility.OTLFacility import OTLFacility
from OTLMOW.Loggers.ConsoleLogger import ConsoleLogger
from OTLMOW.Loggers.LoggerCollection import LoggerCollection
from OTLMOW.Loggers.TxtLogger import TxtLogger
from OTLMOW.OTLModel.Classes.DNBLaagspanning import DNBLaagspanning
from OTLMOW.OTLModel.Classes.EnergiemeterDNB import EnergiemeterDNB
from OTLMOW.OTLModel.Classes.HoortBij import HoortBij
from OTLMOW.OTLModel.Classes.Voedt import Voedt

if __name__ == '__main__':
    logger = LoggerCollection([
        TxtLogger(r'C:\temp\pythonLogging\pythonlog.txt'),
        ConsoleLogger()])
    otl_facility = OTLFacility(logger)

    # use the generated datamodel to create instances of OTL classes
    dnb = DNBLaagspanning()
    dnb.naam = 'A0024'
    dnb.toestand = 'in-gebruik'
    # dnb.toestand = 'foute toestand'  # raises ValueError
    dnb.assetId.identificator = 'eigen_Id_voor_A0024'
    dnb.eanNummer = '541448860003995215'
    dnb.adresVolgensDNB.gemeente = 'brasschaat'
    dnb.adresVolgensDNB.postcode = '2930'
    dnb.adresVolgensDNB.straatnaam = 'Bredabaan 90'

    meter = EnergiemeterDNB()
    meter.naam = '50004784'
    meter.assetId.identificator = 'eigen_Id_voor_50004784'
    meter.aantalTelwerken = 1
    meter.geometry = 'POINT Z (157696.6 219065.5 0)'

    voedingsrelatie = Voedt()
    voedingsrelatie.assetId.identificator = "A0024-50004784"
    voedingsrelatie.bronAssetId.identificator = 'eigen_Id_voor_A0024'
    voedingsrelatie.doelAssetId.identificator = 'eigen_Id_voor_50004784'

    importer = EMInfraImporter(cert_path = 'C:\\resources\\datamanager_eminfra_prd.awv.vlaanderen.be.crt', key_path = 'C:\\resources\\datamanager_eminfra_prd.awv.vlaanderen.be.key')
    asset_id = importer.get_asset_id_from_uuid_and_typeURI(uuid='43e9c946-ca49-44b3-8ce3-46de0ec12489', typeURI='https://lgc.data.wegenenverkeer.be/ns/installatie#LS')
    ls = importer.import_asset_from_webservice_by_asset_id(asset_id)

    hoortBijrelatie1 = HoortBij()
    hoortBijrelatie1.assetId.identificator = "A0024-LS"
    hoortBijrelatie1.bronAssetId.identificator = dnb.assetId.identificator
    hoortBijrelatie1.doelAssetId.identificator = ls.assetId.identificator

    hoortBijrelatie2 = HoortBij()
    hoortBijrelatie2.assetId.identificator = "50004784-LS"
    hoortBijrelatie2.bronAssetId.identificator = meter.assetId.identificator
    hoortBijrelatie2.doelAssetId.identificator = ls.assetId.identificator


    lijst_otl_objecten = [dnb, meter, voedingsrelatie, ls,hoortBijrelatie1, hoortBijrelatie2]

    # encode to a json representation
    encoded_json = otl_facility.encoder.encode(lijst_otl_objecten)
    print(encoded_json)

    # write the json file
    filepath = f'Output/{datetime.now().strftime("%Y%m%d%H%M%S")}_export.json'
    otl_facility.encoder.write_json_to_file(encoded_json, filepath)

    otl_facility.visualiser.show(lijst_otl_objecten)
