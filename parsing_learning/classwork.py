from selenium import webdriver
from lxml.html import fromstring


def get_driver():
    agent = webdriver.Firefox(executable_path='geckodriver_64.exe')

    return agent


def get_source_code(agent, url):
    agent.get(url)

    return fromstring(agent.page_source)


def get_table_pages(agent, url):
    source_code = get_source_code(agent, url)
    pages = source_code.xpath('//ul[@class="pagination"]/li/a/@href')
    return list(set(pages))


def get_data(agent, link, pages):
    headings = []
    for page in pages:
        full_link = link + page
        source_code = get_source_code(agent, full_link)
        source = source_code.xpath('//thead/tr/th/a/text()')
        for i in source:
            if i not in headings:
                headings.append(i)
    return headings


if __name__ == '__main__':
    driver = get_driver()
    urls = [
        'http://kaf65.mephi.ru/tutorial/datasource_first/',
        'http://kaf65.mephi.ru/tutorial/datasource_second/',
        'http://kaf65.mephi.ru/tutorial/datasource_third/'
    ]

    url_headings = []

    for url in urls:
        url_headings.append(get_data(driver, url, get_table_pages(driver, url)))

    print(url_headings)
    driver.close()
