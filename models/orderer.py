from network import Connection


class Orderer:
    def __init__(self,env,network,name,org_name,location):
        self.env = env
        self.network = network
        self.name = name
        self.location = location
        self.env.organizations[org_name]['ordering service'].append(self.name)
         
    # def connect(self,followers):
    #     print("leader - ",self.name)
    #     print("follwers - ")
    #     for i in followers:
    #         print(i.name)
    #     for i in followers:
    #         conn = Connection(self.env,self,i)