import unittest
from unittest.mock import Mock

from practice.unit_testing.stub_example import Alarm
from practice.unit_testing.stub_example import Sensor

class AlarmTest(unittest.TestCase):

    def test_alarm_is_off_by_default(self):
        alarm = Alarm()
        self.assertFalse(alarm.is_alarm_on)

    def test_check_too_low_pressure_sounds_alarm(self):
        alarm = Alarm(sensor=TestSensor(12))
        alarm.check()
        self.assertTrue(alarm.is_alarm_on)

    def test_check_too_high_pressure_sounds_alarm(self):
        alarm = Alarm(sensor=TestSensor(22))
        alarm.check()
        self.assertTrue(alarm.is_alarm_on)

    def test_check_too_normal_pressure_no_sounds_alarm(self):
        alarm = Alarm(sensor=TestSensor(18))
        alarm.check()
        self.assertFalse(alarm.is_alarm_on)

    def test_check_with_pressure_ok_with_mock_fw(self):
        test_sensor = Mock(Sensor)
        test_sensor.sample_pressure.return_value = 18
        alarm = Alarm(test_sensor)
        alarm.check()
        self.assertFalse(alarm.is_alarm_on)

class TestSensor():
    def __init__(self, pressure):
        self.pressure = pressure
    def sample_pressure(self):
        return self.pressure

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
