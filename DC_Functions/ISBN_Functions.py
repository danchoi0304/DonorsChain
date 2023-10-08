import requests
from bs4 import BeautifulSoup



def get_book_name(isbn):
    url = 'https://openlibrary.org/isbn/' + isbn.replace('-', '')
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    result = soup.find('h1').text
    
    return(result)



def get_cover(isbn):
    url = 'https://covers.openlibrary.org/b/isbn/' + isbn.replace('-', '') + ".jpg"
    return url