# Standard Libs
import time
from os import getenv

# My Code
from . import str116
from . import settings
from .omega import Omega
from .fake_controller import FakeController
from .color import *
from .slack import BrewerBot

# Not my code
import serial
from terminaltables import AsciiTable

class Controller:
    """
    Entry point for this project.
    """
    def __new__(cls):
        """
        Looks for hardware. If it doesn't find any, return a `FakeController`

        Can be overridden by environment variables `force_fake_controller` and `force_real_controller` set to '1'
        """
        if getenv("force_fake_controller") == '1':
            green("force_fake_controller enabled")
            green("Using FakeController()")
            return FakeController()
        elif getenv("force_real_controller") == '1':
            green("force_real_controller enabled")
            green("Using Controller()")
            return super(Controller, cls).__new__(cls)

        try:
            # This is what throws the error if there's no hardware. Might seem a bit out of place.
            omega = Omega(
                settings.port,
                settings.rimsAddress,
                settings.baudRate,
                settings.timeout
            )
        except serial.serialutil.SerialException as exc:
            return FakeController()
        return super(Controller, cls).__new__(cls)

    def __init__(self):
        self.omega = Omega(
            settings.port,
            settings.rimsAddress,
            settings.baudRate,
            settings.timeout
        )

        self.settings = settings

        self.slack = BrewerBot()

    @staticmethod
    def simulator():
        return FakeController()

    def relay_status(self, relay_num):
        return str116.get_relay(relay_num)

    def set_relay(self, relay_num, state):
        str116.set_relay(relay_num, state)

    def pid_running(self):
        return self.omega.is_running()

    def pid_status(self):
        return {
            "pid_running": bool(self.pid_running()),
            "sv": self.sv(),
            "pv": self.pv()
        }

    def pid(self, state):
        self._safegaurd_state(state)
        if state == 1:
            self.omega.run()
        else:
            self.omega.stop()
        return True

    def hlt(self, state):
        self._safegaurd_state(state)
        self.set_relay(self.settings.relays["hlt"], state)
        return True

    def hlt_to(self, location):
        if location == "mash":
            self.set_relay(self.settings.relays["hltToMash"], 1)
            return True
        elif location  == "boil":
            self.set_relay(self.settings.relays["hltToMash"], 0)
            return True
        else:
            raise ValueError("Location unknown: valid locations are 'mash' and 'boil'")


    def rims_to(self, location):
        if location == "mash":
            self.set_relay(self.settings.relays["rimsToMash"], 1)
            return True
        elif location == "boil":
            self.set_relay(self.settings.relays["rimsToMash"], 0)
            return True
        else:
            raise ValueError("Location unknown: valid locations are 'mash' and 'boil'")

    def pump_status(self):
        return self.relay_status(self.settings.relays["pump"])

    def pump(self, state):
        self._safegaurd_state(state)
        self.set_relay(self.settings.relays['pump'], state)
        return True

    def _safegaurd_state(self, state):
        if not isinstance(state, int):
            raise ValueError("Relay State needs to be an integer, " + str(type(state)) + " given.")
        if state < 0 or state > 1:
            raise ValueError("State needs to be integer 0 or 1, " + str(state) + " given.")
        return True

    def sv(self):
        return float(self.omega.sv())

    def set_sv(self, temp):
        self.omega.safeguard(temp, [int, float])
        self.omega.set_sv(temp)
        return self.omega.sv()

    def pv(self):
        return float(self.omega.pv())

    def watch(self):
        while not round(self.pv()) in range(int(self.sv() - 3), int(self.sv() + 3)):
            time.sleep(4) # :nocov:

        return True

    def status_table(self):
        status = AsciiTable([
            ["Setting", "Value"],
            ["PID on?", str(self.pid_status()['pid_running'])],
            ["Pump on?", str(self.pump_status())],
            ["pv", str(self.pv())],
            ["sv", str(self.sv())]
        ])
        return status
