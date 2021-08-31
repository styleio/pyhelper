#selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

import urllib.parse #URL を解析して構成要素にする
import time #時刻データへのアクセスと変換
from time import sleep #一時停止
import random
import sys

#デバッグ用
from pprint import pprint

class Concert:
    #定数
    waite = 3

    #セレニウム準備
    def __init__(self):
        #webdriverを起動（バージョン違いなら自動インストールされる）
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()

    #URLを開く
    def open(self,url,obj={}):
        self.driver.get(url)
        self.driver.implicitly_wait(10)
        self.rsleep(self.waite)

    #要素をクリック
    def click(self,obj={}):
        #セレクト
        self.select(obj)
        #クリック
        self.elem.click()
        #スリープ
        self.rsleep(self.waite)

    #情報読取
    def text(self,obj={}):
        #セレクト
        self.select(obj)
        #データリターン
        return self.elem.text

    #情報送信
    def send(self,str,obj={}):
        #セレクト
        self.select(obj)
        #特殊文字分岐
        if(str=='ENTER'):
            self.elem.send_keys(Keys.ENTER)
        else:
            self.elem.send_keys(str)
        #スリープ
        self.rsleep(self.waite)

    #存在確認
    def exists(self,obj={}):
        if(self.select(obj)==False):
            return False
        else:
            return True

    #セレクタ
    def select(self,obj={}):
        try:
            if('name' in obj):
                self.elem = self.driver.find_element_by_name(obj['name'])
            elif('id' in obj):
                self.elem = self.driver.find_element_by_id(obj['id'])
            elif('xpath' in obj):
                self.elem = self.driver.find_element_by_xpath(obj['xpath'])
            elif('css' in obj):
                self.elem = self.driver.find_element_by_css_selector(obj['css'])
            else:
                return False
        except:
            return False


    #ランダムスリープ
    def rsleep(self,num,obj={}):
        start = num - 1;
        end = num + 1;
        sleep(random.randint(start,end))

    #終了
    def close(self):
        self.driver.quit()
