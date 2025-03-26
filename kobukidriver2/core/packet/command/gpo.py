from kobukidriver2.core.enums.gpo_flags import GPOFlags
from kobukidriver2.core.packet.command import Command


class GPO(Command):
    identifier = 0x05
    data_length = 2

    def __init__(self, gpo_flag: GPOFlags):
        super().__init__()
        self.gpo_flag = gpo_flag

    @property
    def data_bytes(self) -> bytes:
        return self.gpo_flag.to_bytes(2, byteorder="little")
