import random
from factories.peer_factor import PeerFactory
from ledger.block import Block
from ledger.chain import Chain
from models.peer import Peer
from network import Network
from service.ordering_service import OrderingService
from simpy import Store


class Channel:
    def __init__(self,world,network,name,total_org,organizations,admin,endorsers,endorsment_policy,total_peers,peers,orderers):
        self.world = world
        self.network = network
        self.name = name
        self.total_organizations = total_org
        self.organizations = organizations
        self.admin = admin
        self.endorsers_list = endorsers
        self.endorsment_policy = endorsment_policy
        self.total_peers = total_peers
        self.peers = peers
        self.orderers = orderers
        self.trans_store = Store(self.world.env)
        self.block_store = Store(self.world.env)

        self.service = OrderingService(self.world.env,self.orderers,self)

        for i in peers:
            i.add_to_channel(self.name)
        
        

        
        
