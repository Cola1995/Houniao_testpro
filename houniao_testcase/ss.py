from selenium import  webdriver
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get('http://124.95.129.86:9000/manage/index')
driver.find_element_by_id("username").send_keys("guanliyuan")
driver.find_element_by_id("password").send_keys("youjian@2018")
time.sleep(5)
driver.find_element_by_id("login-bt").click()
time.sleep(5)
print(driver.title)
driver.find_element_by_xpath('//*[@id="mCSB_1_container"]/ul/li[2]/a').click() #点击服务管理
time.sleep(3)
#driver.find_element_by_xpath('//*[@id="mCSB_1_container"]/ul/li[2]/ul/li[1]/a').click() #点击产品管理
driver.find_element_by_xpath('//*[@id="mCSB_1_container"]/ul/li[2]/ul/li[2]/a').click()

driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))  #切换到iframe
# driver.find_element_by_id('findName').send_keys('平衡检测')
# time.sleep(5)
# driver.find_element_by_xpath('//*[@id="collapseOne"]/div/div[3]/button').click()


ul=driver.find_element_by_id('treeDemo')
time.sleep(3)
#li=ul.find_elements_by_tag_name('li')
li=ul.find_elements_by_xpath('//li[@class="level0"]')
for item in li:
    t=item.find_element_by_tag_name('a')
    print(t.get_attribute('title'))
    if t.get_attribute('title')=='test':
        t.click()
        break

driver.find_element_by_id('addSub').click()  #点击添加子检查项按钮
time.sleep(3)
driver.find_element_by_id('safetyCheckName').send_keys('test1')   #新增名称输入框发送test1
time.sleep(3)
driver.find_element_by_id('safeCheckRemark').send_keys('test1')  #新增备注输入框发送test1
time.sleep(3)

driver.find_element_by_xpath('//*[@id="createForm"]/div[3]/a[1]').click() #新增输入框点击保存






#
# time.sleep(5)
# driver.find_element_by_xpath('//*[@id="toolbar"]/a').click()
# time.sleep(3)
# driver.find_element_by_id('safetyCheckName').send_keys('test')
# time.sleep(3)
# driver.find_element_by_id('safeCheckRemark').send_keys('test')
# driver.find_element_by_xpath('//*[@id="createForm"]/div[3]/a[1]').click()

















#res = driver.find_element_by_xpath('//*[@id="main"]/div[1]/div[2]/div[4]/div[1]/span[1]').text[-5]
#res = driver.find_element_by_xpath('//*[@id="main"]/div[1]/div[2]/div[4]/div[1]/span[1]').text
#res1 = driver.find_element_by_xpath('//*[@id="main"]/div[1]/div[2]/div[4]/div[1]/span[1]').text[14:16]
#print(len(res))

# driver.find_element_by_xpath('//*[@id="findType"]/option[2]').click()
# s=driver.find_element_by_id('findType')
# Select(s).select_by_index(2) #选中下拉框内容
# time.sleep(3)
# driver.find_element_by_xpath('//*[@id="collapseOne"]/div/div[3]/button').click()
#driver.find_element_by_xpath('//*[@id="toolbar"]/a[1]').click() #点击新增产品
#time.sleep(3)
# driver.find_element_by_id('productName').send_keys("test")
# driver.find_element_by_id('productPrice').send_keys('100')
# driver.find_element_by_id('productContent').send_keys("test")
# driver.find_element_by_xpath('//*[@id="createForm"]/div[3]/a[1]').click()
# time.sleep(3)
# js = "window.scrollTo(0,300)"  # 针对Chrome有效
# driver.execute_script(js)
# driver.find_element_by_xpath('//*[@id="main"]/div[1]/div[2]/div[4]/div[1]/span[2]/span/button').click()
# driver.find_element_by_xpath('//*[@id="main"]/div[1]/div[2]/div[4]/div[1]/span[2]/span/ul/li[4]/a').click() #获取最大数据
# driver.find_element_by_xpath('//*[@id="main"]/div[1]/div[2]/div[1]/table/thead/tr/th[6]/div[1]').click()
#driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[3]/td[1]').click()
# checks=driver.find_elements_by_xpath(".//*[@type='checkbox']")
# checks[10].click()
# print(len(checks))
# for i in checks:
#     print(i)
#print(res)
# driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[6]/td[2]').click()
# j=driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[6]/td[2]').text
# print(j)


# """
# 根据table的id属性和table中的某一个元素定位其在table中的位置
# table包括表头，位置坐标都是从1开始算
# tableId：table的id属性
# queryContent：需要确定位置的内容
# """
#
# from selenium.webdriver.common.by import By
# def get_table_content(tableId, queryContent):
#     # 按行查询表格的数据，取出的数据是一整行，按空格分隔每一列的数据
#     table_tr_list = driver.find_element(By.ID, tableId).find_elements(By.TAG_NAME, "tr")
#     print(len(table_tr_list))
#     table_list = []  # 存放table数据
#     for tr in table_tr_list:  # 遍历每一个tr
#         # 将每一个tr的数据根据td查询出来，返回结果为list对象
#         table_td_list = tr.find_elements(By.TAG_NAME, "td")
#         row_list = []
#         print(table_td_list)
#         for td in table_td_list:  # 遍历每一个td
#             print(td.text)
#             row_list.append(td.text)  # 取出表格的数据，并放入行列表里
#         table_list.append(row_list)
#
#     # 循环遍历table数据，确定查询数据的位置
#     for i in range(len(table_list)):
#         for j in range(len(table_list[i])):
#             if queryContent == table_list[i][j]:
#                 # print(i)
#                 # print(j)
#
#                 # print(s_td)
#                 # print(s_tr)
#                 # driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[6] / td[2]').click()
#                 # driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[s_tr] / td[s_td]').click()
#                 driver.find_element_by_xpath(f"//*[@id='table']/tbody/tr[{i}]/td[{j+1}]").click()
#                 #// *[ @ id = "table"] / tbody / tr[6] / td[2]
#                 print("%r坐标为(%r,%r)" % (queryContent, i + 1, j + 1))
#                 break
#         else:
#             continue
#         break
#
#
# get_table_content('table', "test")


