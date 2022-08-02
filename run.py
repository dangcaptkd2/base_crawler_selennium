import time
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from tqdm import tqdm

url = 'https://www.gettyimages.at/fotos/man-without-shirt'
result = set()
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
# driver = webdriver.Chrome(chrome_options=options)
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get(url)
# while True:
#     elements = driver.find_elements_by_class_name("PaginationRow-module__buttonText___XM2mA")
#     elements[-1].click()
#     time.sleep(10)
result = []
c=1
while True:
    try:
        time.sleep(3)
        page = driver.page_source
        # driver.quit()
        soup = BeautifulSoup(page, 'html.parser')
        container = soup.find_all('img', class_='MosaicAsset-module__thumb___yvFP5')
        for i in container:
            result.append((i['src']))
        
        print(">>>>> num urls:", len(result))
        elements = driver.find_elements_by_class_name("PaginationRow-module__buttonText___XM2mA")
        print("num pages loaded", c)
        if c==5:
            break
        else:
            elements[-1].click()
        c+=1
    except:
        break

with open(r'./urls.txt', 'w') as fp:
    fp.write('\n'.join(result))


print(">>>>>", Done)
    
    
