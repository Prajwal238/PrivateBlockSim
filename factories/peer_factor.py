from models.peer import Peer


class PeerFactory:
    def __init__(self,world,network,org_name,location):
        self.world = world
        self.network = network
        self.org_name = org_name
        self.location = location
    def create_peers(self,no_of_peers):
        peers = []
        peer_id =0
        for i in range(no_of_peers):
            peer_id +=1
            peer_name= f'{self.org_name}.peer{peer_id}'
            peer = Peer(self.world.env,
                    self.network,
                    peer_name,
                    self.org_name,
                    self.location)
            peers.append(peer)
        return peers