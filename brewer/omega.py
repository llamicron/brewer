"""
I know this is messy, but I've been having problems with minimalmodbus for weeks and the author has abandoned it.
This is my best option. Sometimes the serial communication fails and you have to retry, hence the while True: loops.
"""
from contextlib import suppress

from omegacn7500 import OmegaCN7500
from .fake_omega import FakeOmega
import minimalmodbus
from . import settings

class Omega():
    """
    A wrapper for OmegaCN7500. Dear god help me...

    Note: "Omega", "CN7500", and "PID" all refer to the same thing. It's an Omega CN7500 PID. Sometimes I refer to the heater as the PID, because I'm slightly retarded.

    Note2: I had to wrap all the methods in while loops because this hardware doesn't play nice.
    """
    def __init__(self, port, address, baudrate=None, timeout=None):
        self.instrument = OmegaCN7500(port, address)
        self.instrument.serial.baudrate = baudrate if baudrate else settings.baudRate
        self.instrument.serial.timeout = timeout if timeout else settings.timeout
        return None

    @staticmethod
    def simulator():
        """
        Returns a "fake omega" that doesn't require any hardware. Used for testing and development.
        """
        return FakeOmega()

    def safeguard(self, item, types):
        """
        Make sure arguments are the expected type
        """
        for type in types:
            if isinstance(item, type):
                return True
        raise ValueError("Safeguard failed, %s does not match given types of %s" % (item, types))

    def pv(self):
        """
        Get the Proccess Value (PV) from the CN7500
        """
        while True:
            with suppress(IOError):
                return float(self.instrument.get_pv())

    def sv(self):
        """
        Get the Setpoint Value (SV) from the CN7500
        """
        while True:
            with suppress(IOError):
                return float(self.instrument.get_setpoint())

    def set_sv(self, temp):
        """
        Set the SV on the CN7500
        """
        while True:
            with suppress(IOError):
                self.safeguard(temp, [int, float])
                self.instrument.set_setpoint(temp)
                return True

    def is_running(self):
        """
        Returns `True` if the CN7500 is powering the heating element, AKA it's "on"
        """
        while True:
            with suppress(IOError):
                return self.instrument.is_running()

    def run(self):
        """
        Turn on the CN7500
        """
        while True:
            with suppres(IOError):
                self.instrument.run()
                return True

    def stop(self):
        """
        Turns off the CN7500
        """
        while True:
            with suppress(IOError):
                self.instrument.stop()
                return True
