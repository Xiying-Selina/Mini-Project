import requests
from bs4 import BeautifulSoup
import lxml

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "lxml")

# print(soup.prettify())
all_movies = soup.find_all(name="h3", class_="title")
movie_titles = [movie.getText() for movie in all_movies]
movie_lst = movie_titles[::-1]
# print(movie_lst)

with open("movie.txt", mode="w") as file:
    for movie in movie_lst:
        file.write(f"{movie}\n")



