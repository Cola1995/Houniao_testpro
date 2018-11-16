from selenium import webdriver
import unittest,time
from HTMLTestRunner import HTMLTestRunner


import pytesseract
from PIL import Image,ImageEnhance
import re
import requests
from pytesseract import image_to_string
import selenium.webdriver.support.ui as ui
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class BaiduIde(unittest.TestCase):
                '''候鸟测试类'''
                def setUp(self):
                                self.driver=webdriver.Chrome()
                                self.driver.implicitly_wait(30)
                                self.base_url="http://hpower.youjiana.com/sso/login/"
                                #driver.get(self.base_url+"/")
                                
                                self.verificationErrors=[]
                                self.accept_next_alert=True
                                
                                
                                
                def test_baidu_ide(self):
                                '''填写账号，密码，验证码点击登录'''
                                driver=self.driver
                                self.driver.get(self.base_url+"/")
                                
                                #driver=webdriver.Chrome()
                                #driver.get("http://hpower.youjiana.com/sso/login/")
                                imgsrc=driver.find_element_by_id("captcha").get_attribute('src')
                                print(imgsrc)
                                screenImg=r"C:\Users\Administrator\Desktop\screenImg.png"
                                driver.get_screenshot_as_file(screenImg)
                                  #获取验证码的位置
                                location=driver.find_element_by_id("captcha").location
                
                                   #获取验证码size
                
                                size=driver.find_element_by_id("captcha").size
                                left=location['x']
                                top=location['y']
                                right=location['x']+size['width']
                                bottom=location['y']+size['height']
                                print(left,top,right,bottom)
                                img=Image.open(screenImg).crop((left,top,right,bottom))
                                img=img.convert('L') 			#转换模式：L | RGB
                                img=ImageEnhance.Contrast(img)#增强对比度
                                img=img.enhance(2.0) 			#增加饱和度
                                img.save(screenImg)
                                print("验证码保存成功")
                                img = Image.open(screenImg)
                                code = pytesseract.image_to_string(img)
                                print(code)
                                #self.code=code
                                
                                #Houniao().Hlogin('guanliyuan','youjian@2018')
                                driver.find_element_by_id("username").send_keys("guanliyuan")
                                driver.find_element_by_id("password").send_keys("youjian@2018")
                                driver.find_element_by_id("checkCode").send_keys(code)
                                driver.find_element_by_id("login-bt").click()
                                #t=driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div[3]')
                                #alert = driver.switch_to_alert().text()
                                #print(alert)
                                time.sleep(3)
                                try:
                                                self.assertEqual("友件物流管理系统",driver.title)
                                except AssertionError as e:
                                                print("标题未找到")
                                                #self.verificationErrors.append(str(e))

                def tearDown(self):
                                
                                self.driver.quit()
                                self.assertEqual([],self.verificationErrors)

if __name__=="__main__":
                #unittest.main()
                suite=unittest.TestSuite()
                suite.addTest(BaiduIde("test_baidu_ide"))
                now_time=time.strftime("%Y_%m_%d_%H_%M_%S")
                fp=open("./report"+now_time+".html","wb")
                runner =HTMLTestRunner(stream=fp,title="百度测试报告",description='用例执行情况')
                runner.run(suite)
                fp.close()
