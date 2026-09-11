import random
import string
from typing import Protocol

# from protocols.device import Device


def generate_id() -> str:
    return "".join(random.choices(string.ascii_uppercase, k=8))


# class IoTService:
#     def __init__(self) -> None:
#         self.devices: list[Device] = []

#     def register_device(self, dev: Device) -> str:
#         device_id = generate_id()
#         dev.connect()
#         self.devices.append(dev)
#         return device_id

#     def unregister_device(self, d: Device) -> None:
#         d.disconnect()
#         self.devices.remove(d)

# REWRITING above class using protocols
# Method register devices method uses any class that inherits from devices
# But all IotServices needs is any class that has connect/disconnect method.
# we can use protocols to minimize exposer to whole ABC structure
# as you can see. We dont need to import Device class.
# no changes to devices class are made.


class DeviceConnections(Protocol):
    def connect(self) -> None: ...
    def disconnect(self) -> None: ...


class IoTService:
    def __init__(self) -> None:
        self.devices: list[DeviceConnections] = []

    def register_device(self, dev: DeviceConnections) -> str:
        device_id = generate_id()
        dev.connect()
        self.devices.append(dev)
        return device_id

    def unregister_device(self, d: DeviceConnections) -> None:
        d.disconnect()
        self.devices.remove(d)
