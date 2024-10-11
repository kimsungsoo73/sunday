import time
from bs4 import BeautifulSoup

html_doc = """<html><head><title> webtest - 고희동 </title></head>
<body>
<p class="title"><b> Acorn WebTest's Education </b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="language" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="python" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="url" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">... webtest - class=story </p>
"""

soup = BeautifulSoup(html_doc, 'html.parser')
# print(soup.prettify())

# print(soup.title.name)
# print(soup.title.string)
# print(soup.title.parent.name)
# print(soup.p)
# print(soup.p['class'])

# for link in soup.find_all('a'):
#     print(link.get('href'))

# print(soup.get_text)

markup = "<b><!--Hey, buddy. Want to buy a used parser?--></b>"
soup = BeautifulSoup(markup, 'html.parser')
comment = soup.b.string
print(comment)
