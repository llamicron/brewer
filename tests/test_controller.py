import sys
import os
import unittest
from terminaltables import AsciiTable
from ..brewer.settings import relays
from ..brewer.controller import Controller

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

    def test_pid(self):
        self.con.pid(1)
        assert self.con.pid_status()['pid_running']
        self.con.pid(0)
        assert not self.con.pid_status()['pid_running']

    def test_hlt(self):
        self.con.hlt(0)
        assert not self.con.relay_status(relays["hlt"])
        self.con.hlt(1)
        assert self.con.relay_status(relays["hlt"])

    def test_hlt_to(self):
        self.con.hlt_to("mash")
        assert self.con.relay_status(relays["hltToMash"])
        self.con.hlt_to("boil")
        assert not self.con.relay_status(relays["hltToMash"])
        with self.assertRaises(ValueError):
            self.con.hlt_to("Narnia")

    def test_rims_to(self):
        self.con.rims_to("mash")
        assert self.con.relay_status(relays["rimsToMash"])
        self.con.rims_to("boil")
        assert not self.con.relay_status(relays["rimsToMash"])
        with self.assertRaises(ValueError):
            self.con.rims_to("Hogwarts")


    def test_pump(self):
        self.con.pump(1)
        assert self.con.pump_status()
        self.con.pump(0)
        assert not self.con.pump_status()
        with self.assertRaises(ValueError):
            self.con.pump("turn it on, damnit")

    def test_sv(self):
        assert isinstance(self.con.sv(), float)
        self.con.set_sv(140.0)
        assert self.con.sv() == 140.0
        with self.assertRaises(ValueError):
            self.con.set_sv("Didney Whorl?")

    def test_pv(self):
        assert isinstance(self.con.pv(), float)

    def test_watch(self):
        self.con.set_sv(self.con.pv() - 1)
        assert self.con.watch()

    def test_status_table(self):
        assert isinstance(self.con.status_table(), AsciiTable)

    def test_relay_safeguard(self):
        with self.assertRaises(ValueError):
            self.con.hlt(6)
            self.con.hlt(-4)



    def tearDown(self):
        self.con.pump(0)
