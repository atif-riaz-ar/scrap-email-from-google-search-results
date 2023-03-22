import time

from bs4 import BeautifulSoup
import requests, lxml

q = 'site:linkedin.com/in/ AND "@gmail.com" AND "DENTIST" AND "United States"'
params = {
    "q": q,
    "hl": "en",  # language
    "gl": "us",  # country of the search, US -> USA
    "start": 0,  # number page by default up to 0
    # "filter": 0         # show all pages by default up to 10
}

# https://docs.python-requests.org/en/master/user/quickstart/#custom-headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}

page_num = 0

while True:
    page_num += 1

    html = requests.get('https://www.google.com/search?q=site:linkedin.com/in/ AND "@gmail.com" AND "DENTIST" AND "United States"&start='+ str(page_num)).text
    soup = BeautifulSoup(html, 'lxml')

    print(soup.find_all("div"))
    exit()

    for result in soup.select("div.MjjYud"):
        title = f'Title: {result.select_one("h3").text}'
        link = f'Link: {result.select_one("a")["href"]}'
        try:
            description = f'Description: {result.select_one(".VwiC3b").text}'
        except:
            description = None

        print(title, link, description, sep="\n", end="\n\n")

    if soup.select_one('.d6cvqb a[id=pnnext]'):
        params["start"] += 10
    else:
        break