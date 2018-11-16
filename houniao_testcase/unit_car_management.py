from selenium import webdriver
import unittest
import time
from selenium.webdriver.support.select import Select

class Car_management(unittest.TestCase):
    """车辆管理测试类"""
    @classmethod
    def setUpClass(self):
        self.driver=webdriver.Chrome()
        self.driver.get("http://124.95.129.86:9000/manage/index")
        self.driver.maximize_window()
        self.driver.find_element_by_id("username").send_keys("guanliyuan")
        self.driver.find_element_by_id("password").send_keys("youjian@2018")
        time.sleep(5)
        self.driver.find_element_by_id("login-bt").click()

    def test_01(self):
        """车牌号输入框测试用例,查询车牌号为辽AWL285的车牌号信息"""
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="mCSB_1_container"]/ul/li[9]/a').click()   #点击首页一级菜单车辆管理
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="mCSB_1_container"]/ul/li[9]/ul/li[1]/a').click() #点击二级菜单车辆信息
        time.sleep(2)
        self.driver.switch_to.frame(self.driver.find_element_by_tag_name("iframe"))  #切换只iframe
        self.driver.find_element_by_id('carInfoNumber').clear()   #车牌号输入框输入辽AWL285
        self.driver.find_element_by_id('carInfoNumber').send_keys('辽AWL285')
        # self.driver.find_element_by_xpath('//*[@id="carInfoNumber"]').clear()
        # self.driver.find_element_by_xpath('//*[@id="carInfoNumber"]').send_keys('辽AWL285')
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="collapseOne"]/div/div[4]/button').click()
        time.sleep(2)
        #res = self.driver.find_element_by_xpath('//*[@id="main"]/div[1]/div[2]/div[4]/div[1]/span[1]').text[-5]
        res = self.driver.find_element_by_xpath('//*[@id="main"]/div[2]/div[2]/div[4]/div[1]/span[1]').text[-5]
        # print(type(res))
        # print(res)
        self.assertEqual('1', res)


    def test_02(self):
        '''车辆信息页面下使用性质输入框测试用例；测试通过的前提是必须有使用性质为营运的数据'''
        self.driver.refresh()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="mCSB_1_container"]/ul/li[9]/a').click()  # 点击首页一级菜单车辆管理
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="mCSB_1_container"]/ul/li[9]/ul/li[1]/a').click()  # 点击二级菜单车辆信息
        time.sleep(2)
        self.driver.switch_to.frame(self.driver.find_element_by_tag_name("iframe"))  # 切换只iframe
        time.sleep(2)
        self.driver.find_element_by_id('carInfoUseProperty').clear()
        self.driver.find_element_by_id('carInfoUseProperty').send_keys('营运')
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="collapseOne"]/div/div[4]/button').click()  #点击查询按钮
        time.sleep(2)
        res = self.driver.find_element_by_xpath('//*[@id="main"]/div[2]/div[2]/div[4]/div[1]/span[1]').text[-5]

        self.assertLess(1,int(res),msg="查询不到数据，测试失败")


    def test_03(self):

        '''车辆信息页面下车牌号、使用性质、会员类型输入框组合测试 ：测试通过的前提是有 车牌号为辽AWL285、使用性质为营运、体验会员的车辆信息'''
        self.driver.refresh()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="mCSB_1_container"]/ul/li[9]/a').click()  # 点击首页一级菜单车辆管理
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="mCSB_1_container"]/ul/li[9]/ul/li[1]/a').click()  # 点击二级菜单车辆信息
        time.sleep(2)
        self.driver.switch_to.frame(self.driver.find_element_by_tag_name("iframe"))  # 切换只iframe
        time.sleep(2)
        self.driver.find_element_by_id('carInfoNumber').clear()  # 车牌号输入框输入辽AWL285
        self.driver.find_element_by_id('carInfoNumber').send_keys('辽AWL285')
        time.sleep(2)
        self.driver.find_element_by_id('carInfoUseProperty').clear()
        self.driver.find_element_by_id('carInfoUseProperty').send_keys('营运')
        v=self.driver.find_element_by_id('carInfoVipType')
        Select(v).select_by_value('1')  #体验会员
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="collapseOne"]/div/div[4]/button').click()  # 点击查询按钮
        time.sleep(2)
        res = self.driver.find_element_by_xpath('//*[@id="main"]/div[2]/div[2]/div[4]/div[1]/span[1]').text[-5]
        self.assertEqual(1, int(res), msg="查询不到数据，测试失败")


    def test_04(self):
        '''车辆管理页面，编辑保养次数测试用例；修改车牌号为辽AWL285的保养次数'''
        self.driver.refresh()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="mCSB_1_container"]/ul/li[9]/a').click()  # 点击首页一级菜单车辆管理
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="mCSB_1_container"]/ul/li[9]/ul/li[1]/a').click()  # 点击二级菜单车辆信息
        time.sleep(2)
        self.driver.switch_to.frame(self.driver.find_element_by_tag_name("iframe"))  # 切换只iframe
        time.sleep(2)
        self.driver.find_element_by_id('carInfoNumber').clear()  # 车牌号输入框输入辽AWL285
        self.driver.find_element_by_id('carInfoNumber').send_keys('辽AWL285')
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="collapseOne"]/div/div[4]/button').click()  # 点击查询按钮
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[16]/a[1]').click()  #点击编辑保养次数按钮
        time.sleep(2)
        self.driver.find_element_by_id('carInfoRepairNum').clear()
        self.driver.find_element_by_id('carInfoRepairNum').send_keys('4')  #填写保养次数

        # self.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[16]/a[1]').clear()
        # self.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[16]/a[1]').send_keys('3')

        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="updateForm"]/div[2]/a[1]').click()  #点击保存按钮
        time.sleep(2)
        count=self.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[13]').text   #获取修改后的保养次数
        self.assertEqual(4,int(count),msg='修改失败，failed')


    def test_05(self):
        '''车辆管理页面，黑名单编辑测试用例：运行用例前应未加入黑名单'''
        self.driver.refresh()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="mCSB_1_container"]/ul/li[9]/a').click()  # 点击首页一级菜单车辆管理
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="mCSB_1_container"]/ul/li[9]/ul/li[1]/a').click()  # 点击二级菜单车辆信息
        time.sleep(2)
        self.driver.switch_to.frame(self.driver.find_element_by_tag_name("iframe"))  # 切换只iframe
        time.sleep(2)
        self.driver.find_element_by_id('carInfoNumber').clear()  # 车牌号输入框输入辽AWL285
        self.driver.find_element_by_id('carInfoNumber').send_keys('辽AWL285')
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="collapseOne"]/div/div[4]/button').click()  # 点击查询按钮
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[16]/a[2]').click()  #点击黑名单操作按钮
        time.sleep(2)
        self.driver.find_element_by_id('blacklistRemark').clear()
        self.driver.find_element_by_id('blacklistRemark').send_keys('test')  #向textarea 发送内容
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="updateForm"]/div[2]/a[1]').click()  #点击保存
        time.sleep(2)
        lable=self.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[15]/label').text
        self.assertEqual(lable,'黑名单',msg='修改失败，faile')


    def test_06(self):
        #self.driver.refresh()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="mCSB_1_container"]/ul/li[9]/a').click()  # 点击首页一级菜单车辆管理
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="mCSB_1_container"]/ul/li[9]/ul/li[3]/a').click()  # 点击二级菜单车辆异常信息
        time.sleep(2)
        self.driver.switch_to.frame(self.driver.find_element_by_tag_name("iframe"))  # 切换只iframe
        time.sleep(2)
        count = self.driver.find_element_by_xpath('//*[@id="main"]/div[2]/div[2]/div[4]/div[1]/span[1]').text[-5]  #获取数据条数
        print(count)
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[16]/a').click()  #点击编辑车辆价格按钮
        time.sleep(2)
        self.driver.find_element_by_id('carPrice').clear()
        self.driver.find_element_by_id('carPrice').send_keys('10')   #填写价格
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="updateForm"]/div[2]/a[1]').click()  #点击保存按钮
        time.sleep(2)
        count1 = self.driver.find_element_by_xpath('//*[@id="main"]/div[2]/div[2]/div[4]/div[1]/span[1]').text[-5]  # 获取数据条数
        print(count1)

        self.assertLess(int(count1),int(count),msg='failed')
    @classmethod
    def tearDownClass(self):
        time.sleep(5)
        self.driver.quit()

if __name__=='__main__':

    unittest.main()
