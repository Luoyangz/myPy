import requests
import re

url = "http://www.zhongyaocai360.com/"#需要爬取图片的网页地址
page = requests.get(url).text#得到网页源码
# print(page)
res = re.compile(r'src="(http.+?.jpg)"')#运用正则表达式过滤出图片路径地址
print(res)
reg = re.findall(res, page)#匹配网页进行搜索出图片地址数组
# print(reg)

#循环遍历下载图片
num = 0
for i in reg:
    a = requests.get(i)
    f = open("C:\program1/test/aaa/%s.png"%num, 'wb')#以二进制格式写入img文件夹中
    f.write(a.content)
    f.close()
    print("第%s张图片下载完毕"%num)
    num = num+1
