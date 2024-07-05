from bs4 import BeautifulSoup
import requests
import pandas as pd

URL = "https://www.abebooks.com/books/100-books-to-read-in-lifetime/"

HEADERS = ({'User-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'})
webpage = requests.get(URL, headers=HEADERS)
print(webpage)

soup = BeautifulSoup(webpage.content, "html.parser")
links = soup.find_all("a", attrs={'class':'Link'})
exclude_texts = {"Shop now", "Books", "Reading lists", "Passion for books. Books for your passion.", ""}
link_texts = [link.get_text(strip=True) for link in links if link.get_text(strip=True) not in exclude_texts]
min_length = len(link_texts)

data = {
    'Book Name': link_texts[:min_length]
}

df = pd.DataFrame(data)
with open('scrap1.txt', 'w') as file:
        for item in df['Book Name']:
            file.write(f"{item}\n")