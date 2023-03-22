from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import  BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time, requests


# Chrome driver install
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.implicitly_wait(0.5)
url = "https://www.google.com/search?q="
url += 'site:linkedin.com/in/ AND "@gmail.com" AND "DENTIST" AND "United States"'
driver.get(url)
time.sleep(2)
search_bar = driver.find_element(By.NAME, 'q')
search_bar.send_keys()
search_bar.send_keys(Keys.ENTER)

page_num = 0

while True:
    page_num += 1
    print(f"{page_num} page:")

    params = {
        "q": "Elon Musk",
        "hl": "en",  # language
        "gl": "us",  # country of the search, US -> USA
        "start": 0,  # number page by default up to 0
        "filter": 0  # show all pages by default up to 10
    }

    headers = {
        "User-Agent": "Chrome/111.0.5563.65"
    }

    html = requests.get("https://www.google.com/search", params=params, headers=headers, timeout=30)
    soup = BeautifulSoup(html.text, 'lxml')

    print(soup.find_element(By.CLASS_NAME, ".tF2Cxc"))
    exit()

    for result in soup.find_element(By.CLASS_NAME, ".tF2Cxc"):
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


# links = []
# n_pages = 20
# for page in range(1, n_pages):
#
#     start = "&start=" + str((page - 1) * 10)
#
#     driver.get(url+start)
#     soup = BeautifulSoup(driver.page_source, 'html.parser')
#     # soup = BeautifulSoup(r.text, 'html.parser')
#
#     divs = soup.select(".MjjYud")
#     for div in divs:
#         # Search for a h3 tag
#         results = div.select(".yuRUbf")
#
#         # Check if we have found a result
#         if (len(results) >= 1):
#             # Print the title
#             h3 = results[0]
#             print(h3.get_text())


# linkedin_users_urls_list = driver.find_elements(By.CLASS_NAME, "yuRUbf")
# linkedin_users_titles_list = driver.find_elements(By.CLASS_NAME, "LC20lb")
# linkedin_users_details_list = driver.find_elements(By.CLASS_NAME, "VwiC3b")

# print(links)