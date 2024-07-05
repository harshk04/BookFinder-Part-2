from bs4 import BeautifulSoup
import requests
import pandas as pd

URL = "https://www.lifestyleasia.com/ind/shop/more/best-fiction-books-of-all-time/"

HEADERS = ({'User-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'}) #add your user agent 

webpage = requests.get(URL, headers=HEADERS)
soup = BeautifulSoup(webpage.content, "html.parser")

names = soup.find_all("ul", class_='btt_toc-list')

book_names = []
for ul in names:
    for li in ul.find_all("li"):
        book_names.append(li.text.split(' by ')[0].strip())


min_length = len(book_names)

data = {
    'Book Name': book_names[:min_length]
}

df = pd.DataFrame(data)

with open('scrap2.txt', 'w') as file:
        for item in df['Book Name']:
            file.write(f"{item}\n")