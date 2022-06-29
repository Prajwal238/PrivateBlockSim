import time
from datetime import datetime


class Block:
   
    def __init__(self,block_number=0,transactions=None,prev_hash=0,hash = 1,timestamp = int(time.time())):
        self.block_number = block_number
        self.timestamp = timestamp
        self.data = transactions
        self.prev_hash = prev_hash
        self.hash = hash

    

    