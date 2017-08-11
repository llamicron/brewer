from controller import Controller

class Recipe():
    def __init__(self, vars):
        self.controller = Controller()
        self.vars = self._all_to_float(vars)

    def store(self):
        pass

    def _all_to_float(self, vars_dict):
        for key, value in vars_dict.iteritems():
            if not key == "name":
                vars_dict[key] = float(value)
        return vars_dict

