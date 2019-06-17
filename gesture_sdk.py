import os
from aip import AipBodyAnalysis


""" 你的 APPID AK SK """
APP_ID = '11741060'
API_KEY = 'uXS3628lLLRGVGYNnqzNjksc'
SECRET_KEY = 'EU4Pykb3RbQllrulScrGizb6IYsmZcYy'

client = AipBodyAnalysis(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """
filename = '2.jpg'
filepath = os.path.abspath('.') + '\\' + filename

with open(filepath, 'rb') as f:  # TODO
    img = f.read()


""" 百度手势识别SDK未开放 """
r = client.bodyAttr(img)  # 人流量统计
print(r)
