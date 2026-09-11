import random
import string

from abc_protocols.device import Device


def generate_id() -> str:
    return "".join(random.choices(string.ascii_uppercase, k=8))


class IoTService:
    def __init__(self) -> None:
        self.devices: list[Device] = []

    def register_device(self, dev: Device) -> str:
        device_id = generate_id()
        dev.connect()
        self.devices.append(dev)
        return device_id

    def unregister_device(self, d: Device) -> None:
        d.disconnect()
        self.devices.remove(d)

