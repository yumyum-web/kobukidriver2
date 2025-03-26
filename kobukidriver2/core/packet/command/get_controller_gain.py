from kobukidriver2.core.packet.command import Command


class GetControllerGain(Command):
    identifier = 0x0E
    data_length = 1

    def __init__(self):
        super().__init__()

    @property
    def data_bytes(self):
        return b"0"
