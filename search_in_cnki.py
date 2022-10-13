from selenium import webdriver
from time import sleep


# 在知网中查找导师的论文信息
def search_in_cnki(tutor_name):
    # 实例化一个浏览器对象（传入浏览器的驱动程序）
    bro = webdriver.Edge(executable_path='D:\CV\Study_Resources\PaChong\SearchForBest\MicrosoftSearchEdge')
    # 让浏览器发起一个指定url的请求
    bro.get('https://kns.cnki.net/kns8/AdvSearch?dbprefix=CF\
               LS&&crossDbcodes=CJFQ%2CCDMD%2CCIPD%2CCCND%2CCISD%2CSNAD%2CBDZK%2CCCJD%2CCCVD%2CCJFN')
    # 获取浏览器当前页面的页面源码数据
    # page_text = bro.page_source
    # 标签定位
    auth_search_btn = bro.find_element_by_xpath("//li[@name='authorSearch']")
    auth_search_btn.click()
    bro.forward()
    sleep(1)
    search_input1 = bro.find_element_by_xpath("//input[@data-tipid='autxt-1']")
    search_input1.send_keys(tutor_name)
    search_input2 = bro.find_element_by_xpath("//input[@data-tipid='autxt-2']")
    search_input2.send_keys('中国科学技术大学')
    search_btn = bro.find_element_by_xpath("//input[@value='检索']")
    search_btn.click()
    sleep(10)
    bro.quit()





