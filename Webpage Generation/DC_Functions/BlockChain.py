import hashlib
import datetime as date
import json

'''
This code defines a Block class, which represents a single block in the blockchain.

Each block contains an index, a timestamp, some data (in this case, a donation), and the hash of the previous block in the chain.
The Blockchain class uses the Block class to create a chain of blocks.

It starts with a genesis block (which is just a regular block with index 0 and no previous hash),
and new blocks are added to the chain by calling the add_block method.

To use this code for donations, you could modify the data field of each block to contain information about the donation,
such as the donor's name, the amount donated, and any notes or comments.

You could also add additional methods to the Blockchain class to make it easier to query the chain 
for information about donations (such as a method to calculate the total amount donated).
'''


class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()
   
    def calculate_hash(self):
        sha = hashlib.sha256()
        sha.update(str(self.index).encode('utf-8') +
                   str(self.timestamp).encode('utf-8') +
                   str(self.data).encode('utf-8') +
                   str(self.previous_hash).encode('utf-8'))
        return sha.hexdigest()


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
   
    def create_genesis_block(self):
        return Block(0, date.datetime.now(), "Genesis Block", "0")
   
    def get_latest_block(self):
        return self.chain[-1]
   
    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)
   
    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True



'''
Save & Load BlockChain with Json files
'''

# Serialize blockchain data to a JSON file
def save_blockchain_to_file(blockchain, filename):
    blockchain_data = []
    for block in blockchain.chain:
        blockchain_data.append({
            'index': block.index,
            'timestamp': str(block.timestamp),
            'data': block.data,
            'previous_hash': block.previous_hash,
            'hash': block.hash
        })
    
    with open(filename, 'w') as file:
        json.dump(blockchain_data, file)
        

# Load blockchain data from the JSON file
def load_blockchain_from_file(filename):
    with open(filename, 'r') as file:
        blockchain_data = json.load(file)
    
    loaded_blockchain = Blockchain()
    
    #Genesis block should be handled separately
    loaded_blockchain.chain[0].timestamp = blockchain_data[0]['timestamp']
    
    for block_data in blockchain_data[1:]:
        loaded_blockchain.add_block(Block(
            block_data['index'],
            date.datetime.strptime(block_data['timestamp'], '%Y-%m-%d %H:%M:%S.%f'),
            block_data['data'],
            block_data['previous_hash']
        ))
    return loaded_blockchain

