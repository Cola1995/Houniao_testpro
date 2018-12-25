import unittest
from selenium import webdriver
import time
from InformationPage import *


class Information(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.url = "http://124.95.129.86:9000/sso/login"
        self.username = "guanliyuan"
        self.password = "youjian@2018"

    def test_01(self):
        '''公告管理新增文章测试用例'''
        Info_page = InformationPage(self.driver, self.url, u"权限管理系统")
        # 调用打开页面组件
        Info_page.open()
        # 切换到登录框Frame
        # Info_page.switch_frame('x-URS-iframe')
        # 调用用户名输入组件
        Info_page.input_username(self.username)
        # 调用密码输入组件
        Info_page.input_password(self.password)
        # 调用点击登录按钮组件
        Info_page.click_submit()
        #调用带点击综合服务管理组件
        Info_page.information_click()
        time.sleep(2)
        Info_page.gonggao_click()
        time.sleep(2)
        Info_page.toframe() #切换至frame
        c1=Info_page.count()
        print(c1)
        time.sleep(2)
        Info_page.addtitle()   #调用点击新增文章按钮组件
        time.sleep(2)
        Info_page.write_title("测试标题一")
        time.sleep(2)
        Info_page.add_link("http://web.youjiana.com/")
        time.sleep(2)
        Info_page.switch_frame('ueditor_0')
        time.sleep(2)
        Info_page.neiron('1111')
        time.sleep(2)
        Info_page.switch_farme_default()
        time.sleep(2)
        Info_page.toframe()  # 切换至frame

        print('pk')
        time.sleep(2)
        Info_page.sava()
        time.sleep(2)
        Info_page.refush()
        time.sleep(2)
        c2 = Info_page.count()
        print(c2)
        self.assertGreater(int(c2),int(c1),msg='添加公告失败')

    def test_02(self):
        self.driver.refresh()
        Info1_page = InformationPage(self.driver, self.url, u"权限管理系统")
        Info1_page.information_click()
        time.sleep(2)
        Info1_page.gonggao_click()
        time.sleep(2)
        Info1_page.toframe()  # 切换至frame
        time.sleep(2)
        Info1_page.ctime_click()
        time.sleep(2)
        Info1_page.first_check()
        time.sleep(2)
        Info1_page.deltitle_click()
        time.sleep(2)
        Info1_page.q_click()
        # time.sleep(2)
        # Info1_page.refush()

    @classmethod
    def tearDownClass(self):
        time.sleep(5)
        self.driver.quit()

if __name__=="__main__":
    unittest.main()