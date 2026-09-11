from protocols import diagonistics
from protocols.devices import Light, Speaker
from protocols.service import IoTService

service: IoTService = IoTService()

boss = Speaker()
light = Light()

service.register_device(boss)
service.register_device(light)

service.unregister_device(boss)
service.unregister_device(light)

diagonistics.diag_status(boss)
