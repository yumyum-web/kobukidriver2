from kobukidriver2.core.packet.command import Command


class Sound(Command):
    identifier = 0x03
    data_length = 3

    def __init__(self, note: int, duration: int):
        super().__init__()
        self.note = note
        self.duration = duration

    @property
    def data_bytes(self) -> bytes:
        note_bytes = self.note.to_bytes(2, byteorder="little")
        duration_bytes = self.duration.to_bytes()
        return note_bytes + duration_bytes
