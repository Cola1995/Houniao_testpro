from selenium import webdriver
import unittest, time
from selenium.common.exceptions import NoSuchElementException
from HTMLTestRunner import HTMLTestRunner


class loginout(unittest.TestCase):
    '''首页退出登录测试'''

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://124.95.129.86:9000/manage/index"


    def test_login_out(self):
        '''点击退出登录按钮'''
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("username").send_keys("guanliyuan")
        driver.find_element_by_id("password").send_keys("youjian@2018")
        time.sleep(5)
        driver.find_element_by_id("login-bt").click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="menu"]/li[3]/ul/li/a/i').click()  #点击设置按钮
        driver.find_element_by_xpath('//*[@id="menu"]/li[3]/ul/li/ul/li[3]/a').click() #点击退出登录按钮
        time.sleep(3)
        self.assertEqual('权限管理系统',driver.title)
    def tearDown(self):
        time.sleep(5)
        self.driver.quit()



if __name__ == "__main__":
    unittest.main()

