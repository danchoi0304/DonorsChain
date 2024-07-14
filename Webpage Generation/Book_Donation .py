import requests
from bs4 import BeautifulSoup
import hashlib
import datetime as date
import json
import DC_Functions.Random as Random
import folium

from DC_Functions.BlockChain import *
from DC_Functions.ISBN_Functions import *
from DC_Functions.Random import *
from DC_Functions.Folder_Move import *


class book:
    def __init__(self, isbn, donor, donors_chain):
        self.isbn = isbn
        self.donor = donor
        self.donors_chain = donors_chain
        self.hexa_code = hexa_random()
    
    def book_name(self):
        return get_book_name(self.isbn)


# Create a new blockchain
my_blockchain = Blockchain()

# Add blocks to the blockchain
my_blockchain.add_block(Block(1, date.datetime.now(), (37.4563, 126.7052), ""))
my_blockchain.add_block(Block(2, date.datetime.now(), (42.443961, -76.501881), ""))


bk1 = book('0-9767736-6-X', 'Joung Hwa Choi', my_blockchain)
print(bk1.donor)
print(bk1.book_name())


start_lat = bk1.donors_chain.chain[1].data[0]
start_lon = bk1.donors_chain.chain[1].data[1]

end_lat = bk1.donors_chain.chain[2].data[0]
end_lon = bk1.donors_chain.chain[2].data[1]

print(end_lat, end_lon)

# Create a map centered around the starting coordinates
m = folium.Map(location= (start_lat, start_lon), tiles='CartoDB Positron', zoom_start=5)



# Add markers for the starting and ending points
folium.Marker(location= (start_lat, start_lon), popup='Donated').add_to(m)
folium.Marker(location= (end_lat, end_lon), popup='Received').add_to(m)

m.save("map.html")
move_to_outputs("map.html")
