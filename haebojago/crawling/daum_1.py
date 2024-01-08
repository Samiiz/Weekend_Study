import requests
from bs4 import BeautifulSoup

# 사람인척 하기위해 속이는 코드
header_user = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

url = "https://webtoon.kakao.com/"
req = requests.get(url)
html = req.text
soup = BeautifulSoup(html, "html.parser")

webtoon_titles = soup.select("whitespace-pre-wrap break-all break-words support-break-word overflow-hidden text-ellipsis !whitespace-nowrap s22-semibold-white text-center leading-26")
webtoon_authors = soup.select("whitespace-pre-wrap break-all break-words support-break-word overflow-hidden text-ellipsis !whitespace-nowrap s12-regular-white mt-4 opacity-75 text-center leading-14")

for title, author in zip(webtoon_titles, webtoon_authors):
    print("웹툰 제목:", title.text.strip())
    print("작가:", author.text.strip())
    print()