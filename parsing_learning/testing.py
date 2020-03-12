from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from lxml.html import fromstring

driver = webdriver.Firefox(executable_path='geckodriver.exe')


def get_html(url):
    global driver
    driver.get(url)
    return fromstring(driver.page_source)


html = get_html('https://ja.wikipedia.org/wiki/ウィキ')
text = html.xpath('//*[@id="mw-content-text"]/div/p[9]/text()')
picture = html.xpath('//*[@id="mw-content-text"]/div/div[4]')
picture_2 = driver.find_element_by_xpath('//*[@id="mw-content-text"]/div/div[4]')

print(text)

driver.close()
