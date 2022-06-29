import json
import datetime
import simpy

class SimulationWorld:
    def __init__(self,initial_time:int,sim_duration:int,confiq_file:str,latency_file:str,delays_file:str):
        self.initial_time = initial_time
        self.simulation_duration = sim_duration
        self.config = self._read_json_file(confiq_file)
        self.latency = self._read_json_file(latency_file)
        self.delays = self._read_json_file(delays_file)
        self.locations = self.config['locations']
        self._env = simpy.Environment(initial_time=self.initial_time)
        self._env.config = self.config
        self._env.latency = self.latency
        print(self._env.latency)
        self._env.delays = self.delays
        end_simulation = initial_time + sim_duration
        self._env.data = {}
        self._env.organizations = {}

    @property   
    def env(self):
        return self._env
    @property
    def start_simulation(self):
        end = self.initial_time + self.simulation_duration
        self._env.run(until=end)
    
    def _read_json_file(self, file_location):
        with open(file_location) as f:
            return json.load(f)
