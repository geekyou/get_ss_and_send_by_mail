#! /usr/bin/python3
#! _*_ coding:utf-8 _*_

import re
import requests
import smtplib
import time
from email.mime.text import MIMEText
#f = open("ss.txt",'a')
headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0"}

url = "https://doub.bid/sszhfx/"

html = requests.get(url,headers = headers)
ss_account_number = "A good day! \n"
ss_account_number += "公众号'做一个极客'\n"
ss_account_number += "ss客户端下载地址\n"
ss_account_number += "https://my.pcloud.com/publink/show?code=XZPtsIZtdDcKUI9JwbNW2OIkGvMcQht2k9V\n"
ss_account_number += "github开源仓库\n"
ss_account_number += "https://github.com/geekyou/get_ss_and_send_by_mail"
ss_account_number += "欢迎star\(^o^)/~\n"
ss_account_number += "将下面的ss:// or ssr:// 批量导入客户端即可"

ss_ = re.findall('ss://(.*?)" target="_blank">',html.text) #获取ss://
for each in ss_:
    # print("ss://" + each)
    ss_account_number = ss_account_number + "ss://" + each + "\n"
ssr_ = re.findall('ssr://(.*?)" target="_blank">',html.text) #获取ssr://
for each in ssr_:
    # print("ssr://" + each)
    ss_account_number = ss_account_number + "ssr://" + each + "\n"

_user = "邮箱名"    #改成你的邮箱名
_pwd  = "密码"      #邮箱密码


#  mail_list


mail_list = ["875101164@qq.com"]  # 收件人邮箱 是一个列表


# mail_list
#f.write(ss_account_number)
#f.close()
for _to in mail_list:                        #发送邮件
    msg = MIMEText(ss_account_number)
    msg["Subject"] = "Your_ss"
    msg["From"]    = _user
    msg["To"]      = _to

    try:
        s = smtplib.SMTP_SSL("smtp.exmail.qq.com", 465)  #这里将 "smtp.email.qq.com" 填写smtp服务器地址
        s.login(_user, _pwd)
        s.sendmail(_user, _to, msg.as_string())
        s.quit()
        print("******")
        time.sleep(0.5)
        print("************")
        time.sleep(0.5)
        print("*****************")
        time.sleep(0.5)
        print("***********************")
        time.sleep(0.5)
        print("*******************************")
        time.sleep(0.5)
        print("Succeed sharing your ss with ")
        print(_to + "\n")
    except smtplib.SMTPException as e:
        print("Failed  -----------,%s" % e)
