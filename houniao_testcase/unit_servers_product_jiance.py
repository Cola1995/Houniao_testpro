from selenium import webdriver
import unittest
import time


class Jiance(unittest.TestCase):

    '''首页服务管理——检测项管理新增修改测试类'''

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://124.95.129.86:9000/manage/index"
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        driver.find_element_by_id("username").send_keys("guanliyuan")
        driver.find_element_by_id("password").send_keys("youjian@2018")
        time.sleep(5)
        driver.find_element_by_id("login-bt").click()
    def test_01(self):
        '''新增一级检测测试用例'''
        self.driver.find_element_by_xpath('//*[@id="mCSB_1_container"]/ul/li[2]/a').click()  # 点击服务管理
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="mCSB_1_container"]/ul/li[2]/ul/li[2]/a').click()  # 点击产品管理
        self.driver.switch_to.frame(self.driver.find_element_by_tag_name("iframe"))  #切换iframe
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="toolbar"]/a').click()  #点击‘新增一级检测’
        time.sleep(3)
        self.driver.find_element_by_id('safetyCheckName').send_keys('test')
        time.sleep(3)
        self.driver.find_element_by_id('safeCheckRemark').send_keys('test')
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="createForm"]/div[3]/a[1]').click()
        time.sleep(3)
        ul = self.driver.find_element_by_id('treeDemo')   #查找test
        time.sleep(3)
        # li=ul.find_elements_by_tag_name('li')
        li = ul.find_elements_by_xpath('//li[@class="level0"]')
        name=[]
        for item in li:
            t = item.find_element_by_tag_name('a')
            print(t.get_attribute('title'))
            name.append(t.get_attribute('title'))
            if t.get_attribute('title') == 'test':
                t.click()
                break

        self.driver.find_element_by_id('addSub').click()  # 点击添加子检查项按钮
        time.sleep(3)
        self.driver.find_element_by_id('safetyCheckName').send_keys('test1')  # 新增名称输入框发送test1
        time.sleep(3)
        self.driver.find_element_by_id('safeCheckRemark').send_keys('test1')  # 新增备注输入框发送test1
        time.sleep(3)

        self.driver.find_element_by_xpath('//*[@id="createForm"]/div[3]/a[1]').click()  # 新增输入框点击保存

        self.assertIn('test',name)  #断言

    def test_02(self):
        '''删除检测项测试'''
        self.driver.refresh()
        self.driver.find_element_by_xpath('//*[@id="mCSB_1_container"]/ul/li[2]/a').click()  # 点击服务管理
        #self.driver.find_element_by_xpath('//*[@id="mCSB_1_container"]/ul/li[2]/ul/li[1]/a').click()  # 点击产品管理
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="mCSB_1_container"]/ul/li[2]/ul/li[2]/a').click()  # 点击检测管理
        time.sleep(3)
        self.driver.switch_to.frame(self.driver.find_element_by_tag_name("iframe"))  #切换iframe
        ul = self.driver.find_element_by_id('treeDemo')  # 查找test
        time.sleep(3)
        # li=ul.find_elements_by_tag_name('li')
        li = ul.find_elements_by_xpath('//li[@class="level0"]')
        name = []
        for item in li:
            t = item.find_element_by_tag_name('a')
            print(t.get_attribute('title'))
            name.append(t.get_attribute('title'))
            if t.get_attribute('title') == 'test':
                t.click()
                name.remove('test')
                break
        self.driver.find_element_by_id('deleteBtn').click()  #点击删除按钮
        time.sleep(3)
        self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div[4]/button[1]').click()
        self.assertNotIn('test',name)


    @classmethod
    def tearDownClass(self):
        time.sleep(5)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()