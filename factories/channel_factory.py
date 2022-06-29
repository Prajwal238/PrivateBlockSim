import random

from models.channel import Channel



class ChannelFactory:
    def __init__(self,world,network,organizations,orderers):
        self.world = world
        self.network = network
        self.organizations = organizations
        self.orderers = orderers
        self.no_of_peers = self.total_peers()

    def create_channels(self,no_of_channels):
        channels = []
        channel_id = 0
        for i in range(no_of_channels):
            channel_id +=1
            channel_name = f'channel{channel_id}'
            total_org = random.randint(1,len(self.organizations))
            orgs = self.generate_organizations(total_org)
            total_peers = random.randint(2,self.no_of_peers)
            peers = self.generate_peers(total_peers,orgs)
            admin = peers[0]
            endorsers = self.generate_endorsers(peers)
            endorsment_policy = random.randint(1,len(endorsers))
            channel = Channel(self.world,
                            self.network,
                            channel_name,
                            total_org,
                            orgs,
                            admin,
                            endorsers,
                            endorsment_policy,
                            total_peers,
                            peers,
                            self.orderers)
            
            print(channel_name + " created by " + admin.name)
            print("\t organizations :",end=" ")
            for i in orgs:
                print(i.name,end=" ")
            print()
            print("\t endorsers : ",end=" ")
            for i in endorsers:
                print(i.name,end = " ")
            print()
            print("\t Endorsment policy - ",endorsment_policy)
            print("\t peers : ",end=" ")
            for i in peers:
                print(i.name,end=" ")
            print()
            
            channels.append(channel)
        return channels
    
    def generate_organizations(self,no_of_orgs):
        orgs = []
        for i in range(no_of_orgs):
            org = self.organizations[random.randint(0,len(self.organizations)-1)]
            if org not in orgs:
                orgs.append(org)
            else:
                i -= 1
        return orgs

    def generate_peers(self,no_of_peers,orgs):
        peers = []
        for i in range(no_of_peers):
            org = orgs[random.randint(0,len(orgs)-1)]
            peer = org.peers[random.randint(0,len(org.peers)-1)]
            if peer not in peers:
                peers.append(peer)
            else:
                i -=1
        return peers
    
    def generate_endorsers(self,peers):
        no_of_endorsers = random.randint(1,len(peers))
        endorsers = []
        for i in range(no_of_endorsers):
            end = peers[random.randint(1,len(peers)-1)]
            if end not in endorsers:
                endorsers.append(end)
            else:
                i -= 1
        return endorsers

    
    def total_peers(self):
        peers = 0
        for i in self.organizations:
            peers += i.total_peers
        return peers
    
