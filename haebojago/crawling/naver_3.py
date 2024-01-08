import requests
from bs4 import BeautifulSoup

# 사람인척 하기위해 속이는 코드
header_user = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

base_url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query="
key_word = input("검색어를 입력해주세요 : ")
# 탐색을 원하는 url
url = base_url + key_word

req = requests.get(url, headers=header_user)

html = req.text손
soup = BeautifulSoup(html, "html.parser")

print(soup)

# title_link _cross_trigger : 글의 제목
# name : 작성자

title = soup.select(".title_link._cross_trigger")
name = soup.select(".name")

for i in zip(title, name):
    print(i[0].text) #[슈퍼스타]
    print(i[1].text)
    print(i[0]['href'])
    print()