#coding:utf-8

from weibo import APIClient
APP_KEY = '3053279868'
APP_SECRET = 'e2d8cc0e021f4d08007b69c275c1a9c1'
CALLBACK_URL = 'http://127.0.0.1：8000'

client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
url = client.get_authorize_url()
code = '099a6ce9417f988d57c4f05c18a6f6d4'
client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
r = client.request_access_token(code)
access_token = r.access_token 
expires_in = r.expires_in 

client.set_access_token(access_token, expires_in)


print client.statuses.user_timeline.get()
print client.statuses.update.post(status=u'测试OAuth 2.0发微博')
