from OTLMOW.Facility.AgentCollection import AgentCollection
from OTLMOW.Facility.FileFormats.EMInfraImporter import EMInfraImporter
from OTLMOW.Facility.OTLFacility import OTLFacility
from OTLMOW.Facility.RequesterFactory import RequesterFactory
from OTLMOW.Loggers.ConsoleLogger import ConsoleLogger
from OTLMOW.Loggers.LoggerCollection import LoggerCollection
from OTLMOW.Loggers.TxtLogger import TxtLogger
from OTLMOW.OTLModel.Classes.HoortBij import HoortBij
from OTLMOW.OTLModel.Classes.Wegkantkast import Wegkantkast

if __name__ == '__main__':
    # create the main facade class: OTLFacility
    logger = LoggerCollection([
        TxtLogger(r'C:\temp\pythonLogging\pythonlog.txt'),
        ConsoleLogger()])
    otl_facility = OTLFacility(logger, settings_path='C:\\resources\\settings_OTLMOW.json', enable_relation_features=True)

    input_uuids = ["00b3dcd1-eeda-44d6-b3bb-fe16470015d9","01b867eb-585e-47e1-9045-37ccee706e58","02a4f3d2-4237-4dad-88ac-c94c2fc07c2a","03193cb9-ce79-4bd0-89ab-0dd542499b7b","031dadaa-519d-4ccc-b3f3-17de77ba93c5","0325dc53-27d4-4ebb-bee1-bc3eb288a8b8","04b577f6-22e0-4618-a524-afded60529b2","04ba8233-0224-4fc8-84e0-fbd64502e537","04ce20d5-4839-4eea-905a-eb82e70b68d3","04e0814a-135b-44e7-9f73-6eca96930282","05a155e9-f627-46fd-bcb7-42c3702233ae","05efc4e9-01e9-4955-af78-b68f6c9c37a4","065ffa2c-f7ba-4be2-9421-41f4523e1f87","0681a15a-911a-4270-a1cc-5649a34686e8","06b45a32-99c2-4e78-8f46-22b23ccbda99","06f3507d-b17b-4c5e-b499-f943f88e680d","0739a87b-d223-45a1-9c80-c8beb02fe728","078b19b1-38ec-408e-a18d-1d837a2e9328","0791dfa5-360a-4b20-94f4-898b77eee73a","07b436c7-308b-45c3-acf3-72e255a11a2d","07cdad23-9945-44c1-8c35-0a59ab0fcfc7","080697a4-fd1d-4349-9652-65ed7bfca642","083d6f3b-24cd-4755-a6b5-afe87dda517c","08cfabb0-1f5f-4e52-98c3-f52c97aba7c6","08d52c2c-14fb-4347-92af-db0cc6e1ad9c","093bbb74-ded0-4946-b580-fa321a5d8819","093fd505-93cc-40ea-aa59-21d8d23eb6e6","095b2a1a-1ba4-46a6-ac61-19b6dae053ab","0963d124-9cbc-4a71-b521-86336d232c89","09a804c5-3b32-43cb-92f8-df089d4b0f51","0a3738ba-eceb-4804-85bf-e0181228174a","0a4b8efc-e12f-487d-b85c-db8eddbad6e0","0a80412d-5603-4e45-b40f-ee36fe4f0d9c","0b176bda-7370-470a-bfb4-f68a1f221c99","0bf3cb56-3ae2-4700-aa9b-15ec74b95105","0c931639-c7d1-421c-a3db-9237b4951d74","0e1bb1fb-183f-4d47-b5a9-b1087a6d57bd","0e65826d-01f7-4b9a-bd6a-6c0f2068e86c","0e8a3f55-fbe2-47f4-bfb0-e09517480ff3","0eca5534-6a7b-4a66-90e0-3df860882b23","102f4afe-1d46-4f20-9e82-b7629e16393d","10a53434-ed95-4a6f-96d0-5986764474fd","1146f59c-6d38-42c1-b712-9dce54970d9c","11ba4d2b-9367-4c5e-9946-9fdfa6144d52","123e5c5f-1a49-482a-a4bf-47544520dadb","1244e25c-520f-4de1-aa4b-407e8edf8552","1250ab56-61bd-4580-a73f-1a99dcbfac86","136f915a-91dd-4653-b070-5fab912228ef","14c17ac0-d707-4de1-a88e-37e6c674a64a","150e9ace-4b95-4b6a-8dd8-5669f66ca389","153085a5-cde6-4051-b9d7-226b1d0fd652","15ad0fea-0376-4d53-b08a-c9ef7b98ba3c","160eac95-9c1a-424e-947d-938824ffbc8b","16247ce5-5e8c-45a6-bbb1-3dca2569312d","162e0067-3d1b-4db2-abb0-4d59d8b7b751","16613d80-427b-40dd-8dcb-0b5f8f47038a","169a7a7b-6bad-415b-8dc6-ad234d3d48ed","16ac822c-dd0f-4988-a9f8-1e35033df0c8","16ba6c35-550d-45bc-ae89-4e200c0211e3","16c8e29f-7ea5-4a39-b30c-bccae189a30b","17310edb-b286-434a-9a71-3d69bdfdf56c","17becd88-8253-45a9-96cc-2943a28fd4df","19c031ce-51c2-4cdb-899b-6d708a6ee054","1a5518f0-b699-402b-beff-fa556123820d","1aa067df-a9d9-4b5c-8f7a-ce5da0206756","1abbc5c4-6e1b-475b-8f2b-fc1d311eaddf","1b45a437-f1c6-4b47-b7fd-ec70a88191bd","1bc8d5da-4e16-4a77-9fb7-62230f90babe","1bff8209-4e55-4f43-a0d6-4aadeb5b946e","1c6b17c2-4919-4de6-9f45-b398c05f0da5","1c80713c-ba35-47d6-a515-631d18100a15","1c9f02c9-78b6-4a4d-999a-9c395fa42d68","1ccf6ff2-1879-431d-bda8-85cdc000fc2c","1d495c08-a21f-4cdd-8545-5b69d131f23e","1d6c9974-4dd7-49bb-b334-81817c8d3f50","1df3b3b7-4b3b-4526-8236-2a3ea506b31c","1e4b9303-9d05-45ca-bf56-c5d8a7a6e645","1e6a6c58-c4a5-4d50-82c2-466f18a9e60a","1eee7bf5-33a2-4619-a290-948bb595008f","1ffa58be-cc70-4a12-baa5-494ef6cb6056","1ffb6d0f-b075-40b8-b72a-daa6bf776d1b","20c2f90c-3c50-4ce5-8305-73f96b3df1f9","219843cc-f43b-42db-84ed-3508d81ffd16","2251a9d9-3bb6-4b30-b284-5f93aca89767","23519a3f-b28e-4e3e-9b90-0290457b2e31","23851d08-572d-4c78-8f06-c668632fbf27","2444dd79-7221-43ce-ab3b-42af3b41dcb1","256e6eeb-54d6-454a-a706-d826f4684d30","25a1c9bf-b54e-4167-b00c-cd9b0c1ccbc4","25e8cfd8-7eb8-47d1-9ed7-52fcb63ec2f7","2639319f-aa8d-41fc-8c26-4c53a338c629","266c3c96-2f00-4a85-a3ec-3327379ef97f","272654dc-0a6a-4eee-9e2c-e05dd83434a2","277a4b2c-5d80-44a6-b64e-64bb0e7848a2","285020a5-96e3-4bc6-a3ee-c6c98b5b0318","287929a7-126e-4bb5-bbb0-1274d47f10d1","29703c53-d939-42c0-af63-d129102c5e0a","29f0c6fc-03d2-45ca-ac8f-5658b2989970","29f7f7e7-8fcd-40c3-9199-c58360b42598","2a98fbe4-bcfc-4ff8-b84d-1229ba9d5251","2abbfae1-c455-4feb-b134-a216129f5057","2ae93cc4-496c-457f-ac9f-1906ca80aaf7","2b916b68-7d90-4423-9392-e745af4c8263","2b9e0e40-891f-4714-8f43-7784f00e0d8b","2bc4ef36-179c-44f2-bb2d-8b94f4ab8c3c","2c011f5e-c8ea-4417-92ae-e5807e8c9ba8","2c2c121c-40b6-404b-a875-3c4ef55a0bc1","2cb03822-0915-4f9e-8ae3-9d8bed32fb46","2cb849ba-22f5-40b4-a66d-aa198e3a9144","2cf4876f-4d55-4881-a0e4-f71010eed8f8","2d115294-4400-474f-87a0-881ba487bd6a","2d240c8a-0d85-480b-addd-54e54a526d39","2d573946-5532-47e6-93da-64e151a5daee","2df4ca22-8062-4d69-b504-dfb9fe8f3519","2e6a0d6c-d58d-493f-aa7c-cc274817b8e6","2e85d7a2-acec-4e15-847a-f5ba3e31bd45","2ebd0b99-bb1b-4d21-94a1-314fde1aa7a7","2ed9b285-13f9-409a-ada8-c96f280f65b2","2f2bcac0-62a8-4dd1-9bc1-ed65472ff392","2fa290b7-a0b8-4e8a-aa99-40772d6458c9","2fec3b26-ceec-44ef-a88c-e27358fe1d0f","30251b0c-e19b-4318-ac22-f085a9045ec6","30252945-57c3-46fa-9b04-e01397f1b231","304b4f9a-7494-47fa-be5b-b8e6d02540f3","30de8da2-0f7d-4dc6-a84c-4dbcaf21760a","3103f5a1-17b0-4df9-800e-ab95adc37516","3189b5d2-89cc-4aa6-ba8b-4e22d4f07870","3286a13f-5b7a-4eb6-b8be-7b97ba55d51b","335b3bb9-d8da-448e-84e5-f5065268e21e","33bfdeb7-e1a8-4121-904e-a121e98a4601","3403861c-3594-4022-98b0-89916f769fa6","34596e03-0aca-4ecf-b088-5c00d51cc38b","34fb5387-f18f-485f-843b-100bad9d8c78","36163ac9-445c-4090-8881-a3ad6bb437a5","367516ca-469e-4b23-8e04-ca2ee9e20c64","373dff72-8c19-4ac1-85d5-6a85561ea391","3777be2f-9344-4ba9-8f09-75dffdaab052","3927e441-d0f0-40d1-8215-bf42985be2ac","393d79b6-6dd2-40bf-9460-a81853679c86","39f1a463-6290-4500-ba45-62aaeb866da9","3a2739c6-3387-40a7-9758-57f68c4a1cd6","3a965e89-d8bb-4e17-9d79-308598d79191","3a9be0ea-80fa-43e2-936c-2ac068c06b74","3aca9e23-19b5-4cea-a143-7d2eab7e69e4","3b2cc7f1-39d6-4389-a944-752071de835d","3b33f35d-61b4-4c2a-a396-1ea5d0285a59","3b916d19-4321-450d-99a1-64f99a0cb8e5","3bb6c679-f0fa-43f2-8e04-f017a0027344","3c0ed01c-256d-4f84-ac59-784e5192cd05","3d8fa8eb-ad78-4e69-8926-cbb55d08f66f","3dc17a21-b96f-4360-b28d-22043d2fc771","3dd6d053-d956-4a31-9e5f-a462fae2fb26","3ea631a5-4497-4a5d-b7ad-6b14f0cb9e4d","3ec2bee1-0ee7-44a6-be26-4cf803693557","3ef2eac5-8a03-421b-93e6-717b0087c0d7","3f431c39-95ec-4951-bf88-c8d39913aa8d","3fccb8be-6539-4e0c-86a4-aa13c7afb0a2","4015cb7a-03ab-4e73-a76f-196060513099","40522802-adcd-456a-a9e7-ffc8748875ff","4060cb57-8601-406d-b842-04e19d34a132","40a76910-42f1-40e2-8f83-39b1321b612e","40af5f93-f79c-4161-b023-c9613be68600","41286f92-183a-4071-9e48-9f038f94ad76","414e9ba2-f509-493d-8d5d-ce70002ffcbd","41c97132-c819-4913-98f1-d522106f7f72","42c210c0-55a9-4833-b19c-699a8fcfb563","42cb4d61-ec4d-4b86-ad0f-59e346f80200","43028655-5b89-40f9-a292-2677388f2bba","43086033-fef5-480d-bec0-615f90ea1499","434058f6-4a2f-48b8-9eb2-69161dcf61e8","43af73af-bfd5-4848-b32e-583305063839","446f4fb1-9856-4964-804b-bc7137e48536","44bfb5a1-b1fe-46f0-bd0f-bed720ba5a77","450014de-f74e-4025-8074-03ddd86d893b","460939fe-0eb1-4e5f-9341-86ca88241430","4639c86a-0680-4ec6-b54a-7053cdff6e2b","464ec29a-eff0-4c11-b7d0-d91aab67370f","4666baf0-4548-4e02-a455-d149b14db971","46d126ba-91c1-45a8-ba2b-ae309a14a61f","483d0850-d401-483a-9626-58b046f99bc1","4891486a-a51c-4991-9618-561f87ebaf72","48a37ac4-c848-41cd-9753-8fe41cb62a57","497ce41e-aff6-4581-b09b-0afd5e2f48c1","4a36366e-2ede-4f8f-82a2-8c1227b96ab3","4a3a75f2-1684-495b-8a83-88c41a928cb7","4bf1473b-4f58-4c9b-ad1a-ceaf0721a811","4c4a200c-6608-41ae-a09b-b62d192372fe","4ca8eae4-d2f6-49ab-8bf5-cd4a300b4ed8","4cc3df26-f030-41a5-b43d-5d1c40efae07","4d31fb0d-5534-4ffa-936a-4d69feb331e2","4da51942-b4a2-49f3-a13a-84fb7a8594b5","4e99baba-8f51-4ff1-ae9d-4ffd80181229","4edfaba6-c3f2-4726-91a9-c5941d28ee82","4fc3ab26-72ee-408d-9117-0720d66a0837","4fd0f9d4-32a4-4191-9705-77914d375a0b","4fe2867c-598f-4347-923e-76a931975723","5093ee92-11c8-44f6-a523-a45231a2e53c","518a2260-2bca-42a3-bd0e-5c9f986ac43c","51b3a097-c20d-46f5-bd04-bd314782cf90","52a7ecce-7420-4bd5-a731-3f9d59627e1d","536a9db4-3f58-45ef-b053-4d402b6e53d4","53fa8ba9-676c-4d1d-bd8c-00e9a87e38f3","5434ff34-9649-4a0c-a13d-d61826c3d219","54835aa9-170d-462d-9bb8-9274ae796c7e","54ef9310-801c-4857-9c36-3696569f18f7","55e3186c-4110-4f50-b8fd-94e83606f687","55f94424-f503-41c4-a0bd-055030f69bda","5605d45a-50d6-40aa-93f0-b844f843b89c","56b84066-355e-4c54-80ca-8d1dc91a5665","56c35cfc-cc72-47be-b0c3-d372145761ce","572ea77e-76ed-4ebc-b5d2-be45937a73b3","575cda79-54b0-4683-a215-de1bcd16e329","581efdbd-f2d4-420c-8404-b3208a4ce679","582e18d7-2f38-4ee7-bbad-34cc3f2c2341","58a89c52-7e83-4563-8b24-adf4edae6435","5900a9a6-490f-4807-8557-8097228c9f1e","5962583f-105e-4f07-b215-352a8e135180","596ed135-9ce0-4659-b202-c6e9fed6ae42","59a1ab41-2d77-467f-a5ba-29a051003fdc","5a02c856-59f4-4aa7-927e-7837c4fbc662","5a500827-21e9-4e8c-b51b-5ccbb8e489b4","5b6083b0-68d2-4242-8ada-20cd16cc4e6b","5c70867f-4f70-4e50-b564-6eb5017bb3a3","5cf9d714-7c1c-4711-8126-ab66684fd6ae","5d0ea980-196b-490e-9364-5cd3535981ef","5d690e71-9349-46fd-beff-d0007b553546","5dbbe57a-c39e-4c20-93c5-f9f4446ac857","5deef64a-832e-470e-92a5-e7f4107691e8","5ede116f-4649-4008-9df4-506207483483","5ee5fb30-9027-4d1a-bb79-dbb2ce5cfb0c","5f464b16-5f30-41ee-9fc6-2c13cc8368be","5f4e28cb-8645-47da-bae6-cc9cfa7302c5","5faa1d11-b7c4-45b9-b9ec-953c3a308b55","60d17ae8-c7db-49f3-81db-c8bdbf942814","61c4cb37-a5ac-4321-bd71-594080d67fc6","61d46ade-aaee-4ede-9948-96b263635b30","61f3b49d-8610-4552-9085-6f6cfae44b23","62125233-a980-44e8-8cad-d60d996fa04b","6296fec9-1d4f-4112-8def-6aeb91bb9841","630fd861-2233-4c05-bc72-8c1358ec8113","639757c5-3b1d-434b-a0fd-058febc5698b","63b0ad0e-5eb6-457a-a3e2-5d75c67f77c8","63cc0adf-a0e2-4929-b9db-1e6516c7180b","6405dc91-f917-4792-adb0-080cdf415752","641440b0-831c-4c18-b2cf-f44d5600a8b7","6546f681-1992-4348-a6c0-0059cb0b13ee","659a186c-dcec-431e-a4fb-40af26792424","65de197d-31ad-4e24-a8e3-aa22ae0987b9","6653ef1a-50ff-4dcc-aa4f-ea60cea4ada5","6723fadf-e16f-4312-bd1c-b2cdf2825133","6884eea2-1016-473b-8bea-f54e35c9fef3","689c01bd-6f06-4d26-8c0f-85ddb0f0fd38","696e9d77-3c60-487a-a6ef-a40793ebed54","697d0280-ce1a-4573-9123-0e742a9fcb12","69907b38-8127-4a84-bb03-f63091b91537","69dafbca-3b8d-44c5-9475-b9455c20d6e4","6a184504-4fe3-4858-998e-b806410fef10","6a489c94-dfc2-492e-b815-4e17f532b0a5","6a7b8a16-92ea-4cc1-b104-8817fee1f643","6b49059f-290c-467c-924a-22aae95a023f","6b8dd4a4-3508-40a1-aaf0-c83fc07f31bf","6bca113c-a3c5-4fe9-a265-bbc47d37b635","6d8810bd-422d-4f53-8814-17666043e1a7","6db667ca-66f9-4deb-8c99-e1c9bc5d4874","6dd330b9-c6f7-4dee-b8cb-c9f4ebaffd66","6e7e1dbe-59ff-498d-ae29-d64ca06be6cf","6e8a0189-e424-4bcc-9125-0b4a2146c4e5","6ecc0667-d6ff-487e-a646-e7493f74a542","6ef5530e-9ff6-448a-b0fe-75e04e730d53","6f09f5dd-8cd8-4cea-b865-2329f24c99a9","6f566d91-390b-4a58-b55c-75e969adfa3f","6f934cb0-3680-4074-840d-69b2c718dbb6","6fd32bf8-c1d1-4196-999c-d5cd71c7fb01","7020e4db-17f5-4fc7-9bdb-7f5c21c29842","704c91c7-3f3f-493a-bc5b-0f47dd7717d8","70c40f07-7cff-47e3-9fbd-3c48044ed425","711557ea-97a5-4e47-8060-b3b42932e306","712ac449-7146-4c40-abe3-452e4ab12926","72be5e3b-fbb8-45a7-aa2f-586d62e95531","73458884-4558-4bbf-9331-03aeed77a847","7393feba-a359-410f-8acd-db80df3cf3ee","73ed455e-de7d-4e8c-bfc2-33d60b199e48","73fec9ea-49fa-40fb-9250-15140d3471b0","74232be0-65c6-4e6c-a36b-927c3c9d33f9","75843dcb-89be-44f4-af7a-7aa0b5b5d116","76a97b6f-bb39-4996-ae5b-2b4dd99a0cf6","76ab1ffe-8d46-4ed4-9069-ec8d77a243d8","76beab1d-72d7-4636-9281-6ca4940929a5","76f43a67-ce13-4fd7-bae9-47f534eca7c2","770b6480-4679-4215-8bdc-9cb4ddfe6092","777cc0ea-59df-4df8-91e7-81e58afc883f","78693578-1a3d-4415-a0de-12fdb86f1323","78b8b2d3-2eeb-4c83-908f-7a4656bdde16","78ddb1a9-579b-4d89-9d7e-40bd515ef4ab","790a3680-0726-4626-ab66-565e2d6b8a68","79bfc006-5c53-481f-9cd9-202df4360b3a","79fff9bf-1d93-4b5a-85b0-ca7a13ee9e60","7a3cf07e-9258-4539-a827-21c44195686e","7a8250d3-4a5d-4f23-989c-f1a10b76e5b7","7b643251-7b51-4231-bc9f-433dbc9481f1","7b87c568-259d-4b6c-bafb-4e8bac1a457c","7c88e20a-8d42-4eca-8f96-93f6e67cb96f","7c8c06e8-f1ae-4b01-ab96-b06f7bc0927a","7d112217-25bc-4268-ab71-23dccad29e85","7e613368-9fb7-4226-bb0b-e266c7a30c34","7f93a123-0d98-44f7-a7ec-b9dc9c31991f","7f9b4463-f223-4934-b5dc-6c64b5c2a2ff","80c5a5fa-15ee-4e33-bc48-de835d7ecbc9","80f5a4c3-f80e-49b8-820f-0d33f57fd117","81b78883-f643-4dd8-b456-bd477b25a0c1","81c3c0aa-a760-4b6c-a7a9-32ae5d9076fd","8225fa50-e3ec-4b48-bdcc-5750642f336e","827268cd-f3db-4a9b-896d-b42561f2ba0c","82ab9afd-c964-4bca-8689-e705d6571b80","83100cb3-da8f-4aa3-a709-65a701afdabb","83289817-37e8-4b9a-bf4e-b4036e89275b","83df2cbf-7b1e-483c-9154-b7242babccb2","85087e00-9d85-494a-8a10-972abdcd9421","853ee323-b300-48aa-a858-eb2f2102d244","857b4f2f-6ed3-46c4-93b6-15b4538890de","8622a8d0-aabd-452a-bbfe-c501f79d5721","86a9f41c-31ef-40bc-afd1-db758678d951","86e562df-8f0a-4a56-9279-db97d95ddc32","871903f4-110b-4e21-8ef6-6647d6c29914","8769f735-0ec5-45ae-b52d-720df29b6220","8782844a-c91b-4fc7-8739-7d496fd977d4","87f2d33a-6bbc-44d2-908d-548f9b3cecc5","881a9ce4-509b-4988-95e9-0fe403d45c12","883ad403-14f7-4b5e-82bb-1b1966a23c97","88f465ba-a09c-47df-8b34-9672c54f9c07","892805ac-f0f3-4673-82cb-43589d77f4c8","8952748d-73a3-4463-a30c-4b68b7f7fd8a","895f31f4-2055-4fe5-b485-c04566ddc6aa","89904ed0-1681-4b65-acbd-d02b490e6e62","89c3dd9b-be1f-47bb-82f8-96c3ae506bcc","8a6d6f17-1048-4b31-b1f7-b717457533a5","8b0c522e-9473-47df-8174-95fee69d46c7","8b3c1d88-e5a9-40dc-876c-28f68a840f51","8b3f6ced-4667-49a5-8bfb-595965ab7cf3","8b43f432-a422-4e7f-ba80-33fcb8830440","8c12abaf-8fa6-4837-944b-31c8466c2345","8c26d579-4a70-41cc-884a-b45c950bdabb","8dc50566-5d4a-49fa-bbe7-56e4a5612c04","8dfb4a2e-6e12-4fdb-a47c-c8c05b25a1ee","8e8e97e3-b566-4f05-895e-93aedad30f1e","8f3f1c70-4537-4746-85d6-956489723ff0","8f8a5416-f61e-4350-8195-18ef55f4b64f","8fecfc4e-f05a-4152-959f-02c3e0f20641","9044106b-c6cf-4cb6-bc8e-cc663214a892","905900b3-2858-4c7c-8904-6daf0e2c6cbf","906861b2-da43-4b86-8369-7ca27729b65a","906cedc4-3ddd-4dc4-a646-8be2e48780da","9095f8ff-203e-4993-9638-96e06665c089","90bc0c63-acee-4edd-aee8-af014c69f519","90e15e0e-ca2c-48ea-8900-1a2972eedbf9","90e8f692-ee08-4bea-990c-993226a0eb07","917b6c0f-5b94-4d22-944f-b1a5efdcb6cb","92477654-acbb-4496-a466-0377c9a31e0e","933a9ea1-3f29-41e3-8714-09b941cddb61","933d767c-9282-4020-b835-c824d3a34caa","934cb2dc-731b-413c-9602-896c7fa15be2","941d123c-ef15-40c5-be5f-1daa0238d7c6","942adc18-736f-4873-9d6e-45514fbe4a8a","94688691-20c8-4a8e-b8e1-a92928eb4c87","948e4ddf-5e97-4426-a3f9-bbdb4a5621e7","95761887-c2ba-448d-a85c-8d132270e30d","961af87e-6f00-4901-b56e-fda3873347dd","962a33f1-ecd6-41f3-a5ab-fbc13e012e4f","9657f5c8-4994-49d0-b890-9436de91f787","96dcd2b6-fd17-4a2d-81ab-0a7e10268a0c","97037771-fd49-41d7-a74d-d82e177f1f53","97155dd0-a539-43e3-9ab0-35817aad1eaf","978fad6d-8352-40d7-869e-92094815ac5a","9794bb6b-3c74-4df4-aa8e-08ff45c72288","97fcb999-069e-4c94-8213-e04e46718c88","98511889-f03e-461d-970d-6fc5dcd9adba","9888cd4d-3744-4a59-a33d-bb238d9dfecf","98d6d96c-50c7-4239-b63d-4ce7a8a696c0","99276ad6-5e43-4eb8-964e-e0794474b4f9","9966c086-9ab0-49eb-84e1-a7de99b68f3e","996a97a2-5e18-400c-8a98-ef5cfffc8021","996c80fc-1ffc-4a22-913e-35ccbc98d889","99b26f4e-5a6b-40ee-966a-fa2654de7fcd","99bfb5be-695e-46d7-aa75-7d325c8007fb","99fb96a8-7854-42a2-b983-be128327a586","9a03f40b-ee35-4a39-aafb-a132d67e9bf4","9a3b0bee-f130-431a-b0f8-b27df0d72923","9aed4120-7180-4f15-96c2-f6d5612bc72e","9c28333b-2598-411f-8f39-58b7eb3216ec","9c43dcc5-5175-4c7f-a5ea-7b2c20537899","9c63a051-fb41-4157-94dd-386d0883a1f0","9c9aeaae-4001-4b2b-aa3d-c56e2b2dc10f","9d4128f5-2aac-497c-abca-d131c26b2fd7","9d9ed37a-a095-4e20-a36c-d4b8b88e4eda","9e4369dc-a152-4630-b01a-bc4354b85744","9e805d31-b314-44f3-8fdd-d0d30d7748d6","9edad4e4-2b0e-46df-af03-7fe98fce4623","9eea5719-2834-4988-a204-41fdc740d8c7","9f0a4320-12a8-4a9a-9e9e-701576d2d9a4","9f146952-053e-4a8e-8396-f7412f80666a","9f33114c-234e-4df3-adc4-2162a3a234ed","9fd46628-c455-4e83-ac1f-755fb524957d","9fd5f70f-148a-42fc-abdb-f651eff0bc51","a00d3157-035f-4168-8098-3d5e34bd9896","a0a022ce-1143-4c49-a988-fda264164893","a1605242-61a2-4392-9d7f-d97d29dceb40","a1999503-4b1a-424d-8411-5467f8abd44b","a1dbe1e6-a2ba-46fa-8326-14502065c0f1","a1e78188-d479-43ae-8354-b096e889c25b","a1ef5043-c428-4928-ab15-917d87197765","a27dcdc9-66c3-4df5-a346-c9a0fc8c85e8","a2efe85a-4740-4306-b449-ac3ed64066f1","a33d8e18-814d-4669-87a2-941e4216e46b","a365da0d-cb92-46e9-84b3-af59b7369adf","a3bcb1c8-a342-40e0-837a-b20fe5a4a0da","a40ed02d-15e2-472a-9b4c-b936fddb9f4d","a4476641-e7f5-4634-a218-763cd3bca73f","a500c7fc-1165-4e1c-b683-59a361db40e9","a53307e3-ff53-41e3-a26f-0eed8a7af4a8","a54e462e-ff04-4fb7-a95f-ca1e38491593","a59053c5-9bac-45cc-86ac-0d4ea1f97896","a5c932a6-d33d-4e37-890b-c647ffd486c6","a5d13360-b734-4247-8a40-65ac0de1696c","a61e71bf-e88d-4d9c-a58c-f21dc8c372ba","a64772f0-79f0-4a59-bd90-feaf127b0a7f","a68a7a61-f2da-4d83-9e57-1e73d20e85ad","a6a4eabf-35f3-4f70-9b3f-309b9596fdd0","a6d84924-a795-4b15-9385-2c1b8280b791","a760805f-3f47-494c-8791-916a197d9391","a78601bd-769f-4a75-b2c7-c716cc817bd5","a7a9aeee-4383-4ea8-b25e-c27bf2462194","a8690254-a9d8-4169-9d25-a27f8013ba88","a880ad22-afe7-4a8c-b898-d9446e368af6","a9637316-220f-4ea3-81f8-7a2fc03118f6","a991aa6a-c9b6-484c-9a84-be1f05e5c9f0","a9f70623-79f5-4d8d-96c1-4ccf7774523b","a9f897a9-0778-4ef1-b281-d4e78f149d14","aa2daddc-fa7d-40fb-9f1b-f125c4834075","aa528fe2-5199-4482-bee4-56a158760209","aba0ad29-3234-408d-8b23-76915115654d","aba3acc9-6226-45b8-a4b1-cbd097c68329","ac3eeb16-3777-474f-a372-5067c3e6b472","acdca43f-7194-40a7-9fec-fd85c8d95c2d","ace4ae19-346a-466d-9d76-b2a1910a4e9f","adbe52b5-f95d-428d-997d-4eefbc1b4980","adc2f49c-fcbd-4644-a010-bce2b705068d","ae0140de-1631-4e78-90f0-72958ea77e04","ae6befb1-2717-43a9-8a29-6711ffe553de","aeaf5d82-45c9-4e79-a5f6-dceb6d6f6cca","aeb47066-013b-4f6f-8284-1b876bb657e5","aecd72e8-53a3-4d65-a9c4-2263a598b2e3","aef6f0e1-58a9-4a45-a215-db75947791c4","af0532ef-66e0-4a20-9e55-652ba455c6fc","af4a9280-9056-44bc-81b2-d4cd414a2595","afc2ecbe-18a3-4e38-ad99-1c5db53858c5","afc648c6-78eb-4195-a4f3-4a523a4195e4","b028f4c1-7549-489e-ae5a-dc0472132561","b0a1e3da-7e97-46c1-8f95-1921e77db726","b0dfd36d-4c6d-429d-8a86-42927dc18b53","b125ea39-9f19-4e88-8ede-d19b7b893d07","b1fcf3f3-5dea-4b84-a584-b88798738bec","b34a502d-31f8-48a9-9ea6-c22195391f37","b45ea482-0e60-494b-9434-af81af2c2b3d","b478ad41-636e-41a8-8202-ce7df6be3782","b4f9270e-5347-4b30-82c4-83a8f50e7da7","b6de4139-a289-4bc8-9d7f-38ac355cc851","b7104fea-6797-4cb1-b735-dc362db88f86","b797c89c-f63c-4fa5-a63c-bfb50e9c355a","b7ecf09c-e561-4f55-ae46-4be56ab89385","b8bd41da-69a0-45d1-a091-c06c5056bebf","b8c9eed9-0d90-4a22-b442-2a6c8c68354e","b8d831e8-0ff0-4651-b9d1-5b563873b292","b8e715ad-f4ba-43dc-bba0-483b5e48c3ca","b9330258-d6b7-4cd9-8b04-801799a4e488","b9f161d3-d051-44e5-8ff8-01dfcca86a37","ba40fe96-aaff-456b-b90a-419f728f4391","ba99e78c-76c6-4634-8744-bb71165fcf85","bb22b2ac-040c-431a-8726-cfd3d0bd7498","bb888c24-cacf-49ff-8187-d69480c9df70","bb95d336-83fd-4d63-b716-2101dd4d0247","bc031e22-323d-4cad-972d-97d6b4bc5bc2","bc741f51-816c-45eb-a66d-75858461b26e","bc7456e6-352b-4133-b2d3-cc562941b9b4","bc94d837-5d37-4da2-bc19-748f780bf214","bca6b101-c1bd-41a7-8bf8-2f39395b2bcf","bcac9a9c-e69c-44ce-9186-598e820329f6","bcbef677-e5c7-4a4c-a778-c9968e2e0a9e","bd361573-070e-4a6c-954b-531118b76a86","bd4481e9-d575-4562-af1f-b63e7e5a5c20","be0d3981-bab7-4ec9-af8c-5cce5a1e8f4c","be7aea5b-3923-4f03-9f6c-06ad982cdaf0","be8b64b5-9824-4e24-a0a9-b6d88b9e63f0","beba587f-4311-4340-9c4c-b777ec5d2fa8","bf13cadf-0576-4434-afa7-73bb02330994","bffc9985-2714-4666-968d-1ffdbd43ebb7","c032a12c-ca9c-42aa-8390-0515597eda02","c0db7563-9aab-4cdc-8348-2d89fe884a68","c151ab1c-94ae-4451-9fd5-552093684652","c15edf98-9ea3-48d8-b467-0b4944cd2906","c1786f0a-9214-4e06-8005-d890a12c8fb5","c1dad986-5585-4a09-8c02-1f38dbe434cc","c1eb9b64-f656-4bf0-b856-a8535aedd05d","c2037222-503c-4872-9fdd-664a49032177","c21c4bbc-efda-43aa-89b1-944ac294ae1c","c27fda2c-1220-4cb0-8fea-ab18bc017281","c2ba49f4-3b9f-43f5-a933-5a4a58bc9e50","c384c144-bd79-48b2-aff9-3b84745e0c3e","c392c134-a74b-4a6c-9a7c-6697817ed9f7","c3bf23f2-4c24-4c2d-904f-9bc86fbb5228","c3ce6c82-d172-4d98-90e8-cab23d20b34c","c4113d62-295c-4218-86ec-309354e55b4f","c45d5aab-974a-4ce0-b9fc-ff39a4ec7fd7","c488b553-692d-4c00-bac4-342ec3bb67fa","c4c12c06-4d6f-486f-9382-2ad60cdfbb37","c4fb8a93-7b8f-4769-ab09-6fba4d6344c7","c5acc077-bf9e-4b4d-8071-cba9197d4e88","c656aa72-3c1d-4573-b34d-0a9b3d85d552","c6c6445b-4496-4364-a41d-5093843367b5","c6e4d6a0-9cdc-4818-9c53-b14441ba39b7","c6fe7ff7-521a-4e28-83ef-ea4eb950f8ed","c749dd58-dc22-42f6-975e-037cb39e6eec","c7823d58-d240-4b97-bf7a-7aca0dcf1adc","c7cf1ff3-e45f-4b8d-a448-ecc0c12cd382","c96e1190-ac12-4c46-8fdc-cb20a7c2f013","c9965fb8-40ea-45e2-9200-d001d62d2b70","c9f2c2a9-782b-48aa-bf41-b6374118dbd4","ca07b864-6916-4589-88a5-e71cbbe75f31","caa4ccea-b798-4cac-b61c-d4ee8c935516","cb190b1b-d812-44c1-af9b-42d793b5482c","cbfa23f8-1091-4012-9664-6f283dc69e3a","cbfe9e6e-a87d-40a0-96c0-97d4fcdf50ee","cd0b213a-ee1e-459f-9c8c-a6bb96fbe410","cd1a767e-3b13-4d75-9f63-ca080bbccb78","cda0cd53-21b3-4bf9-adb3-220281af45a4","ce00c3a9-a79e-41a6-8590-7501dbfba22c","ce068c1f-3138-4149-9edf-f7c43902a84b","ce672e16-59b6-4b26-bd91-b1d4d39d9703","ce8626f3-6515-45e1-9368-1779b2b1d900","ce98f19d-01e7-4513-97a7-a11829be6424","cea51828-ea80-450b-82d3-8743ec2ceb0f","cf0e7fe9-3c15-4673-8be8-610459884817","cf43f9ac-fcf0-413f-994e-98960b2a3944","cf5f3430-bb9a-46bc-a917-db1a6f79fbc4","cfda0c80-a5a8-4537-bd75-a705c40f1079","d0a3b282-48f0-4729-89af-7a80af6a4d93","d13e312b-6f87-40f5-b91d-a6d52df3362d","d16e9480-df8d-4f3b-bd19-2676f228ee5b","d3419899-9c23-449a-bf66-dc5278aae6c5","d38fca55-c66a-4ea4-b821-29b79abfa09f","d44726c3-9fc9-452c-b108-52929f744e8b","d513d213-2b3b-40a3-8208-23152c15a947","d5715692-75f4-49ce-a240-df9eeaa8f10b","d59471c4-32c9-42d8-833e-c7d14075c2a2","d5980012-f7df-4a84-9a20-c57c947beb7b","d5b02a9c-198f-433a-bbae-6c7fdf5bf51d","d6196553-76a4-4e9b-a046-c6f354d127c2","d6c2aa2f-7aaf-44be-9fa8-79572929ed94","d6c73de7-1bec-4a5f-9a33-88aa1e4e392e","d6e753d6-9544-43d1-8279-020081f4dbcd","d7e18807-9fc6-4af5-94c1-764be366feb2","d8080d1e-60f3-4776-ae59-93f74518c08c","d89ec736-e279-4979-b358-5d33d637796d","d8c4a3d5-d675-408e-8cfb-9613583e81fa","d8d60d5d-a3c4-4f0d-90e9-c0263142fa89","d8dda513-ee97-42b4-9b63-5f0faec5b631","d8ef5497-9673-4b13-8a99-35eedc57afcd","d8f040e9-0f3f-49cd-ac07-554d925416a5","d98457f8-428f-4f88-9186-27fd2122345f","d9949b1b-d4b0-4b99-ac51-5d959f9839cd","d9c9d70f-985b-4f65-b362-cd8914762cca","d9e0b78a-be6c-4679-bab8-25b7502db180","da329ccd-e60c-4257-8058-9d110a0d89f1","da399092-b07b-4ac5-82cc-e2db84a18109","da7bdcaa-fcf5-41b4-a5cf-74de6f88bee9","db5cffb1-fdf5-4f52-b931-8391af1bfcab","dc3cc7a8-bd22-4e5f-85b3-cb3cb3465c4b","dc5caacb-be6e-4c4b-9239-4ce2bb643314","dc7bccf4-d86d-4173-99c4-26d73612de69","dcdce3a2-f916-4563-b406-d0a313ffd652","dd06e2c3-9ddc-427c-af15-43221016c953","dd5659f5-348f-4bcb-bf14-bdfa786195ee","dda9c7da-348f-4a56-a584-09e090341d28","ddc8b3d8-a59d-4888-9396-c8d1877f6976","dee0884c-ce58-4cdd-90c5-1a92f6454102","df1632e2-3f06-4c8c-9836-52e15b7b78db","df686bdd-98f3-41b0-94e6-d6fa5a39d5f4","dfc6da8f-9213-412e-8e16-e91584b6718a","e0123361-e488-4b7a-b3fd-fa20c24cfcbe","e017ccca-6406-4f3a-be58-bcca0a3fa2b0","e0c09811-addc-402e-85d7-b8f32f2d20ac","e0f59790-6283-460f-81e3-cba0b2e17913","e23bdaf0-7bc9-423f-8590-dbf151421211","e23dd7a7-3314-47b8-b14e-27d3d420dd48","e250db11-aceb-45a3-8dec-2272e123c16a","e29aa171-b039-4f99-946c-032c34b3df63","e2ab1dac-1032-4933-8a15-e70a6a449846","e2f05a1d-e2db-41c7-b51f-9951c361740e","e41c9179-a917-4cf3-96ab-fbb6428a7418","e45b294c-3d59-48d0-9ebe-67a511400f9e","e4796bd6-8f41-48fd-b716-c417fa4622ca","e4b78e9e-52e9-4738-80f6-00ac467b3917","e4e56f46-1548-4c58-8b66-6e0feef94e48","e57fa90e-7a32-4c5d-8ed2-d38a079bf92d","e593bb79-d2ba-4d27-b214-a55fb7a32add","e60b48aa-1525-4f34-9fd1-bffa81b359b8","e6149f48-55ba-4f1d-bea5-d8013660e078","e64cd6dc-26e9-4e66-8867-e542c72c9ca9","e7041fd5-b85c-4990-a294-f2084ba7aeab","e70f7e1e-d6b4-4e27-bf49-ec93eeb50fef","e7e7d3cf-5aba-4e0e-ab38-e0b4836c42e0","e83cf65b-f813-4206-be8a-f884fa861b3b","e865256b-d254-446c-81ea-8e892a7a4f31","e8771eb6-3fd5-47a3-915d-cb11605abb0f","e8bd2df5-f752-4183-9198-4f1dd84c30e0","e8ec7c59-883e-4e3a-a317-8202d5972d81","e9246090-583d-4ee1-9d02-07f37dd38f79","e9275877-009c-472f-b8ad-7ce239672a4f","e93ed10d-e8fb-4e5d-b709-41f68e26c4ef","e9cfff55-a924-454d-a373-be63b99968f1","e9eb6032-51b2-4fd5-b41b-7e0b5652569a","ea25ef7d-39a3-4888-b409-310ac08d953c","ea26e081-d820-46a6-87a6-5baecbac3f02","ea3d1f3a-c2ac-4340-802c-52c885b07d42","ead5ba54-8b4a-4e44-aee3-d73014b1864f","eb5d4c13-c8a5-4175-9b7f-9a4256d369cb","eb7c51b7-419d-4bfe-a009-beed9f4b4d9d","eb9c5a09-ccd8-4bbf-8d03-ede657f1b8f3","ebc65331-8a89-4414-999e-9d473dc0ee8a","ec056155-72d6-4efa-b156-2db0bdb99d7f","ecfcd01e-e099-4f24-afce-8ef9396c72f7","edb190ab-6998-459f-bd67-5f3c3abdbf96","edc1b776-6d48-4271-8e0d-b96021e54a52","ede1f137-8a8c-4290-9202-1d31921aa580","ee26da9e-4b42-4e85-bc67-6a7b8807f393","eed09ebe-5d31-4113-988b-60e10b09e789","ef451eb2-420c-42e4-96bd-176107bfe5d7","f028bffd-eaab-4c0b-a1e7-9bda21019844","f04330e7-7e50-488a-a58e-ac75a07364f2","f0a9dda3-02db-4823-80de-198a82fdbb67","f0f4555a-f0ef-48ad-9683-94631b69038c","f13767f6-c558-4c16-9527-b4b6ca6db8cd","f1756bbe-c373-47d0-9dc4-e541046ee4ce","f176f050-88de-4628-b860-ef03a4474d06","f1a99f01-bc4c-419d-bb94-cc42ca5b1b91","f1f1e8f6-568a-43a9-b567-805602c6d292","f297dd22-32e1-4998-86ae-970135e36bad","f35f82e8-d923-41fd-affd-2447c9a328b1","f373dad7-5f37-450e-82e0-74029f9bd21e","f384f3f8-df3a-4470-aeab-1a53d016a130","f3aed36d-92cb-42b3-b5f5-28f41e60b969","f47f4b30-6702-4c0c-8134-9d1292936fd0","f4a68612-0ca8-4db1-8a6b-95a73d1b0b1f","f5453c00-fc79-4e89-a9d1-6720a8a6adb2","f5df5613-fc6b-4304-b658-0edb03c1ff60","f5e5b79f-1a2e-43ac-bef7-1c26ca62ba5e","f62537af-5fe9-4bfb-bb65-06a6e3d990dd","f6adc477-7c15-4011-92ba-d55c3f95d6af","f6b76651-3bc7-4fb7-b8a0-db36b646adfe","f6bd9254-cf52-4ea5-9c9b-1d029cb1a387","f71df1ae-0959-49c9-93f8-7ee06eb50b4c","f79234c8-e71c-41a1-a2e9-02bcaa1cd8a0","f7a1b988-325a-4a67-999b-1eb58c77b41b","f7e13a62-0000-4079-887e-d077d9411654","f7e595e1-86e6-42a7-b326-270e5e922fd2","f7f49c6e-4afa-4662-ade7-4f1f9dd3b902","f8960753-8a72-4a8e-b8c7-220554f7a92c","f9010c52-7748-4f18-957b-aaf41725445f","f911893f-a4d9-4b5b-9bec-db0bd5212471","f91f7ebb-b7d1-4307-b365-423ae19ab640","fa758917-4b78-400b-ba5f-b7dd3a398754","fae380ca-f3e2-43cd-b169-917dfce6dca1","fae4dfb5-7b65-47cf-9cb0-f72207c7e917","fb0d1462-f2e6-4d4d-bf24-20bafd2049f8","fb3e6b03-5d00-415c-a5c2-7ae866181604","fbc05df2-563f-40a3-958a-c1767f18a31e","fcd8a4a5-7072-4ea6-bb37-a3e0172c3cb3","fd13c6c6-172c-4083-9e1e-6713601c5875","fd729795-1391-459a-829b-fcde62a00105","fd9d13e5-32b9-440e-a380-06cf46abd852","fe103573-c77f-436a-8fe6-db48b270e832","fea3e6fa-8273-4ad6-94ae-eb5d6d34f6c8","fec117e9-ad53-4f81-8f7d-4013233929e4","fecd2c2d-0d4b-450d-ac7c-a12aa2597328","fef1efee-c219-4ad6-a379-34c865a3cbb8","ff829789-e84b-4f70-a82c-2da0aabd4410","ff89a50b-10d0-4643-b031-0de3e354adc6","ffcef8a9-b45a-48e9-bea7-117a0878691f"]

    requester = RequesterFactory.create_requester(settings=otl_facility.settings, auth_type='JWT', env='prd')

    importer = EMInfraImporter(requester=requester)
    assets = importer.import_assets_from_webservice_by_uuids(input_uuids)
    lijst_objecten = []

    agent_collection = AgentCollection(requester=requester)

    for kast in assets:
        wegkantkast = Wegkantkast()
        wegkantkast.naam = kast.naam
        wegkantkast.toestand = kast.toestand
        wegkantkast.geometry = kast.geometry
        wegkantkast.assetId.identificator = kast.naam
        wegkantkast.assetId.toegekendDoor = 'OTLMOW'

        toezichternaam = kast.toezichter.voornaam
        if toezichternaam is None:
            toezichternaam = ''
        if kast.toezichter.naam is not None:
            toezichternaam = toezichternaam + ' ' + kast.toezichter.naam
        toezichter = agent_collection.get_agent_by_full_name(toezichternaam)
        if toezichter is not None:
            toezichterrelatie = otl_facility.relatie_creator.create_betrokkenerelation(bron=wegkantkast, doel=toezichter)
            toezichterrelatie.rol = 'toezichter'
            lijst_objecten.append(toezichterrelatie)

        toezichtgroepnaam = kast.toezichtgroep.naam
        toezichtgroep = agent_collection.get_agent_by_full_name(toezichtgroepnaam)
        if toezichtgroep is not None:
            toezichtgroeprelatie = otl_facility.relatie_creator.create_betrokkenerelation(bron=wegkantkast, doel=toezichtgroep)
            toezichtgroeprelatie.rol = 'toezichtsgroep'
            lijst_objecten.append(toezichtgroeprelatie)

        schadebeheerdernaam = kast.schadebeheerder.naam
        schadebeheerder = agent_collection.get_agent_by_full_name(schadebeheerdernaam)
        if schadebeheerder is not None:
            schadebeheerderrelatie = otl_facility.relatie_creator.create_betrokkenerelation(bron=wegkantkast,
                                                                                            doel=schadebeheerder)
            schadebeheerderrelatie.rol = 'schadebeheerder'
            lijst_objecten.append(schadebeheerderrelatie)

        lijst_objecten.append(wegkantkast)

        hoortbijrelatie = otl_facility.relatie_creator.create_relation(bron=wegkantkast, doel=kast, relatie=HoortBij)
        lijst_objecten.append(hoortbijrelatie)

    # write to a json file that can be uploaded in Davie
    otl_facility.davieExporter.export_objects_to_json_file(lijst_objecten,
                                                           'C:\\resources\\DA-2022-00567_wegkantkasten_prd_voor_import.json')
