import random


class Transcations:
    def __init__(self,world,env):
        self.world = world
        self.env = env
    
    def generate_transcations(self,channel):
        i = 1
        while(True):
            tid = i
            amount = random.random()
            l = len(channel.peers)
            sender = channel.peers[random.randint(0,l-1)]
            reciver = channel.peers[random.randint(0,l-1)]
            while(reciver==sender):
                reciver = channel.peers[random.randint(0,l-1)]
            transcation = Transcation(self.env,tid,amount,sender,reciver)

            if(self.env.process(transcation.validate(channel.endorsers_list,channel.endorsment_policy))):
                yield self.env.timeout(2)
                yield channel.trans_store.put(transcation)
                
                #yield self.store.put(transcation)
                #print(f"\t{transcation.tid} {transcation.amount} {transcation.sender_node.name} {transcation.reciver_node.name} {channel.name}")
                
                #pass the transaction to the ordering service
                #service = channel.service
            i += 1


        

class Transcation:
    def __init__(self,env,tid,amount,sender_node,reciver_node):
        self.env = env
        self.tid = tid
        self.amount = amount
        self.sender_node = sender_node
        self.reciver_node = reciver_node
    
    def validate(self,endorsers,policy):
        #check wheather the endorsers accept it or not
        check = 0
        for i in endorsers:
            check += random.randint(0,1) 
            yield self.env.timeout(0.134)
        if(check>=policy):
            return True
        else:
            return False

