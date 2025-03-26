from io import BytesIO

from serial import Serial

from kobukidriver2.core.packet.feedback import Feedback
from kobukidriver2.core.packet.feedback.basic_sensor_data import BasicSensorData
from kobukidriver2.core.packet.feedback.cliff_sensor_data import CliffSensorData
from kobukidriver2.core.packet.feedback.controller_gain import ControllerGain
from kobukidriver2.core.packet.feedback.current import Current
from kobukidriver2.core.packet.feedback.docking_ir import DockingIR
from kobukidriver2.core.packet.feedback.firmware_version import FirmwareVersion
from kobukidriver2.core.packet.feedback.gpi import GPI
from kobukidriver2.core.packet.feedback.hardware_version import HardwareVersion
from kobukidriver2.core.packet.feedback.inertial_sensor_data import InertialSensorData
from kobukidriver2.core.packet.feedback.raw_3d_gyro import Raw3DGyro
from kobukidriver2.core.packet.feedback.udid import UDID


class FeedbackTransmission:
    feedback_classes: list[Feedback] = [
        BasicSensorData,
        CliffSensorData,
        ControllerGain,
        Current,
        DockingIR,
        FirmwareVersion,
        GPI,
        HardwareVersion,
        InertialSensorData,
        Raw3DGyro,
        UDID,
    ]

    def __init__(self, *feedbacks: Feedback):
        self.feedbacks = feedbacks

    @classmethod
    def from_serial(cls, serial: Serial):
        feedbacks = []
        data_length = serial.read()[0]
        data = serial.read(data_length)
        checksum = serial.read()[0]
        for b in data:
            checksum ^= b
        if checksum != 0:
            raise Exception("Checksum error")
        data_buffer = BytesIO(data)
        while data_buffer.tell() < data_length:
            feedback_id = data_buffer.read(1)[0]
            for feedback_class in cls.feedback_classes:
                if feedback_class.identifier == feedback_id:
                    feedback_length = data_buffer.read(1)[0]
                    feedbacks.append(
                        feedback_class.from_buffer(data_buffer, feedback_length)
                    )
                    break
            else:
                raise Exception(f"Unknown feedback identifier: {feedback_id}")
        return cls(*feedbacks)
