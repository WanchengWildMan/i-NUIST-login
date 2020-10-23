# i--NUIST-login
南京信息工程大学校园网登录
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
用户名
#### password:
密码
#### domain:
Unicom/CMCC/ChinaNet
对应：中国联通/中国移动/中国电信
#### enablemacauth:
0/1

## 针对的平台
### iOS
快捷指令实现
### MacOS

## 缘由
iOS端虽然可以点击wifi设置禁止自动登录实现，但Safari中"认证域"表单仍然显示"南京信息工程大学"，点击后该选项和此前记住密码的选项同时勾选~~十分玄学~~
MacOS可以 sudo defaults write /Library/Preferences/SystemConfiguration/com.apple.captive.control Active -boolean false
但要开浏览器）
