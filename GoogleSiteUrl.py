import os
import time
import urllib
from scrapy import Selector
from selenium import webdriver
from selenium.webdriver.common.by import By
proxy={"http":"*"}

class  GoogleSiteUrl:
    def __init__(self):
        self.browser=webdriver.Chrome('C:\Program Files\Google\Chrome\Application\chromedriver.exe')
        self.key_world = input('Please input the content of the picture you want to grab >:')

    #获取网页匹配的超链接数据并提取出来url
    def start_crawl(self):
        self.browser.get('https://www.google.com/search?q=%s' %self.key_world)
        self.browser.implicitly_wait(3)
        """
        xpath_urls='//div[@class="yuRUbf"]/a'
        urls_pre = self.browser.find_elements("xpath",xpath_urls)       
        for i in range(0, len(urls_pre)):
            url = urls_pre[i].get_attribute("href")
            time.sleep(1)
            print(url)
        """

    #点击下一页
    def Start_Next_Click(self):
#        next=self.browser.find_element("link text","下一页")
        xpath_xiayiye='//*[@id="pnnext"]/span[2]'
        self.browser.find_element("xpath",xpath_xiayiye).click()
#        next.click()


if __name__=='__main__':
    google_url=GoogleSiteUrl()
    google_url.start_crawl()              #获取网页匹配的超链接数据
    google_url.Start_Next_Click()
    time.sleep(10)
