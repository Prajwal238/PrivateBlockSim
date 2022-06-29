from numpy import source


class Network:
    def __init__(self,env,name:str):
        self.env = env
        self.name = name
    
class Connection:
    def __init__(self,env,source_node,destination_node):
        self.env = env
        self.source_node = source_node
        self.destination_node = destination_node
        self.latency = self.get_latency()
        #print(self.latency)
    
    def get_latency(self):
        loc1 = self.source_node.location