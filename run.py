import variables
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import re

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('https://www.google.com/search?q='+variables.query)
# search_bar = driver.find_element(By.NAME, 'q')
# search_bar.send_keys(variables.query)
# search_bar.send_keys(Keys.ENTER)

# driver.get('https://www.google.com/search?q=' + q + '&start=' + str(page_num))

# driver.find_elements(By.XPATH, '//div[@class="yuRUbf"]/a[@href]')

divs =  driver.find_elements(By.CLASS_NAME, 'MjjYud')

for result in divs:

    # T = result.xpath('//*[starts-with(@class, "LC20lb")]/text()').extract_first()
    # D = result.xpath('//*[starts-with(@class, "VwiC3b")]/text()').extract_first()
    try:
        T = result.find_element(By.CLASS_NAME, 'LC20lb')
        Desc = result.find_element(By.CLASS_NAME, 'VwiC3b')

        D = re.findall("[0-9a-zA-z]+@[0-9a-zA-z]+\.[0-9a-zA-z]+", Desc.text)


        title = f'Title: {T.text}'
        description = f'Link: {D[0]}'

        print(title, description, sep="\n", end="\n\n")
    except:
        pass
