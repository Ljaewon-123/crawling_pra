from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from time import sleep

def scroll():
    last_page_height = driver.execute_script("return document.documentElement.scrollHeight")
    for i in range(5):
        driver.execute_script('window.scrollTo(0, document.documentElement.scrollHeight)')
        sleep(3)
        new_page_height = driver.execute_script("return document.documentElement.scrollHeight")

        if new_page_height == last_page_height:
            break
        last_page_height = new_page_height

url = 'https://pixabay.com/images/search/'

service = webdriver.edge.service.Service('../drivers/msedgedriver.exe')
driver = webdriver.Edge(service=service)

driver.implicitly_wait(3)   # 3초 기다렸다가 url 가져오겠다
driver.get(url)
scroll()

soup = BeautifulSoup(driver.page_source,'html.parser')

div = soup.find('div',class_='container--HcTw2')

imgs = div.select('img[src]')

path = '../crawling_down_img'

for img in range(len(imgs)):
    # print(img)
    src_img = div.select('img[src]')[img]['src']
    with open(path + f'\pp{img}.jpg', 'wb') as f:
        download_file = requests.get(src_img, )
        f.write(download_file.content)
    print(src_img)




### 이미지 다운도 한번 해보자

# Success!!!

# path = '../crawling_down_img'


# with open(path+'\pp.jpg','wb') as f:
#     download_file = requests.get(div.select('img[src]')[0]['src'],)
#     f.write(download_file.content)


# with open('NASA31.jpg','wb') as f:
#     response = requests.get('http://www.python.org/images/success/nasa.jpg')
#     f.write(response.content)
