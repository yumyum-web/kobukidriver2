from kobukidriver2.core.enums.sequence_number import SequenceNumber
from kobukidriver2.core.packet.command import Command


class SoundSequence(Command):
    identifier = 0x04
    data_length = 1

    def __init__(self, sound_sequence_id: SequenceNumber):
        super().__init__()
        self.sound_sequence_id = sound_sequence_id

    @property
    def data_bytes(self) -> bytes:
        return self.sound_sequence_id.to_bytes()
