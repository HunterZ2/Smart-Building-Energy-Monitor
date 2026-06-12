import random

class VoltageSensor:
    def read(self):
        return random.uniform(215, 235)

class CurrentSensor:
    def read(self):
        return random.uniform(5, 25)
