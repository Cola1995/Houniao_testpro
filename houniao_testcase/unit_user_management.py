from selenium import webdriver
import unittest
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import random

class user_management(unittest.TestCase):
    '''用户管理测试类'''
    @classmethod
    def setUpClass(self):
        self.driver=webdriver.Chrome()
        self.driver.get('http://124.95.129.86:9000/manage/index')
        self.driver.maximize_window()
        self.driver.find_element_by_id("username").send_keys("guanliyuan")
        self.driver.find_element_by_id("password").send_keys("youjian@2018")
        time.sleep(5)
        self.driver.find_element_by_id("login-bt").click()
        self.fac = '北京不修车修理厂'
        self.pla = '测试工位'
        self.a = 'test'
        self.aa=''
    @unittest.skip
    def test_01(self):
        '''汽修厂管理添加汽修厂测试用例'''
        e=random.randint(0,9)   #手机号最后两位用随机数拼接
        q= random.randint(0,9)
        phone=f"131255878{e}{q}"

        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="mCSB_1_container"]/ul/li[5]/a').click()  # 点击首页一级菜单用户管理
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="mCSB_1_container"]/ul/li[5]/ul/li[4]/a').click()  # 点击二级菜单汽修厂管理
        time.sleep(2)
        self.driver.switch_to.frame(self.driver.find_element_by_tag_name("iframe"))  # 切换只iframe
        time.sleep(2)
        count = self.driver.find_element_by_xpath('// *[ @ id = "main"]/div[1]/div[2]/div[4]/div[1]/span[1]').text[-5]  # 获取当前汽修厂数量
        #// *[ @ id = "main"] / div[1] / div[2] / div[4] / div[1] / span[1]

        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="toolbar"]/a').click()
        time.sleep(2)
        #汽修厂名称
        self.driver.find_element_by_xpath('//*[@id="repairFactoryName" and @maxlength="30"]').send_keys('北京测试修理厂')
        time.sleep(2)
        #汽修厂电话
        self.driver.find_element_by_xpath('//*[@id="repairFactoryPhone" and @maxlength="30" ]').send_keys(phone)
        time.sleep(2)
        self.driver.find_element_by_id('repairFactoryHrMoney').clear()   #钱/工时
        self.driver.find_element_by_id('repairFactoryHrMoney').send_keys('50')
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="repairFactoryPersonName" and @maxlength="30"]').send_keys('王')  #负责人名称
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="repairFactoryPersonPhone" and @maxlength="30"]').send_keys(phone) #负责人电话
        time.sleep(2)
        p=self.driver.find_element_by_id('province')  #省份
        Select(p).select_by_visible_text('北京')
        time.sleep(2)
        u=self.driver.find_element_by_id('updateCityId')  #市
        time.sleep(2)      #通过input 标签传入图片字符串
        self.driver.find_element_by_id('repairFactoryCover').send_keys(r'C:\Users\Administrator\Desktop\picture\005.jpg')
        Select(u).select_by_visible_text('北京市')
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="goMapBtn"]/label').click()  #点击打开地图按钮
        time.sleep(3)
        canvas=self.driver.find_element_by_tag_name("canvas")     #获取canvas并移动到相应位置点击定位
        #print(canvas.get_attribute('offset'))
        drawing=ActionChains(self.driver) \
            .move_by_offset(-15, -400).click()

        drawing.perform()
        time.sleep(4)
        self.driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/div/div/div/div[1]').click()

        # time.sleep(2)
        # self.driver.find_element_by_id('mapName').send_keys('北京市昌平区龙泽园街道龙锦苑(五区)龙锦苑5区')
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="updateForm"]/div[3]/a[1]').click()  #点击保存
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="main"]/div[1]/div[1]/div[2]/button').click()
        time.sleep(2)
        count1 = self.driver.find_element_by_xpath('//*[ @ id = "main"]/div[1]/div[2]/div[4]/div[1]/span[1]').text[-5]  # 获取当前汽修厂数量
        self.assertGreater(int(count1),int(count),msg='汽修厂创建失败 faied')
    @unittest.skip
    def test_02(self):
        '''汽修厂新增：北京不修车修理厂，测试工位,视屏账号test'''

        self.driver.refresh()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="mCSB_1_container"]/ul/li[5]/a').click()  # 点击首页一级菜单用户管理
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="mCSB_1_container"]/ul/li[5]/ul/li[5]/a').click()  # 点击二级菜单汽修厂工位管理
        time.sleep(2)
        self.driver.switch_to.frame(self.driver.find_element_by_tag_name("iframe"))  # 切换只iframe
        time.sleep(2)
        count1 = self.driver.find_element_by_xpath('// *[ @ id = "main"] / div[2] / div[2] / div[4] / div[1] / span[1]').text[-5]  # 获取当前汽修厂数量
                # // *[ @ id = "main"] / div[2] / div[2] / div[4] / div[1] / span[1]
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="toolbar"]/a[1]').click()
        time.sleep(2)
        from selenium.webdriver.support.select import Select
        s=self.driver.find_element_by_id('updateFac')
        Select(s).select_by_visible_text('北京不修车修理厂')     #汽修厂
        time.sleep(2)
        self.driver.find_element_by_id('workPositionName').send_keys('测试工位')   #工位
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="workPositionAccount" and @maxlength="64"]').send_keys('test')
        #self.driver.find_element_by_id('workPositionAccount').send_keys('test')
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="updateForm"]/div[2]/a[1]').click()
        time.sleep(2)
        count = \
        self.driver.find_element_by_xpath('// *[ @ id = "main"] / div[2] / div[2] / div[4] / div[1] / span[1]').text[
            -5]  # 获取当前汽修厂数量
        self.assertGreater(int(count),int(count1),msg='汽修厂工位新增失败')


    @unittest.skip
    def test_03(self):
        '''汽修厂工位删除用例'''

        self.driver.refresh()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="mCSB_1_container"]/ul/li[5]/a').click()  # 点击首页一级菜单用户管理
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="mCSB_1_container"]/ul/li[5]/ul/li[5]/a').click()  # 点击二级菜单汽修厂工位管理
        time.sleep(2)
        self.driver.switch_to.frame(self.driver.find_element_by_tag_name("iframe"))  # 切换只iframe
        time.sleep(2)
        f=self.driver.find_element_by_id('facId')
        Select(f).select_by_visible_text(self.fac)
        time.sleep(2)
        self.driver.find_element_by_id('workPositionAccount').send_keys(self.a)
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="collapseOne"]/div/div[5]/button').click()  #查询
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[2]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="toolbar"]/a[2]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div/div/div[4]/button[1]').click()  #确认删除
        time.sleep(2)
        count=self.driver.find_element_by_xpath('//*[@id="main"]/div[2]/div[2]/div[4]/div[1]/span[1]').text[-5]
        self.assertEqual(count,'0',msg='删除失败')




    @unittest.skip
    def test_04(self):
        '''用户管理添加用户测试用例'''
        self.driver.refresh()
        h = random.randint(0, 9)
        j= random.randint(0, 9)
        k= random.randint(0, 9)
        l= random.randint(0, 9)
        tel = f"1312525{h}{j}{k}{l}"
        self.aa=tel
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="mCSB_1_container"]/ul/li[5]/a').click()  # 点击首页一级菜单用户管理
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="mCSB_1_container"]/ul/li[5]/ul/li[1]/a').click()  # 点击二级菜单用户管理
        time.sleep(2)
        self.driver.switch_to.frame(self.driver.find_element_by_tag_name("iframe"))  # 切换只iframe
        time.sleep(2)
        count=self.driver.find_element_by_xpath('//*[@id="main"]/div[1]/div[2]/div[4]/div[1]/span[1]').text[19:22] #获取数据总数

        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="toolbar"]/a').click()  #点击新增用户
        time.sleep(4)
        self.driver.find_element_by_id('userBaseName').send_keys('test1')
        self.driver.find_element_by_id('userBasePhone').send_keys(tel)
        time.sleep(2)
        l=self.driver.find_element_by_id('userBaseLevel')
        Select(l).select_by_visible_text('一级')
        time.sleep(2)
        p=self.driver.find_element_by_id('province')
        Select(p).select_by_visible_text('北京')
        time.sleep(2)
        c=self.driver.find_element_by_id('userBaseCityid')
        Select(c).select_by_visible_text('北京市')
        self.driver.find_element_by_xpath('//*[@id="createForm"]/div[3]/a[1]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="main"]/div[1]/div[1]/div[2]/button').click()
        time.sleep(2)
        count1 = self.driver.find_element_by_xpath('//*[@id="main"]/div[1]/div[2]/div[4]/div[1]/span[1]').text[
                 19:22]  # 获取数据总数
        self.assertGreater(int(count1),int(count),msg='添加用户失败')


    @unittest.skip
    def test_05(self):
        '''查询用户测试用例：姓名test1 电话13322115522'''
        self.driver.refresh()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="mCSB_1_container"]/ul/li[5]/a').click()  # 点击首页一级菜单用户管理
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="mCSB_1_container"]/ul/li[5]/ul/li[1]/a').click()  # 点击二级菜单用户管理
        time.sleep(2)
        self.driver.switch_to.frame(self.driver.find_element_by_tag_name("iframe"))  # 切换只iframe

        time.sleep(2)
        self.driver.find_element_by_id('userName').clear()
        self.driver.find_element_by_id('userName').send_keys('test1')
        time.sleep(2)
        self.driver.find_element_by_id('phone').send_keys('13322115522')
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="collapseOne"]/div/div[3]/button').click()
        time.sleep(2)
        count = self.driver.find_element_by_xpath('//*[@id="main"]/div[1]/div[2]/div[4]/div[1]/span[1]').text[
            -5]  # 获取数据总数
        self.assertEqual(count,'1',msg='查询失败')
    @unittest.skip
    def test_06(self):
        self.driver.refresh()
        h = random.randint(0, 9)
        j = random.randint(0, 9)
        k = random.randint(0, 9)
        l = random.randint(0, 9)
        tel = f"131{h}{j}{k}{l}7785"
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="mCSB_1_container"]/ul/li[5]/a').click()  # 点击首页一级菜单用户管理
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="mCSB_1_container"]/ul/li[5]/ul/li[2]/a').click()  # 点击二级菜单取送员管理
        time.sleep(2)
        self.driver.switch_to.frame(self.driver.find_element_by_tag_name("iframe"))  # 切换只iframe
        time.sleep(2)
        count=self.driver.find_element_by_xpath('//*[@id="main"]/div[1]/div[2]/div[4]/div[1]/span[1]').text[-5]
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="toolbar"]/a').click() #点击新增取送员按钮
        time.sleep(2)
        self.driver.find_element_by_id('userDrivingPhone').clear()
        self.driver.find_element_by_id('userDrivingPhone').send_keys(tel)
        time.sleep(2)
        self.driver.find_element_by_id('userDrivingName').send_keys('取送员')
        time.sleep(2)
        p=self.driver.find_element_by_id('privince')
        Select(p).select_by_visible_text('北京')
        time.sleep(2)
        d=self.driver.find_element_by_id('userDrivingCityIdSelect')
        Select(d).select_by_visible_text('北京市')
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="createForm"]/div[3]/a[1]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="main"]/div[1]/div[1]/div[2]/button').click()   #刷新页面
        time.sleep(2)
        count1 = self.driver.find_element_by_xpath('//*[@id="main"]/div[1]/div[2]/div[4]/div[1]/span[1]').text[-5]

        self.assertLess(int(count),int(count1),msg='新建取送员失败')

    def test_07(self):
        #self.driver.refresh()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="mCSB_1_container"]/ul/li[5]/a').click()  # 点击首页一级菜单用户管理
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="mCSB_1_container"]/ul/li[5]/ul/li[2]/a').click()  # 点击二级菜单取送员管理
        time.sleep(2)
        self.driver.switch_to.frame(self.driver.find_element_by_tag_name("iframe"))  # 切换只iframe
        time.sleep(2)
        self.driver.find_element_by_id('userName').clear()
        self.driver.find_element_by_id('userName').send_keys('取送员')
        time.sleep(2)
        self.driver.find_element_by_id('phone').clear()
        self.driver.find_element_by_id('phone').send_keys('13104157785')
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="collapseOne"]/div/div[3]/button').click()
        time.sleep(2)
        count=self.driver.find_element_by_xpath('//*[@id="main"]/div[1]/div[2]/div[4]/div[1]/span[1]').text[-5]
        self.assertEqual(count,'1',msg='查找失败')
    @classmethod
    def tearDownClass(self):
        time.sleep(5)
        self.driver.quit()


if __name__=='__main__':
    unittest.main()