# 抓取 漫畫狂的網頁原始碼(HTML)
import bs4
import urllib.request as req
url = "https://www.cartoonmad.com/"
# 建立一個 Request 物件,附加 Request Headers 的資訊
request = req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
})
with req.urlopen(request) as response:
    data = response.read()
# 解析原始碼，取得每篇文章的標題
root = bs4.BeautifulSoup(data, "html.parser")  # html小寫
def FindComic(name):
    titles = root.find("a",string=name)
    return titles.string

def FindComicLink(name):
    Link =root.find("a",string=name)
    return Link
name=input("Comic name: ")
print(FindComic(name))
print(FindComicLink(name))


