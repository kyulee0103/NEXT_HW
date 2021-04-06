import requests
from bs4 import BeautifulSoup
from movie import extract_info
import csv

file = open('movie.csv', mode='w', newline='')
writer = csv.writer(file)
writer.writerow(["title","grade","director","actors","date","img"])

movie_html = requests.get('https://movie.naver.com/movie/running/current.nhn#')
movie_soup = BeautifulSoup(movie_html.text,"html.parser")

movie_list_box = movie_soup.find("ul",{"class": "lst_detail_t1"})
movie_list = movie_list_box.find_all("li")

result = extract_info(movie_list)

for element in result:
    row=[]
    row.append(element["title"])
    row.append(element["grade"])
    row.append(element["director"])
    row.append(element["actors"])
    row.append(element["date"])
    row.append(element["img"])
    writer.writerow(row)    

