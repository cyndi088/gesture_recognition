import os
import requests
import base64


class BodyAnalysis(object):
    def __init__(self):
        self.authorization_service = 'https://aip.baidubce.com/oauth/2.0/token'
        self.grant_type = 'client_credentials'
        self.api_key = 'uXS3628lLLRGVGYNnqzNjksc'
        self.secret_key = 'EU4Pykb3RbQllrulScrGizb6IYsmZcYy'
        self.gesture_url = 'https://aip.baidubce.com/rest/2.0/image-classify/v1/gesture'

    """获取access_token"""
    def access_token(self):
        payload = {'grant_type': self.grant_type, 'client_id': self.api_key, 'client_secret': self.secret_key}

        r = requests.post(self.authorization_service, data=payload)
        res = r.json()
        access_token = res['access_token']  # TODO
        return access_token

    """手势API"""
    def gesture(self, filename):
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}

        filepath = os.path.abspath('.') + '\\' + filename
        with open(filepath, 'rb') as f:  # TODO
            img = base64.b64encode(f.read())
        access_token = self.access_token()
        payload = {'access_token': access_token, 'image': img}
        r = requests.post(url=self.gesture_url, headers=headers, data=payload)
        res = r.json()
        if res['result']:
            classname = res['result'][0]['classname']
            return classname
        else:
            classname = None
            return classname


if __name__ == "__main__":
    body = BodyAnalysis()
    for i in range(1, 18):
        filename = str(i) + '.jpg'
        classname = body.gesture(filename)
        print(filename, classname)
    # filename = "2.jpg"
    # classname = body.gesture(filename)
    # print(classname)
