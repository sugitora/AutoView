from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import random
from selenium.webdriver.common.by import By

import os
from dotenv import load_dotenv
import webbrowser

# .envファイルから環境変数を読み込む
load_dotenv()

# 環境変数からURLを取得
url = os.getenv('MY_WEBSITE_URL')
xpath = os.getenv('MY_XPATH')
# URLが設定されている場合、デフォルトのウェブブラウザで開く
if url:
    webbrowser.open(url)
else:
    print("URLが.envファイルに設定されていません。")

t = 9 * 60 + random.uniform(0, 37)

options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service, options=options)

for i in range(100):    
    t=9*60+random.uniform(0, 37)
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)
    driver.get(url) #URLにアクセス
    # // elemの変数を用意して、elemの変数にクリックしたい「画像」のxpathの情報を格納している。
    elem = driver.find_element(By.XPATH, xpath)

    # // 先ほど指定したクリックしたい要素を格納した変数elemにクリックを指示する
    elem.click()

    time.sleep(t)
    print(str(i)+"回目の"+str(t)+"秒経過しました。")
    driver.close()