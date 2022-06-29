from calendar import c
from ledger.block import Block
from ledger.chain import Chain
#from models.channel import Channel
from network import Connection
from simpy import Store
import random


class OrderingService:
    def __init__(self,env,orderers,channel):
        self.env = env
        self.orderers = orderers
        self.leader = orderers[0]
        self.followers = [i for i in orderers if i!=self.leader]
        self.channel = channel
        self.trans = []
        self.pbft = PBFT(env,channel)
        self.env.process(self.start_action(self.channel.trans_store))
        

    def start_action(self,store):
        print(self.channel.name)
        while True:
            transaction =  yield store.get()
            #sending
            for i in self.followers:
                conn = Connection(self.env,self.leader,i)
                yield self.env.timeout(conn.latency)
                
            #response
            response = 0
            for i in self.followers:
                conn = Connection(self.env,i,self.leader)
                yield self.env.timeout(conn.latency)
                response += random.randint(0,1)
                
            
            majority = (response/len(self.followers)) *100
            if(majority>50):
                self.trans.append(transaction)
                if(len(self.trans)==20):
                    block = self.generate_block(self.channel,self.trans)
                    self.env.process(self.pbft.block_validation(block))
                    # for peer in self.channel.peers:
                    #     channels = peer.channels
                    #     index = 0
                    #     for i in range(len(channels)):
                    #         if(channels[i].channel == self.channel.name):
                    #             index = i
                    #             break
                    #     chain = peer.channels[index].chain
                    #     chain.add_block(block)
                    print("\t",self.channel.name," Block Number -",block.block_number,"Prev Hash -",block.prev_hash,"Hash -",block.hash)
                    self.channel.block_store.put(block)
                    self.trans = []
        
        
    def generate_block(self,channel,transactions):
        
        channels = channel.peers[0].channels
        index = 0
        for i in range(len(channels)):
            if(channels[i].channel == channel.name):
                index = i
                break
        chain = channel.peers[0].channels[index].chain
        chain.block_number += 1
        chain.prev_hash = chain.hash
        chain.hash +=  1
        block = Block(chain.block_number,transactions,chain.prev_hash,chain.hash)
        return block
    

class PBFT:
    def __init__(self,env,channel):
        self.env = env
        self.channel = channel
        self.total_peers = len(self.channel.peers)
        self.leader =  channel.peers[0]
        self.followers = [i for i in channel.peers if i!=self.leader]

    def block_validation(self,block):
        
        for i in self.followers:
            conn = Connection(self.env,self.leader,i)
            yield self.env.timeout(conn.latency)
        for i in self.followers:
            for j in self.followers:
                if(i!=j):
                    conn = Connection(self.env,i,j)
                    yield self.env.timeout(conn.latency)
        
        self.add_block_ledger(block)
        
    def add_block_ledger(self,block):
        for peer in self.channel.peers:
            channels = peer.channels
            index = 0
            for i in range(len(channels)):
                if(channels[i].channel == self.channel.name):
                    index = i
                    break
            chain = peer.channels[index].chain
            chain.add_block(block)
        