import time
from v1_6 import DummySensor

class MissionComputer:
    def __init__(self):
        self.env_values = {
            "mars_base_internal_temperature": None,
            "mars_base_external_temperature": None,
            "mars_base_internal_humidity": None,
            "mars_base_external_illuminance": None,
            "mars_base_internal_co2": None,
            "mars_base_internal_oxygen": None
        }
        self.ds = DummySensor()
    
    def get_sensor_data(self):
        while(1):
            self.ds.set_env()
            values = self.ds.get_env()
            self.env_values = values
            print("{")
            print(f"    \'mars_base_internal_temperature\':{self.env_values["mars_base_internal_temperature"]},")
            print(f"    \'mars_base_external_temperature\':{self.env_values["mars_base_external_temperature"]},")
            print(f"    \'mars_base_internal_humidity\':{self.env_values["mars_base_internal_humidity"]},")
            print(f"    \'mars_base_external_illuminance\':{self.env_values["mars_base_external_illuminance"]},")
            print(f"    \'mars_base_internal_co2\':{self.env_values["mars_base_internal_co2"]},")
            print(f"    \'mars_base_internal_oxygen\':{self.env_values["mars_base_internal_oxygen"]}")
            print("}")
            time.sleep(5)


RunComputer = MissionComputer()
RunComputer.get_sensor_data()