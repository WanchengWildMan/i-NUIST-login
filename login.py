
import requests
import base64

username="02502356238"
password=b"895189"
isp="中国联通"
todomain={"中国移动":"CMCC","中国联通":"Unicom","中国电信":"ChinaNet"}
passwordbase64=base64.b64encode(password)
dic={
    "username":username,
    "domain":todomain[isp],
    "password":passwordbase64,
    "enablemacauth":0
}
from urllib.parse import urlencode
resp=requests.post("http://a.nuist.edu.cn/index.php/index/login",headers={
    #"POST":"/index.php/index/login HTTP/1.1","Host":"a.nuist.edu.cn",
    "Content-Type": "application/x-www-form-urlencoded",
    #"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36",
    #"Referer": "http://a.nuist.edu.cn/",
    #"Content-Length": "68",
    #"Cookie": "sunriseDomain=Unicom; sunrisePassword=895189; sunriseRememberPassword=true; sunriseUsername=02502356238; think_language=zh-cn; PHPSESSID=8k21dooe0vsnr80oj4hom3vno1",
    },
data=urlencode(dic))
print(urlencode(dic))
resp.encoding=resp.apparent_encoding
print(resp.text)

if(resp.text.find('''"status":1''')!=-1):
    print("Login Success")
elif(resp.text.find("\u7528\u6237\u5df2\u767b\u5f55")!=-1):
    print("用户已登录")
