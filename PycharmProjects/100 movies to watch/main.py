import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(url=URL)
soup = BeautifulSoup(response.text, "html.parser")
movies = soup.find_all(name="h3", class_="title")
movies_title = [movie.getText() for movie in movies]
movies_title.reverse()
print(movies_title)
with open(file="movies.txt", mode="w", encoding="utf-8") as file:
    for title in movies_title:
        file.write(f"{title}\n")
# Write your code below this line 👇


