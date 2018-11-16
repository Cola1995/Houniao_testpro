from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import unittest
import time
import os
 
#==============定义发送邮件==========
def send_mail(file_new):
                msg_from='991571566@qq.com'                                 #发送方邮箱
                passwd='kvmgnchjqnuqbbji'                                   #填入发送方邮箱的授权码
                msg_to='991571566@qq.com'
                subject="自动化测试报告"                                                 #主题     
                content="车辆信息已查到"  #正文
                msg = MIMEText(content)

                #file_new=r"C:\Users\Administrator\Desktop\Py\test_report\report2018_10_11_11_55_16.html"
                f = open(file_new,'rb')
                mail_body = f.read()
                f.close()
                msg = MIMEText(mail_body,'html','utf-8')
                msg['Subject'] = subject
                msg['From'] = msg_from
                msg['To'] = msg_to
                try:
                                s = smtplib.SMTP_SSL("smtp.qq.com",465)      #邮件服务器及端口号
                                s.login(msg_from, passwd)
                                s.sendmail(msg_from, msg_to, msg.as_string())
                                print ("发送成功")
                except s.SMTPException.e:
                                print ("发送失败")
                finally:
                                s.quit()
    
#======查找测试目录，找到最新生成的测试报告文件======
def new_report(test_report):
    lists = os.listdir(test_report)                                    #列出目录的下所有文件和文件夹保存到lists
    lists.sort(key=lambda fn:os.path.getmtime(test_report + "\\" + fn))#按时间排序
    file_new = os.path.join(test_report,lists[-1])                     #获取最新的文件保存到file_new
    print(file_new)
    return file_new
 
if __name__ == "__main__":
 
    test_dir = "./houniao_testcase"
    test_report = "./houniao_testreport"
 
    discover = unittest.defaultTestLoader.discover(test_dir,
                                                   pattern = 'unit*.py')
    now = time.strftime("%Y-%m-%d_%H-%M-%S")
    filename = test_report + '\\' + now + 'result.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner(stream = fp,
                            title = '测试报告',
                            description = '用例执行情况：')
    runner.run(discover)
    fp.close()
 
    #new_report = new_report(test_report)
    #send_mail(new_report)
