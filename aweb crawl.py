#web crawling / web scraping ?
#1.request and wait for response --> urllib.request
#2.if response is positive, then fetch data , bs4 (pip install bs4) ,lxml (pip install lxml)
import urllib.request as url
import bs4
name = input("Enter Movie Name : ").replace(" ","+")
path ="https://www.imdb.com/find?q="+name
res = url.urlopen(path)
data = bs4.BeautifulSoup(res,'lxml')
result = data.find('td',class_='result_text')

a_link = "https://www.imdb.com/"+result.find('a')['href']
res = url.urlopen(a_link)
data = bs4.BeautifulSoup(res,'lxml')
div = data.find('div',class_="title_wrapper")
movie_name = div.find('h1').text
print("Movie Name : ",movie_name)
rating = data.find('span',itemprop="ratingValue")
print("Rating :",rating.text,"/10")
