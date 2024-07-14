import requests
from bs4 import BeautifulSoup
import hashlib
import datetime as date
import json


#What I made
from DC_Functions.ISBN_Functions import *
from DC_Functions.Random import *
from DC_Functions.BlockChain import *

# Create a new blockchain
my_blockchain = Blockchain()

# Add blocks to the blockchain
my_blockchain.add_block(Block(1, date.datetime.now(), "Data for block 1", ""))
my_blockchain.add_block(Block(2, date.datetime.now(), "Data for block 2", ""))
my_blockchain.add_block(Block(3, date.datetime.now(), "Data for block 3", ""))

# Print blockchain contents
for block in my_blockchain.chain:
    print(f"Block {block.index}:")
    print(f"Timestamp: {block.timestamp}")
    print(f"Data: {block.data}")
    print(f"Hash: {block.hash}")
    print(f"Previous Hash: {block.previous_hash}")
    print()

# Check if the blockchain is valid
print(f"Is blockchain valid? {my_blockchain.is_chain_valid()}")


my_blockchain = Blockchain()

# Add blocks to the blockchain
my_blockchain.add_block(Block(1, date.datetime.now(), "Data for block 1", ""))
my_blockchain.add_block(Block(2, date.datetime.now(), "Data for block 2", ""))
my_blockchain.add_block(Block(3, date.datetime.now(), "Data for block 3", ""))


# Save the blockchain to a JSON file
save_blockchain_to_file(my_blockchain, 'blockchain_data.json')


#Load the blockchain from the JSON file
loaded_blockchain = load_blockchain_from_file('blockchain_data.json')

# Print loaded blockchain contents
for block in loaded_blockchain.chain:
    print(f"Block {block.index}:")
    print(f"Timestamp: {block.timestamp}")
    print(f"Data: {block.data}")
    print(f"Hash: {block.hash}")
    print(f"Previous Hash: {block.previous_hash}")
    print()

# Check if the loaded blockchain is valid
print(f"Is loaded blockchain valid? {loaded_blockchain.is_chain_valid()}")