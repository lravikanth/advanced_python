from protocols.device import Device


def diag_status(d: Device):
    print(d.status_update())
