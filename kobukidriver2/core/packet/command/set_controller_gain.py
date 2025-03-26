from kobukidriver2.core.enums.controller_gain_type import ControllerGainType
from kobukidriver2.core.packet.command import Command


class SetControllerGain(Command):
    identifier = 0x0D
    data_length = 13

    def __init__(
        self, controller_gain_type: ControllerGainType, kp: int, ki: int, kd: int
    ):
        super().__init__()
        self.controller_gain_type = controller_gain_type
        self.kp = kp
        self.ki = ki
        self.kd = kd

    @property
    def data_bytes(self):
        controller_gain_type_byte = self.controller_gain_type.to_bytes()
        kp_bytes = self.kp.to_bytes(4, byteorder="little")
        ki_bytes = self.ki.to_bytes(4, byteorder="little")
        kd_bytes = self.kd.to_bytes(4, byteorder="little")
        return controller_gain_type_byte + kp_bytes + ki_bytes + kd_bytes
