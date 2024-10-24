import requests
import bs4


# 加入head头伪装爬虫为正常浏览器
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0"
}
# 创建变量接收获取的网页数据并加入herad头
requests = requests.get("https://movie.douban.com/top250", headers=headers)
# 打印网页状态码
print(requests.status_code)
# 打印网页源码
print(requests.text)



