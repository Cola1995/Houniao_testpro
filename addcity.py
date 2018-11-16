from selenium import  webdriver
import time
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.maximize_window()
driver.get('http://124.95.129.86:9000/manage/index')
driver.find_element_by_id("username").send_keys("guanliyuan")
driver.find_element_by_id("password").send_keys("youjian@2018")
time.sleep(5)
driver.find_element_by_id("login-bt").click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="mCSB_1_container"]/ul/li[8]/a').click()  #点击一级城市管理
time.sleep(3)
driver.find_element_by_xpath('//*[@id="mCSB_1_container"]/ul/li[8]/ul/li/a').click() #点击二级菜单城市管理
driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
time.sleep(3)
ul=driver.find_element_by_id('treeDemo')
time.sleep(3)
#li=ul.find_elements_by_tag_name('li')
li=ul.find_elements_by_xpath('//li[@class="level0"]')
for item in li:
    t=item.find_element_by_tag_name('a')
    print(t.get_attribute('title'))
    if t.get_attribute('title')=='安徽省':   #手动更改***省
        t.click()
        city_list=t.find_elements_by_xpath('//a[@class="level1"]')
        break



#print(city_list)
cc=[]
for a in range(len(city_list)):   #获取已添加的省份名称
    print(city_list[a].text)
    cc.append(city_list[a].text)
cc.append('')
print(cc)
time.sleep(3)
driver.find_element_by_id('addSub').click()
time.sleep(3)
city=driver.find_element_by_id('city1')
#all=Select(city).all_selected_options
options_list=city.find_elements_by_tag_name('option')
ac=[]
for ite in range(len(options_list)):  #获取当前省份下所有的市
    allc=options_list[ite].get_attribute('value')
    #print(type(allc))
    ac.append(allc)
    print(allc)
    #all_city.append(options_list[ite].get_attribute('value'))


for ii in ac:
    if ii not in cc:
        print("ii:"+ii)

        time.sleep(3)
        city = driver.find_element_by_id('city1')
        Select(city).select_by_value(ii)
        time.sleep(3)
        driver.find_element_by_id('cityVipCreatePrice').clear()
        driver.find_element_by_id('cityVipCreatePrice').send_keys('1')  #会员费用比率
        time.sleep(3)
        driver.find_element_by_xpath('//input[@id="cityLimit" and @placeholder="最低限额(元)"]').clear()
        driver.find_element_by_xpath('//input[@id="cityLimit" and @placeholder="最低限额(元)"]').send_keys('1000')

        time.sleep(3)
        #driver.find_element_by_id('cityDrivingPrice').send_keys('50')  #代驾费
        driver.find_element_by_xpath('//*[@id="cityDrivingPrice" and @placeholder="代驾费（总额）"]').clear()
        driver.find_element_by_xpath('//*[@id="cityDrivingPrice" and @placeholder="代驾费（总额）"]').send_keys('50')

        time.sleep(3)
        driver.find_element_by_id('cityCreateMaxKm').send_keys('200000') #最大公里数
        time.sleep(3)
        driver.find_element_by_id('cityCreateMaxYear').send_keys('10') #城市要求最大年限
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="createForm"]/div[4]/a[1]').click()  #点击保存

        time.sleep(3)
        ul = driver.find_element_by_id('treeDemo')
        time.sleep(3)
        li = ul.find_elements_by_xpath('//li[@class="level0"]')
        for item in li:
            t = item.find_element_by_tag_name('a')
            print(t.get_attribute('title'))
            if t.get_attribute('title') == '安徽省':        #手动更改某个省
                t.click()
                city_list = t.find_elements_by_xpath('//a[@class="level1"]')
                break

        time.sleep(3)
        driver.find_element_by_id('addSub').click()



