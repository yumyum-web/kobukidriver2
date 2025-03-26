from kobukidriver2.core.packet.command import Command


class CommandTransmission:
    def __init__(self, *commands: Command):
        self.commands = commands

    def serialize(self) -> bytes:
        headers_bytes = bytearray([170, 85])

        data_bytes = bytearray()
        for command in self.commands:
            data_bytes += command.serialize()

        length_bytes = len(data_bytes).to_bytes()

        payload_bytes = length_bytes + data_bytes

        checksum = 0
        for i in range(2, len(payload_bytes)):
            checksum ^= payload_bytes[i]
        checksum_bytes = checksum.to_bytes()

        return headers_bytes + payload_bytes + checksum_bytes
