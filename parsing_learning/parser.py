from library import *

driver = driver()
urls_indices = [
    '_first',
    '_second',
    '_third'
]
urls = [
    'http://kaf65.mephi.ru/tutorial/datasource_first/',
    'http://kaf65.mephi.ru/tutorial/datasource_second/',
    'http://kaf65.mephi.ru/tutorial/datasource_third/'
]
table_data = '//tbody/tr/td/text()'
headings = []

for url in urls:
    headings.append(get_headings(driver, url))
    url_data = get_data(driver, url, get_table_pages(driver, url), table_data)
    wb = openpyxl.Workbook()
    sheet = wb.active

    for page in range(len(url_data)):
        rows_number = len(url_data[page]) // len(headings[urls.index(url)])
        dividing_list = [url_data[page].index(name) for name in url_data[page]
                         if url_data[page].index(name) % len(headings[urls.index(url)]) == 0
                         and url_data[page].index(name) != 0]

        url_data[page] = [url_data[page][i:j] for i, j in zip([0] + dividing_list, dividing_list + [None])]

        for row in url_data[page]:
            sheet.append(row)

    wb.save('data' + f'{urls_indices[urls.index(url)]}' + '.xlsx')


driver.close()
