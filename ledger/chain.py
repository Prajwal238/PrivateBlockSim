class Chain:

    def __init__(self):
        self.block_number = 0
        self.prev_hash = 0
        self.hash = 1
        self.chain = []
    
    def add_block(self,block):
        self.chain.append(block)
        

