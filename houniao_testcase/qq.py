str="显示第 1 到第 10 条记录，总共 13 条记录"
print(len(str))
print(str[-5])
print(str[19:22])

# str='//*[@id="table"]/tbody/tr[6]/td[2]'
# a=1
# b=str(a)
# print(b)
# from selenium import webdriver
# import unittest
# import time
#
# from selenium.webdriver.support.select import Select
#
# driver=webdriver.Chrome()
# driver.get("http://124.95.129.86:9000/manage/index")
# driver.maximize_window()
# driver.find_element_by_id("username").send_keys("guanliyuan")
# driver.find_element_by_id("password").send_keys("youjian@2018")
# time.sleep(5)
# driver.find_element_by_id("login-bt").click()
#
#
# time.sleep(2)
# driver.find_element_by_xpath('//*[@id="mCSB_1_container"]/ul/li[9]/a').click()   #点击首页一级菜单车辆管理
# time.sleep(2)
# driver.find_element_by_xpath('//*[@id="mCSB_1_container"]/ul/li[9]/ul/li[1]/a').click() #点击二级菜单车辆信息
# time.sleep(2)
# driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))  #切换只iframe
# driver.find_element_by_id('carInfoUseProperty').clear()
# driver.find_element_by_id('carInfoUseProperty').send_keys('营运')
# time.sleep(2)
#driver.find_element_by_xpath('//*[@id="collapseOne"]/div/div[4]/button').click()  #点击查询按钮
# self.driver.find_element_by_xpath('//*[@id="carInfoNumber"]').clear()
# self.driver.find_element_by_xpath('//*[@id="carInfoNumber"]').send_keys('辽AWL285')

# js = "window.scrollTo(0,300)"  # 针对Chrome有效
# driver.execute_script(js)  #滚动条向下滚动
# time.sleep(2)
# res = driver.find_element_by_xpath('//*[@id="main"]/div[2]/div[2]/div[4]/div[1]/span[1]').text[-5]
# rea1=driver.find_element_by_xpath('//*[@id="main"]/div[2]/div[2]/div[4]/div[1]/span[1]').text
#
# print(rea1)
# print(res)
# v=driver.find_element_by_id('carInfoVipType')

#v=driver.find_element_by_xpath('//*[@id="carInfoVipType"]')
# Select(v).select_by_value('1')
# import random
# # print(random.randint(0,9))
# e=random.randint(0,9)
# q= random.randint(0,9)
# phone=f"131255878{e}{q}"
#
#
# print(phone)







