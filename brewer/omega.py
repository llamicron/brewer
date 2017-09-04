from omegacn7500 import OmegaCN7500
import minimalmodbus
import settings

"""
I know this is messy, but I've been having problems with minimalmodbus for weeks and the author has abandoned it.
This is my best option
"""
class Omega(OmegaCN7500):
    def __init__(self, port, address, baudrate=None, timeout=None):
        if not baudrate:
            baudrate = settings.baudRate

        if not timeout:
            timeout = settings.timeout

        self.omega = OmegaCN7500(port, address)
        self.omega.serial.baudrate = baudrate
        self.omega.serial.timeout = timeout
        return None

    def safeguard(self, item, types):
        for type in types:
            if isinstance(item, type):
                return True
        raise ValueError("Safeguard failed, %s does not match given types of %s" % (item, types))

    def pv(self):
        while True:
            try:
                return float(self.omega.get_pv())
            except IOError:
                continue

    def sv(self):
        while True:
            try:
                return float(self.omega.get_setpoint())
            except IOError:
                continue

    def set_sv(self, temp):
        while True:
            try:
                self.safeguard(temp, [int, float])
                self.omega.set_setpoint(temp)
                return True
            except IOError:
                continue

    def pid_running(self):
        while True:
            try:
                return self.omega.is_running()
            except IOError:
                continue

    def run(self):
        while True:
            try:
                self.omega.run()
                return True
            except IOError:
                continue

    def stop(self):
        while True:
            try:
                self.omega.stop()
                return True
            except IOError:
                continue
