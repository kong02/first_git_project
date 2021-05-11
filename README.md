# first_git_project
from bs4 import BeautifulSoup
from urllib.request import urlopen

url=urlopen("https://movie.naver.com/movie/sdb/rank/rmovie.nhn")
bs=BeautifulSoup(url,'html.parser')
body=bs.body

target=body.find(class_='1st_detail_t1')
list=target.find_all('li')
no=1
for n in range(0,len(list)) :
    print("No.",no)
    no+=1

title=list[n].find(class_='tit').find("a").text
print("영화제목 :\t",title)

# 
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup = BeautifulSoup(html, 'lxml')
titles = soup.find_all('td','title')
rank = 1
for title in titles:
    print(str(rank) + " : " + title.find('a').text)
    rank += 1
