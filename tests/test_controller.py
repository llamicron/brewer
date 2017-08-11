import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import unittest
from settings import relays
from controller import Controller


class ControllerTestCase(unittest.TestCase):
    def setUp(self):
        self.con = Controller()

    def test_object_creation(self):
        assert isinstance(self.con, Controller)

    def test_relay_status(self):
        self.con.set_relay(1, 1)
        assert self.con.relay_status(1)

    def test_set_relay(self):
        self.con.set_relay(3, 0)
        assert not self.con.relay_status(3)
        self.con.set_relay(3, 1)
        assert self.con.relay_status(3)

    def test_pid_status(self):
        assert isinstance(self.con.pid_status(), dict)

    def test_pid_status_types(self):
        assert isinstance(self.con.pid_status()["pid_running"], bool)
        assert isinstance(self.con.pid_status()["pv"], float)
        assert isinstance(self.con.pid_status()["sv"], float)

    def test_hlt(self):
        self.con.hlt(0)
        assert not self.con.relay_status(relays["hlt"])
        self.con.hlt(1)
        assert self.con.relay_status(relays["hlt"])

    def test_rims_to(self):
        self.con.rims_to("mash")
        assert self.con.relay_status(relays["rimsToMash"])
        self.con.rims_to("boil")
        assert not self.con.relay_status(relays["rimsToMash"])
        with self.assertRaises(ValueError):
            self.con.rims_to("Hogwarts")

    def test_hlt_to(self):
        self.con.hlt_to("mash")
        assert self.con.relay_status(relays["hltToMash"])
        self.con.hlt_to("boil")
        assert not self.con.relay_status(relays["hltToMash"])
        with self.assertRaises(ValueError):
            self.con.hlt_to("Narnia")

