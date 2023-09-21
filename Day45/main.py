# from bs4 import BeautifulSoup
# #import lxml
#
# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# #soup = BeautifulSoup(contents, "lxml")
#
# # print(soup)
# # print(soup.prettify())
# # print(soup.title)
# # print(soup.title.name)
# # print(soup.title.string)
# # print(soup.li)
# # print(soup.a)
#
# all_anchor_tags = soup.find_all(name="a")
# # # all_paragraphs = soup.find_all(name="p")
# # #print(all_anchor_tags)
# #
# #
# # for tag in all_anchor_tags:
# #     #print(tag.get_text())
# #     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# #print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# # print(section_heading)
# # print(section_heading.text)
# # print(section_heading.name)
# # print(section_heading.get("class"))
#
# # company_url = soup.select_one(selector="p a")
# # print(company_url)
#
# # name = soup.select_one(selector="#name")
# # print(name)
#
# # headings = soup.select(".heading")
# # print(headings)


from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")

web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")
articles = soup.find_all(name="a", rel="noreferrer")

article_texts = []
article_links =[]

for article_tag in articles:
    text = article_tag.get_text()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)

print(article_texts[largest_index])
print(article_links[largest_index])





