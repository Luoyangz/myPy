# 完整代码
import requests
import time
time.sleep(0.5)

def down_pic(down_url, picname):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3868.400 QQBrowser/10.8.4394.400"
    }  # 发送头信息，这个发送头信息目的就是表明你是一台电脑，防止被网页识别你是爬虫。

    req = requests.get(url=down_url, headers=header)  # 用来获取文本信息
    req.encoding = 'utf-8'  # 用来解码获取的信息（python解释器要按照utf-8编码的方式来读取程序。）

    with open('%s' % picname, "wb") as f:  # 开始写文件，wb代表写二进制文件
        f.write(req.content)

def main():
    url = 'https://www.dlmeasure.com/platform-images/edu_banner1.png'  # 图片链接地址
    picname = '测试.jpg'  # 要保存的图片名称
    down_pic(url, picname)

# 执行函数
main()