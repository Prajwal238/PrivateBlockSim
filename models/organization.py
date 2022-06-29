from unicodedata import name
from factories.orderer_factory import OrderingFactory
from factories.peer_factor import PeerFactory

from models.peer import Peer



class Organization:
    def __init__(self,world,network,name,location,total_peeers,total_orderers,ca=True,):
        self.env = world.env
        self.network = network
        self.name = name
        self.location = location
        self.ca = ca
        self.total_peers = total_peeers
        self.total_orderers = total_orderers
        
        self.env.organizations.update({self.name : {'location':self.location,
                                                    'total_peers':self.total_peers,
                                                    'admin':f'{name}.peer1',
                                                    'peers':[],
                                                    'ordering service':[]
                                                    }})
        peer = PeerFactory(world,network,name,location)
        self.peers = peer.create_peers(self.total_peers)
        orderer = OrderingFactory(world,network,name,location)
        self.orderers = orderer.create_orderers(self.total_orderers)

        

    


        