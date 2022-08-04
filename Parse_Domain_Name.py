# -- coding: utf-8 --

from browsermobproxy import Server
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json
import time
import csv

class BrowserMobProxy:

    def __init__(self):
        # 代理中继及中继端口启动

        self.port = {"port":8800}
        self.server = Server(r"E:\pdf\src\browsermob-proxy-2.1.4-bin\browsermob-proxy-2.1.4\bin\browsermob-proxy.bat")
        self.server.start()
        self.proxy = self.server.create_proxy()
        #浏览器设置代理
        self.chrome_option = Options()
        self.chrome_option.add_argument('--ignore-certificate-errors')
        self.chrome_option.add_argument('--proxy-server={0}'.format(self.proxy.proxy))
        self.driver = webdriver.Chrome(options=self.chrome_option)



    def Proxy_Domain_Name(self,Domain_Name):
        #base_url = "https://app-portal-ppe1.envisioniot.com/forget-password/done"
        base_url = Domain_Name
        self.proxy.new_har(options={'captureHeaders': True, 'captureContent': True})
        self.driver.get(base_url)
        result=self.proxy.har
        with open('proxytest.har', 'w') as outfile:
            json.dump(self.proxy.har, outfile)
        # 从抓取遍历
        re_date = {'qingqiu_head': 1, 'huifu_head': 2, 'qingqiu_url': 3, 'huifu_url': 4}
        for entry in result['log']['entries']:
            _url = entry['request']['url']
            print(len(entry['request']['headers']))
            print(_url)
        self.proxy.close()
        self.server.stop()
        self.driver.quit()




