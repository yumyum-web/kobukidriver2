from kobukidriver2.core.enums.request_flags import RequestFlags
from kobukidriver2.core.packet.command import Command


class RequestExtra(Command):
    identifier = 0x05
    data_length = 2

    def __init__(self, request_flag: RequestFlags):
        super().__init__()
        self.request_flag = request_flag

    @property
    def data_bytes(self) -> bytes:
        return self.request_flag.to_bytes(2, byteorder="little")
