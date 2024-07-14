from bs4 import BeautifulSoup
from DC_Functions.ISBN_Functions import *
from DC_Functions.Folder_Move import *

ISBN = input("Enter ISBN: ")

# Open the HTML file
file_path = 'C:\\Users\\danch\\OneDrive\\바탕 화면\\DonorsChain\\outputs\\basic.html'
with open(file_path, 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html.parser')


# Find the <h1> tag
h1_tag = soup.find('h1')
if h1_tag:
    h1_tag.string = get_book_name(ISBN)

img_tag = soup.find('img')

if img_tag:
    new_src = get_cover(ISBN)
    
    img_tag['src'] = new_src

# Save the modified HTML back to the file
with open(ISBN + '.html', 'w', encoding='utf-8') as file:
    file.write(str(soup))

move_to_outputs(ISBN + '.html')