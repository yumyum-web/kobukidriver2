from kobukidriver2.core.packet.command import Command

GET_CONTROL_GAIN_PACKET_IDENTIFIER = 0x0E


class SetControllerGain(Command):
    identifier = GET_CONTROL_GAIN_PACKET_IDENTIFIER
    data_length = 1

    def __init__(self):
        super().__init__()

    @property
    def data_bytes(self):
        return b"0"
