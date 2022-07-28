import os
import time
import urllib
from scrapy import Selector
from selenium import webdriver

proxy={"http":"xf123456789-zone-custom:123456:proxy.ipidea.io:2333"}

class  GoogleSiteUrl:
    def __init__(self):
        self.browser=webdriver.Chrome('C:\Program Files\Google\Chrome\Application\chromedriver.exe')
        self.key_world = input('Please input the content of the picture you want to grab >:')

    def start_crawl(self):
        self.browser.get('https://www.google.com/search?q=%s' %self.key_world)
        self.browser.implicitly_wait(3)
        xpath_urls='//div[@class="yuRUbf"]/a'
        urls_pre = self.browser.find_elements("xpath",xpath_urls)
        for i in range(0, len(urls_pre)):
            url = urls_pre[i].get_attribute("href")
            time.sleep(3)
            print(url)


if __name__=='__main__':
    google_url=GoogleSiteUrl()
    google_url.start_crawl()

