import os
import time
import urllib
from scrapy import Selector
from selenium import webdriver
from selenium.webdriver.common.by import By

proxy={"http":"*"}
Old_List=[]

class  GoogleSiteUrl:
    def __init__(self):
        self.browser=webdriver.Chrome('C:\Program Files\Google\Chrome\Application\chromedriver.exe')
        self.key_world = input('Please input the content of the picture you want to grab >:')

    #获取网页匹配的超链接数据并提取出来url
    def start_crawl(self):
        New_List=[]
        self.browser.get('https://www.google.com/search?q=%s' %self.key_world)
        self.browser.implicitly_wait(3)
        xpath_urls='//div[@class="yuRUbf"]/a'
        urls_pre = self.browser.find_elements("xpath",xpath_urls)
        for i in range(0, len(urls_pre)):
            url = urls_pre[i].get_attribute("href")             #url为提取出来的href超链接
            time.sleep(1)
            print(url)
            New_List.append(url)
        return New_List


    #点击下一页
    def Start_Next_Click(self):
#        next=self.browser.find_element("link text","下一页")
        xpath_xiayiye='//*[@id="pnnext"]/span[2]'
        self.browser.find_element("xpath",xpath_xiayiye).click()



    def RemoveRepeat(self,Href_List):
        for i in Href_List:
            if i not in Old_List:
                Old_List.append(i)
            return Old_List





if __name__=='__main__':
    google_url=GoogleSiteUrl()                        #初始化环境并输入搜索关键字
    i=0                  #匹配网页计数器
    while(True):
        Href_Result=google_url.start_crawl()              #获取网页匹配的超链接数据
        List_Result=google_url.RemoveRepeat(Href_Result)  #将上一步获取的网页超链接加入到列表中
        Google_Next_Result=google_url.Start_Next_Click()                     #点击下一页按钮
        time.sleep(10)
        i=i+1
        print(i)
    print(len(List_Result))
