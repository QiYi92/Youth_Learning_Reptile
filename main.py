#!/usr/bin/env python3
#encoding:utf8
#依赖第三方库 requests,lxml
#源项目https://gitee.com/syaoranz/qndxx
#本项目为以上开源项目的二次派生修改，非原创
import requests
from lxml import etree

#为request添加verify=False参数
#导入ssl模块
requests.packages.urllib3.disable_warnings()

try:
    #中青报主页
    url = 'http://news.cyol.com/node_67071.htm'
    #发送get请求,获取网页
    response = requests.get(url, verify=False)
    print("响应状态%d"%response.status_code)
    #解析网页
    html = etree.HTML(response.text)
    newest = html.xpath('/html/body/div[@class="mianbody"]/dl[@class="listMM"]/dd[@class="picB"]/ul[@class="movie-list"]/li[1]/a/@href')[0]
    img_path = newest.replace('m.html', 'images/end.jpg').replace('index.html', 'images/end.jpg')
except:
    print('错误的请求!')

with open('截图.jpg', 'wb') as f:
    img = requests.get(img_path) #获取图像路径
    f.write(img.content) #写入图像内容
    f.close() #关闭
    print('保存完毕!')