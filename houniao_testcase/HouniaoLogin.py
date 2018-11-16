import pytesseract
from selenium import webdriver
import time
from PIL import Image,ImageEnhance



class Houniao():
                
                
                def Hlogin(self,username,usepass):
                                
                                driver=webdriver.Chrome()
                                driver.get("http://hpower.youjiana.com/sso/login/")
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
                                                       
                                
                                print(driver.title)
                                driver.find_element_by_id("username").send_keys(username)
                                driver.find_element_by_id("password").send_keys(usepass)
                                driver.find_element_by_id("checkCode").send_keys(code)
                                driver.find_element_by_id("login-bt").click()
                                time.sleep(3)
                                print(driver.title)


if __name__=='__main__':
                Houniao().Hlogin('guanliyuan','youjian@2018')


                                
