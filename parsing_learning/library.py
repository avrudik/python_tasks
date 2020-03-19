import selenium
import lxml
import openpyxl


def driver():
    agent = selenium.webdriver.Firefox(executable_path='geckodriver_64.exe')

    return agent


def get_source_code(agent, url_link):
    agent.get(url_link)

    return lxml.html.fromstring(agent.page_source)


def get_table_pages(agent, url_link):
    source_code = get_source_code(agent, url_link)
    pages = source_code.xpath('//ul[@class="pagination"]/li/a/@href')
    pages = list(set(pages))
    pages.sort()
    return pages


def get_headings(agent, link):
    headings = []
    source_code = get_source_code(agent, link)
    source = source_code.xpath('//thead/tr/th/a/text()')
    for heading in source:
        if heading not in headings:
            headings.append(heading)
    return headings


def get_data(agent, link, pages, xpath):
    source = []
    for page in pages:
        full_link = link + page
        source_code = get_source_code(agent, full_link)
        source.append(source_code.xpath(xpath))
    return source


if __name__ == '__main__':
    pass
