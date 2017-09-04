import unittest
from ..brewer import settings
from ..brewer.omega import Omega


class OmegaTestCase(unittest.TestCase):
    def setUp(self):
        self.omega = Omega(settings.port, settings.rimsAddress, settings.baudRate, settings.timeout)

    def test_has_default_baudrate_and_timeout(self):
        omega = Omega(settings.port, settings.rimsAddress)
        # Omega defaults to the settings file
        assert omega.instrument.serial.baudrate == settings.baudRate
        assert omega.instrument.serial.timeout == settings.timeout

    def test_pv(self):
        assert isinstance(self.omega.pv(), float)

    def test_sv(self):
        assert isinstance(self.omega.sv(), float)

    def test_set_sv(self):
        assert self.omega.set_sv(140)
        assert self.omega.sv() == 140
        assert self.omega.set_sv(135)
        assert self.omega.sv() == 135

    def test_safegaurd(self):
        assert self.omega.safeguard(140, [int, float])
        assert self.omega.safeguard(140.0, [int, float])
        assert self.omega.safeguard("string", [str])
        with self.assertRaises(ValueError):
            assert self.omega.safeguard("string", [int, float])
            assert self.omega.safeguard(140, [str])


    def test_pid_run_stop_running(self):
        assert self.omega.run()
        assert self.omega.is_running()
        assert self.omega.stop()
        assert not self.omega.is_running()
