from selenium import webdriver
import unittest, time
from selenium.common.exceptions import NoSuchElementException
from HTMLTestRunner import HTMLTestRunner


class Chang_pass(unittest.TestCase):
    '''首页修改密码测试类'''

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://124.95.129.86:9000/manage/index"


    def test_Chang_pass(self):
        '''输入新旧密码点击保存，出现弹框表示fail,否则成功'''
        self.ass = {'boolen': None}
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("username").send_keys("kefu")
        driver.find_element_by_id("password").send_keys("kefu2018")
        time.sleep(5)
        driver.find_element_by_id("login-bt").click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="menu"]/li[3]/ul/li/a/i').click()  #点击设置按钮
        driver.find_element_by_xpath('//*[@id="menu"]/li[3]/ul/li/ul/li[1]/a').click() #点击修改密码按钮
        driver.find_element_by_id('oldpassword').send_keys('kefu2018')   #输入旧密码
        driver.find_element_by_id('password').send_keys('123456')     #输入新密码
        driver.find_element_by_xpath('//*[@id="updateForm"]/div[2]/a[1]').click() #点击保存
        #出现弹窗确认按钮
        #driver.find_element_by_xpath('//*[@id="sanhu-power-server"]/div[3]/div[2]/div/div/div/div/div[4]/button').click()
        print(self.ass['boolen'])
        try:
            driver.find_element(by='xpath',value='//*[@id="sanhu-power-server"]/div[3]/div[2]/div/div/div/div/div[4]/button')
        except NoSuchElementException as e:
            print(e)
            self.ass['boolen'] = True
            #return False


        else:
            #return True
            self.ass['boolen'] = False

        print(self.ass['boolen'])
        self.assertTrue(self.ass['boolen'])
        #self.assertEqual('False',self.ass['boolen'])
        # try:
        #     self.assertEqual("发货单管理", driver.title)
        #
        # except AssertionError as e:
        #     print("找不到这个标题")
            # self.verificationErrors.append(str(e))
    def tearDown(self):
        time.sleep(5)
        self.driver.quit()
        # self.assertEqual([],self.verificationErrors)


if __name__ == "__main__":
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(Chang_pass("test_Chang_pass"))
    # now_time = time.strftime("%Y_%m_%d_%H_%M_%S")
    # fp = open("./report" + now_time + ".html", "wb")
    # runner = HTMLTestRunner(stream=fp, title="有件测试报告", description='用例执行情况')
    # runner.run(suite)
    # fp.close()
