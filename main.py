import os
from simpy import Store
import time
from json import dumps as dump_json
from models.Transcations import Transcations
from factories.channel_factory import ChannelFactory
from factories.organizations_factory import OrganizationFactory
from network import Connection, Network
from service.ordering_service import OrderingService

from world import SimulationWorld

def write_report(world):
    path = 'output/report.json'
    if not os.path.exists(path):
        os.mkdir('output')
        with open(path, 'w') as f:
            pass
    with open(path, 'w') as f:
        f.write(dump_json(world.env.data))

def leadger(env,channels):
    for i in channels:
        #print(i.name,"- {")
        env.data[i.name] = {}
        for peer in i.peers:
            env.data[i.name][peer.name] = {}
            #print("\t",peer.name,"-{")
            channelpeer = None
            for index in peer.channels:
                if(index.channel==i.name):
                    channelpeer = index
            chain = channelpeer.chain.chain
            env.data[i.name][peer.name]['Total Blocks'] = len(chain)
            env.data[i.name][peer.name]['Ledger'] = []
            #print("\tTotal Blocks - ",len(chain))
            for block in chain:
                data = []
                if block.data!=None:
                    for trans in block.data:
                        s = f"{trans.tid} : {trans.amount}"
                        data.append(s)
                env.data[i.name][peer.name]['Ledger'].append(f"Block number - {block.block_number}, Block Data - {data},Prev Hash -{block.prev_hash},Hash - {block.hash}")
                #print("\t Block Number -",block.block_number,"Block Data -",data,"Prev Hash -",block.prev_hash,"Hash -",block.hash)
            #print("\t}")
        #print("}")

def run_model():
    now = int(time.time())
    duration = 3600
    world = SimulationWorld(
        now,
        duration,
        'input-parameters/config.json',
        'input-parameters/latency.json',
        'input-parameters/delays.json'
    )
    
    env = world.env
    network = Network(env,"NC4")
    organization_details = {
        'Mumbai':{
            'how_many': 1,
            'Ca':True,
            'peers':5,
            'ordering_service':1
        },
        "Delhi":{
            'how_many':1,
            'Ca':True,
            'peers':5,
            'ordering_service':1
        },
        "Chennai":{
            'how_many':1, 
            'Ca':True, 
            'peers':5, 
            'ordering_service':1 
        }
    }
    org = OrganizationFactory(world,network)
    organizations = org.create_organizations(organization_details)
    print(world.env.organizations)
    world.env.data = world.env.organizations


    orderers = []
    for i in organizations:
        for j in i.orderers:
            orderers.append(j)
    


    number_of_channels = 2
    channel = ChannelFactory(world,network,organizations,orderers)
    channels = channel.create_channels(number_of_channels)

    #obj = Connection(env,channels[0].peers[0],channels[0].peers[1])


    transcations = Transcations(world,env)
    #print("Transcations")
    for i in channels:
        env.process(transcations.generate_transcations(i))

    
    world.start_simulation
    leadger(env,channels)
    write_report(world)
   

if __name__ == '__main__':
    run_model()