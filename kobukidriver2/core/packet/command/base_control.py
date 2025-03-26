from kobukidriver2.core.packet.command import Command


class BaseControl(Command):
    identifier = 0x01
    data_length = 4

    def __init__(self, speed: int, radius: int):
        super().__init__()
        self.speed = speed
        self.radius = radius

    @property
    def data_bytes(self) -> bytes:
        speed_bytes = self.speed.to_bytes(2, byteorder="little")
        radius_bytes = self.radius.to_bytes(2, byteorder="little")
        return speed_bytes + radius_bytes
