from selenium import webdriver
import unittest,time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

class add_product(unittest.TestCase):
    '''首页服务管理——产品管理测试类'''
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://124.95.129.86:9000/manage/index"

    def test_01(self):
        '''登陆类'''
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        driver.find_element_by_id("username").send_keys("guanliyuan")
        driver.find_element_by_id("password").send_keys("youjian@2018")
        time.sleep(5)
        driver.find_element_by_id("login-bt").click()
        time.sleep(5)
        self.assertEqual('候鸟车服后台管理系统',driver.title)

    def test_02(self):
        '''产品管理下产品名称输入框单项测试'''
        self.driver.find_element_by_xpath('//*[@id="mCSB_1_container"]/ul/li[2]/a').click() #点击服务管理
        self.driver.find_element_by_xpath('//*[@id="mCSB_1_container"]/ul/li[2]/ul/li[1]/a').click() #点击产品管理
        self.driver.switch_to.frame(self.driver.find_element_by_tag_name("iframe"))  #切换只ifame
        self.driver.find_element_by_id('findName').send_keys('平衡检测') #输入“平衡检测”
        time.sleep(5)
        self.driver.find_element_by_xpath('//*[@id="collapseOne"]/div/div[3]/button').click()  #点击查询
        time.sleep(5)
        # js = "window.scrollTo(0,300)"  # 针对Chrome有效
        # self.driver.execute_script(js)  #滚动条向下滚动
        # 提取查询数据关键字
        res = self.driver.find_element_by_xpath('//*[@id="main"]/div[1]/div[2]/div[4]/div[1]/span[1]').text[-5]
        #print(type(res))
        self.assertEqual('1',res)  #断言判断是否查到数据
    def test_03(self):
        '''产品管理下“产品类型”输入框单项测试'''
        self.driver.refresh()
        self.driver.find_element_by_xpath('//*[@id="mCSB_1_container"]/ul/li[2]/a').click()  # 点击服务管理
        self.driver.find_element_by_xpath('//*[@id="mCSB_1_container"]/ul/li[2]/ul/li[1]/a').click()  # 点击产品管理
        self.driver.switch_to.frame(self.driver.find_element_by_tag_name("iframe"))
        s = self.driver.find_element_by_id('findType')
        Select(s).select_by_index(2)  # 选中下拉框内容
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="collapseOne"]/div/div[3]/button').click
        res = self.driver.find_element_by_xpath('//*[@id="main"]/div[1]/div[2]/div[4]/div[1]/span[1]').text[-5]
        self.assertGreater(int(res), 1, msg="查到超过1条数据")
    def test_04(self):
        '''产品管理页面下添加产品测试'''
        self.driver.refresh()
        self.driver.find_element_by_xpath('//*[@id="mCSB_1_container"]/ul/li[2]/a').click()  # 点击服务管理
        self.driver.find_element_by_xpath('//*[@id="mCSB_1_container"]/ul/li[2]/ul/li[1]/a').click()  # 点击产品管理
        self.driver.switch_to.frame(self.driver.find_element_by_tag_name("iframe"))
        time.sleep(5)
        first=self.driver.find_element_by_xpath('//*[@id="main"]/div[1]/div[2]/div[4]/div[1]/span[1]').text[19:22]
        self.driver.find_element_by_xpath('//*[@id="toolbar"]/a[1]').click()
        time.sleep(3)
        self.driver.find_element_by_id('productName').send_keys("test")  #产品name
        self.driver.find_element_by_id('productPrice').send_keys('100')
        self.driver.find_element_by_id('productContent').send_keys("test")
        self.driver.find_element_by_xpath('//*[@id="createForm"]/div[3]/a[1]').click()
        time.sleep(5)
        second = self.driver.find_element_by_xpath('//*[@id="main"]/div[1]/div[2]/div[4]/div[1]/span[1]').text[19:22]
        self.assertLess(int(first), int(second), msg="当第二次数据总条数大于第一次是为Pass")
    def test_05(self):
        '''产品管理页面删除产品测试'''
        self.driver.refresh()
        self.driver.find_element_by_xpath('//*[@id="mCSB_1_container"]/ul/li[2]/a').click()  # 点击服务管理
        self.driver.find_element_by_xpath('//*[@id="mCSB_1_container"]/ul/li[2]/ul/li[1]/a').click()  # 点击产品管理
        self.driver.switch_to.frame(self.driver.find_element_by_tag_name("iframe"))
        #按创建时间排序
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="main"]/div[1]/div[2]/div[1]/table/thead/tr/th[6]/div[1]')
        time.sleep(5)
        table_tr_list = self.driver.find_element(By.ID, 'table').find_elements(By.TAG_NAME, "tr")
        print(len(table_tr_list))
        table_list = []  # 存放table数据
        for tr in table_tr_list:  # 遍历每一个tr
            # 将每一个tr的数据根据td查询出来，返回结果为list对象
            table_td_list = tr.find_elements(By.TAG_NAME, "td")
            row_list = []
            print(table_td_list)
            for td in table_td_list:  # 遍历每一个td
                print(td.text)
                row_list.append(td.text)  # 取出表格的数据，并放入行列表里
            table_list.append(row_list)

        # 循环遍历table数据，确定查询数据的位置
        for i in range(len(table_list)):
            for j in range(len(table_list[i])):
                if 'test' == table_list[i][j]:
                    print("坐标为(%r,%r)" % ( i + 1, j + 1))
                    self.driver.find_element_by_xpath(f"//*[@id='table']/tbody/tr[{i}]/td[{j+1}]").click()
                    break
            else:
                continue
            break

        self.driver.find_element_by_xpath('//*[@id="toolbar"]/a[2]').click() #点击删除产品按钮
        self.driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div/div/div[4]/button[1]').click() #点击确认

        self.assertFalse('test' in table_list,msg='table中未找到相关信息，数据删除成功')
    @classmethod
    def tearDownClass(self):
        time.sleep(5)
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

    # suite = unittest.TestSuite()
    # suite.addTest(add_product("test_Alogin_in"))
    # suite.addTest(add_product("test_tadd_product"))
    #
    #
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
