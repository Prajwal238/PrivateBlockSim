from models.orderer import Orderer


class OrderingFactory:
    def __init__(self,world,network,org_name,location):
        self.world = world
        self.network = network
        self.org_name = org_name
        self.location = location
    def create_orderers(self,no_of_orderers):
        ordering_service = []
        ord_id = 0
        for i in range(no_of_orderers):
            ord_id +=1
            ord_name = f'{self.org_name}.ord{ord_id}'
            new_orderer = Orderer(self.world.env,self.network,ord_name,self.org_name,self.location)
            ordering_service.append(new_orderer)
        return ordering_service