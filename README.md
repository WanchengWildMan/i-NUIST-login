# i--NUIST-login for ~~iOS/ipadOS/MacOS~~ all platform
南京信息工程大学校园网登录
# v2新版本
## 认证POST api
### url
http://a.nuist.edu.cn/api/v1/login
### header
##### Content-Type 不是application/json !!
##### Content-Type 不是application/json !!
##### Content-Type 不是application/json !!
#### Content-Type 不写！！！
所以
python requests 参数传到body中，作为一个字符串，不要传到json
### body格式
{"username":"<用户名>","password":"<登录密码>","channel":"<1|2|3|4>","ifautologin":"1","pagesign":"secondauth","usripadd":"<ip地址>"}
eg： {"username":"123123123","password":"123123","channel":"4","ifautologin":"1","pagesign":"secondauth","usripadd":""}
##### channel取值
| 运营商   | 取值 |
| -------- | ---- |
| 中国移动 | 2    |
| 中国电信 | 3    |
| 中国联通 | 4    |
### ip地址GET api
http://a.nuist.edu.cn/api/v1/login
#### ~~正文开始~~
### iOS快捷指令()
https://www.icloud.com/shortcuts/25f586a9791c4e66aa4533a939d6663d
### python脚本示例
``` python
import requests
import ast
import time
r=requests.get("http://a.nuist.edu.cn/api/v1/ip")
ipinfo=ast.literal_eval(r.text)
print(ipinfo)
f="data"

r=requests.post(url="http://a.nuist.edu.cn/api/v1/login",data=\
    r'{"username":"xxxxxxxxxx","password":"xxxxxx","channel":"X","ifautologin":"1","pagesign":"secondauth","usripadd":"'+ipinfo[f]+r'"}')
print(r.text)
time.sleep(0.3)
```
### curl chrome抓包直接复制
windows cmd
``` bat
curl "http://a.nuist.edu.cn/api/v1/login" ^
  --data-raw "^{^\^"username^\^":^\^"xxxxxxxx^\^",^\^"password^\^":^\^"xxxxx^\^",^\^"channel^\^":^\^"4^\^",^\^"ifautologin^\^":^\^"1^\^",^\^"pagesign^\^":^\^"secondauth^\^",^\^"usripadd^\^":^\^"你的ip地址^\^"^}" 
```
非win
``` sh
curl "http://a.nuist.edu.cn/api/v1/login" \
  --data-raw "^{^\^"username^\^":^\^"xxxxxxxx^\^",^\^"password^\^":^\^"xxxxx^\^",^\^"channel^\^":^\^"4^\^",^\^"ifautologin^\^":^\^"1^\^",^\^"pagesign^\^":^\^"secondauth^\^",^\^"usripadd^\^":^\^"你的ip地址^\^"^}" 
```
# v1老版本
## 原理
通过发送http请求模拟登陆
### 请求头
POST /index.php/index/login HTTP/1.1
Connection: keep-alive
Content-Length: 68
Accept: application/json, text/javascript, */*; q=0.01
X-Requested-With: XMLHttpRequest
.....
### 请求体
类型：表单
username=[username]&domain=[InternetServiceProvider]&password=[Base64编码后的密码]&enablemacauth=[0/1]
#### username:
校园网的用户名
#### password:
校园网的密码
#### domain:
Unicom/CMCC/ChinaNet
对应：中国联通/中国移动/中国电信
#### enablemacauth:
0/1

## 实现方法
### iOS/iPadOS
快捷指令实现
### MacOS
待定

## 使用方法
### iOS/iPadOS
1. 在WiFi设置中关闭i-NUIST的自动登录选项
2. 在快捷指令中填入username（校园网的用户名），password（校园网的密码），运营商（中国联通/中国移动/中国电信）
3. 将快捷指令添加到主屏幕或小组件
出现“无法添加不受信任的快捷指令”：[ps]: #ps "ps"
## 缘由
iOS端虽然可以点击wifi设置禁止自动登录实现，但Safari中"认证域"表单仍然显示"南京信息工程大学"，点击后该选项和此前记住密码的选项同时勾选~~十分玄学~~
MacOS可以 sudo defaults write /Library/Preferences/SystemConfiguration/com.apple.captive.control Active -boolean false

但要手动开浏览器进a.nuist.edu.cn记住密码）
## 链接或代码
### iOS/iPadOS快捷指令
[https://www.icloud.com/shortcuts/cf8c607bb406467ab15404a6e255e1b1]

### MacOS
Python打包
打包使用的包：py2app
py2applet --make-setup XXX.py
python/python3 setup py2app
代码见/src文件夹
## ps
#### 添加他人分享的快捷指令前需要打开"允许不受信任的快捷指令"
方法：设置-快捷指令-查看上述开关是否锁死-
-否：打开
-是：运行任意一个快捷指令-开启"允许不受信任的快捷指令"
