import queue
import threading

import serial
import serial.tools.list_ports

from kobukidriver2.core.command_transmission import CommandTransmission
from kobukidriver2.core.feedback_transmission import FeedbackTransmission


class Kobuki:
    def __init__(self, port: str, baud_rate: int):
        self.port = port
        self.baud_rate = baud_rate
        self._serial = serial.Serial(port, baud_rate)
        self._reader_thread: threading.Thread | None = None
        self._feedback_transmissions: queue.Queue[FeedbackTransmission] = queue.Queue()

    @classmethod
    def autodetect(cls):
        for port in serial.tools.list_ports.comports():
            if (  # TODO: Add more thorough checks for detecting a connected Kobuki
                port.description.find("USB Serial Port") != -1
                or port.description.find("Kobuki") != -1
            ):
                return cls(port.device, 115200)
        else:
            raise Exception("Kobuki is not connected")

    def _reader_loop(self):
        while self._reader_thread is not None:
            if (self._serial.read(1) == b"\xaa") and (self._serial.read(1) == b"\x55"):
                self._parse_feedback()

    def _parse_feedback(self):
        self._feedback_transmissions.put(FeedbackTransmission.from_serial(self._serial))

    def send_command_transmission(self, command_transmission: CommandTransmission):
        self._serial.write(command_transmission.serialize())

    def get_feedback_transmission(
        self, block: bool = True, timeout: float | None = None
    ) -> FeedbackTransmission:
        return self._feedback_transmissions.get(block=block, timeout=timeout)

    def start(self):
        self._reader_thread = threading.Thread(target=self._reader_loop)
        self._reader_thread.start()

    def stop(self):
        self._reader_thread = None

    @property
    def is_running(self):
        return self._reader_thread is not None and self._reader_thread.is_alive()
