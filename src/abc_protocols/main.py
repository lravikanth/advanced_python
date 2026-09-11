from abc_protocols import diagonistics
from abc_protocols.devices import Light, Speaker
from abc_protocols.service import IoTService

service: IoTService = IoTService()

boss = Speaker()
light = Light()

service.register_device(boss)
service.register_device(light)

service.unregister_device(boss)
service.unregister_device(light)

diagonistics.diag_status(boss)
