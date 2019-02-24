import requests
from bs4 import BeautifulSoup

# url = "http://dataquestio.github.io/web-scraping-pages/simple.html"
url = "http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html"

page = requests.get(url)

# print("page", page)
# print("page.content", page.content)
# print("page.status_code", page.status_code)

soup = BeautifulSoup(page.content, 'html.parser')

print(soup.prettify())

print(soup.find_all('p', class_='outer-text'))


# print("list(soup.children)", list(soup.children))


# # [print(type(item)) for item in  list(soup.children)]

# html = list(soup.children)[2]

# # print('list(html.children)', list(html.children))

# body = list(html.children)[3]

# # print('list(body.children)', list(body.children))

# p = list(body.children)[1]

# # print('paragraph', p)

# # print('get text:', p.get_text())

# print('soup.find_all(p)', soup.find_all('p'))

# print(soup.find_all('p')[0].get_text())

# print(soup.find('p'))