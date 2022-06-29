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
        loc2 = self.destination_node.location
        locations =self.env.latency['locations'] 
        for i in locations:
            if i==loc1:
                for j in locations[i]:
                    if j==loc2:
                        return locations[i][j]
