from bs4 import BeautifulSoup
from DC_Functions.ISBN_Functions import *
import shutil
import os

# Function to get book name (mock implementation)
def get_book_name(isbn):
    url = "https://openlibrary.org/isbn/" + isbn
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        h1_tag = soup.find('h1')
        if h1_tag:
            return h1_tag.text.strip()
    return "Unknown Title"

# Function to get book cover URL (mock implementation)
def get_cover(isbn):
    url = "https://covers.openlibrary.org/b/isbn/" + isbn + "-L.jpg"
    response = requests.get(url)
    if response.status_code == 200:
        return url
    return ""

# Get user input
donor = input("Enter donor: ")
ISBNs = input("Enter ISBNs (separate by space): ")

# Split the input string into a list of ISBNs
ISBN_list = ISBNs.strip().split()

# Process each ISBN
for ISBN in ISBN_list:
    file_path = 'C:\\Users\\danch\\OneDrive\\문서\\GitHub\\DonorsChain\\Webpage Generation\\outputs\\book_basic.html'
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

    # Update the <h1> tag with the book name
    h1_tag = soup.find('h1')
    if h1_tag:
        h1_tag.string = get_book_name(ISBN)

    # Update the <img> tag with the book cover URL
    img_tag = soup.find('img')
    if img_tag:
        new_src = get_cover(ISBN)
        img_tag['src'] = new_src

    # Save the modified HTML to a new file named after the ISBN
    output_file_path = f'{ISBN}.html'
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(str(soup))

    source = "C:\\Users\\danch\\OneDrive\\문서\\GitHub\\DonorsChain\\Webpage Generation\\" + f'{ISBN}.html'
    
    # Destination path 
    destination = "C:\\Users\\danch\\OneDrive\\문서\\GitHub\\DonorsChain\\Webpage Generation\\outputs\\" + donor

    # If the destination file already exists, remove it
    if os.path.exists(destination + "\\" + f'{ISBN}.html'):
        os.remove(destination + "\\" + f'{ISBN}.html')

    shutil.move(source, destination)

    print(f"Processed {ISBN}, output saved to {output_file_path}")