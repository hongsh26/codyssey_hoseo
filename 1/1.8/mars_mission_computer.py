import time
from v1_6 import DummySensor
import platform
import psutil
import cpuinfo
import os

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
            print(f"    \'mars_base_internal_temperature\':{self.env_values['mars_base_internal_temperature']},")
            print(f"    \'mars_base_external_temperature\':{self.env_values['mars_base_external_temperature']},")
            print(f"    \'mars_base_internal_humidity\':{self.env_values['mars_base_internal_humidity']},")
            print(f"    \'mars_base_external_illuminance\':{self.env_values['mars_base_external_illuminance']},")
            print(f"    \'mars_base_internal_co2\':{self.env_values['mars_base_internal_co2']},")
            print(f"    \'mars_base_internal_oxygen\':{self.env_values['mars_base_internal_oxygen']}")
            print("}")
            time.sleep(5)

    def get_mission_computer_load(self):
        cpu_usage = psutil.cpu_percent(interval=1)
        
        # 메모리 사용 정보
        memory = psutil.virtual_memory()
        memory_total = round(memory.total / (1024 ** 3), 2)  # GB 단위
        memory_used = round(memory.used / (1024 ** 3), 2)
        memory_percent = memory.percent

        print(f"CPU 사용률: {cpu_usage}%")
        print(f"메모리 사용량: {memory_used}GB / {memory_total}GB ({memory_percent}%)")


    def get_mission_computer_info(self):
        info = cpuinfo.get_cpu_info()
        os_info = platform.system()
        os_version = platform.version()
        cpu_name = info['brand_raw']
        cpu_core = os.cpu_count()
        memory = round(psutil.virtual_memory().total / (1024**3), 2)
        print("{")
        print(f"    \'os\':{os_info},")
        print(f"    \'os_version\':{os_version},")
        print(f"    \'cpu_name\':{cpu_name},")
        print(f"    \'cpu_core\':{cpu_core},")
        print(f"    \'memory\':{memory},")
        print("}")
        self.get_mission_computer_load()

RunComputer = MissionComputer()
RunComputer.get_mission_computer_info()