from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup = BeautifulSoup(html, 'lxml')
titles = soup.find_all('td','title')
rank = 1
for title in titles:
    print(str(rank) + " : " + title.find('a').text)
    rank += 1