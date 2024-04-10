# import requests
# from bs4 import BeautifulSoup
# response = requests.get(url="https://news.ycombinator.com")
# web_code = response.text
# soup = BeautifulSoup(web_code, "html.parser")
# news = soup.select(selector=".titleline")
# points = soup.select(selector=".score")
# points_int = [int(point.getText().split()[0]) for point in points]
# index = points_int.index(max(points_int))
# print(news[index].getText())
# print(news[index].find("a").get("href"))
# print(points[index].getText())
