from protocols.device import Device


class Speaker(Device):
    def connect(self) -> None:
        print("Connecting Speaker")

    def disconnect(self) -> None:
        print("Connecting Speaker")

    def status_update(self) -> str:
        return "Speaker is off"


class Light(Device):
    def connect(self) -> None:
        print("Connecting Light")

    def disconnect(self) -> None:
        print("Connecting Light")

    def status_update(self) -> str:
        return "Light is off"
