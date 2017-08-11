import str116
from settings import relays
import time
import omegacn7500

class Controller:
    def __init__(self):
        self.omega = omegacn7500.OmegaCN7500('/dev/ttyAMA0', 1) # port name, slave address

    def relay_status(self, relay_num):
        return str116.get_relay(relay_num)

    def set_relay(self, relay_num, state):
        str116.set_relay(relay_num, state)

    def pid_status(self):
        return {
            "pid_running": self.omega.is_running(),
            "sv": self.omega.get_setpoint(),
            "pv": self.omega.get_pv()
        }

    def hlt(self, state):
        self.set_relay(relays["hlt"], state)

    def hlt_to(self, location):
        if location == "mash":
            self.set_relay(relays["hltToMash"], 1)
            return True
        elif location  == "boil":
            self.set_relay(relays["hltToMash"], 0)
            return True
        else:
            raise ValueError("Location unknown: valid locations are 'mash' and 'boil'")


    def rims_to(self, location):
        if location == "mash":
            self.set_relay(relays["rimsToMash"], 1)
            return True
        elif location == "boil":
            self.set_relay(relays["rimsToMash"], 0)
            return True
        else:
            raise ValueError("Location unknown: valid locations are 'mash' and 'boil'")
