from ..brewer import settings
import unittest


# This is mostly useless, just for peace of mind
class SettingsTestCase(unittest.TestCase):

    def test_port(self):
        assert isinstance(settings.port, str)

    def test_addresses(self):
        assert isinstance(settings.rimsAddress, int)
        assert isinstance(settings.switchAddress, int)

    def test_baudrate(self):
        assert isinstance(settings.baudRate, int)

    def test_timeout(self):
        assert isinstance(settings.timeout, float)

    def test_bytes(self):
        assert isinstance(settings.MA0, str)
        assert isinstance(settings.MA1, str)
        assert isinstance(settings.MAE, str)
        assert isinstance(settings.CN, str)

    def test_relays(self):
        for name, relay in settings.relays.iteritems():
            assert isinstance(name, str)
            assert isinstance(relay, int)

    def test_debug(self):
        assert isinstance(settings.DEBUG, bool)
