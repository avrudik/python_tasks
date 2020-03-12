from selenium import webdriver
from lxml.html import fromstring
from time import sleep


def get_driver():
    agent = webdriver.Firefox(executable_path='geckodriver_32.exe')

    return agent


def get_source_code(agent, url):
    agent.get(url)

    return fromstring(agent.page_source)


def get_table_pages(agent, url):
    source_code = get_source_code(agent, url)
    pages = source_code.xpath('//ul[@class="pagination"]/li/a/@href')
    return list(set(pages))


def get_data(agent, link, pages):
    headers = []
    for page in pages:
        full_link = link + page
        source_code = get_source_code(agent, full_link)
        headers.append(source_code.xpath('//thead/tr/th/a/text()'))
    return headers


if __name__ == '__main__':
    driver = get_driver()
    urls = [
        'http://kaf65.mephi.ru/tutorial/datasource_first/',
        'http://kaf65.mephi.ru/tutorial/datasource_second/',
        'http://kaf65.mephi.ru/tutorial/datasource_third/'
    ]

    for url in urls:
        print(get_data(driver, url, get_table_pages(driver, url)))


    driver.close()
