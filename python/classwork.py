from selenium import webdriver
import time
from lxml.html import fromstring


def get_driver():
    agent = webdriver.Firefox(executable_path='geckodriver.exe')

    return agent


def get_source_page(url, agent):
    agent.get(url)

    return fromstring(agent.page_source)


def get_movie_title(html):
    title = html.xpath('//*[@id="headerFilm"]/h1/span/text()')
    return title


if __name__ == '__main__':
    driver = get_driver()
    source_code = get_source_page("https://www.kinopoisk.ru/film/1080513/", driver)
    print(get_movie_title(source_code))

    time.sleep(3)
    driver.close()

# //*[@id="headerFilm"]/h1/span
# https://github.com/mozilla/geckodriver/releases
