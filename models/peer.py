from ledger.block import Block
from ledger.chain import Chain


class Peer:
    def __init__(self,env,network,name,org_name,location):
        self.env = env
        self.network = network
        self.name = name
        self.location = location
        self.env.organizations[org_name]['peers'].append(self.name)
        self.channels = []

    def add_to_channel(self,channel_name):
        self.channels.append(ChannelPeer(channel_name))
        

class ChannelPeer:
    def __init__(self,channel):
        self.channel = channel
        genesis = Block()
        self.chain = Chain()
        self.chain.add_block(genesis)


    
        





