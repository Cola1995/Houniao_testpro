from selenium.webdriver.common.by import By
from BasePage import BasePage

import time


# 继承BasePage类
class InformationPage(BasePage):
    # 定位器，通过元素属性定位元素对象
    username_loc = (By.ID, 'username')
    password_loc = (By.ID, 'password')
    submit_loc = (By.ID, 'login-bt')
    span_loc = (By.CSS_SELECTOR, "div.error-tt>p")
    dynpw_loc = (By.ID, "lbDynPw")
    userid_loc = (By.ID, "spnUid")
    information_loc = (By.XPATH, '//*[@id="mCSB_1_container"]/ul/li[4]/a')  # 一级菜单综合信息管理
    gonggao_loc = (By.XPATH, '//*[@id="mCSB_1_container"]/ul/li[4]/ul/li[5]/a')  # 公告管理
    frame_loc=(By.TAG_NAME,'iframe')
    addtitle_loc=(By.XPATH,'//*[@id="toolbar"]/a[1]')  #添加公告按钮
    title_loc=(By.ID,'syntheticalTitle')           #标题输入框
    titlelink_loc=(By.ID,'syntheticalLink')       #文章链接输入框
    savebutton_loc=(By.XPATH,'//*[@id="createForm"]/div[3]/a[1]') # 保存按钮
    textarea_loc=(By.XPATH,'/html/body')   #文本框位置
    count_loc=(By.XPATH,'//*[@id="main"]/div[1]/div[2]/div[4]/div[1]/span[1]')
    refush_loc=(By.XPATH,'//*[@id="main"]/div[1]/div[1]/div[2]/button')
    ctime_loc=(By.XPATH,'//*[@id="main"]/div[1]/div[2]/div[1]/table/thead/tr/th[4]/div[1]')   #创建时间
    check_loc=(By.XPATH,'//*[@id="table"]/tbody/tr[1]/td[3]')    #第一条记录
    deltitle_loc=(By.XPATH,'//*[@id="toolbar"]/a[2]')   #删除文章按钮
    quren_loc=(By.XPATH,'/html/body/div[2]/div[2]/div/div/div/div/div[4]/button[1]')   #确认按钮
    # 操作
    # 通过继承覆盖（Overriding）方法：如果子类和父类的方法名相同，优先用子类自己的方法。
    # 打开网页
    def open(self):
        # 调用page中的_open打开连接
        print("子类open")
        self._open(self.base_url, self.pagetitle)

    # 输入用户名：调用send_keys对象，输入用户名
    def input_username(self, username):
        #        self.find_element(*self.username_loc).clear()
        self.find_element(*self.username_loc).send_keys(username)

    # 输入密码：调用send_keys对象，输入密码
    def input_password(self, password):
        #        self.find_element(*self.password_loc).clear()
        self.find_element(*self.password_loc).send_keys(password)

    # 点击登录：调用send_keys对象，点击登录
    def click_submit(self):
        time.sleep(5)  # 预留时间手动输入验证码
        self.find_element(*self.submit_loc).click()

    # 用户名或密码不合理是Tip框内容展示
    def show_span(self):
        return self.find_element(*self.span_loc).text

    # 切换登录模式为动态密码登录（IE下有效）
    def swich_DynPw(self):
        self.find_element(*self.dynpw_loc).click()

    # 登录成功页面中的用户ID查找
    def show_userid(self):
        return self.find_element(*self.userid_loc).text


    #点击一级页面综合信息管理
    def information_click(self):
        self.find_element(*self.information_loc).click()
    #点击告管理
    def gonggao_click(self):
        self.find_element(*self.gonggao_loc).click()

    #切换至frame
    def toframe(self):
        frame1=self.find_element(*self.frame_loc)
        self.switch_frame(frame1)

    #点击新增文章按钮
    def addtitle(self):
        self.find_element(*self.addtitle_loc).click()
    #输入title内容，调用send_keys对象
    def write_title(self,title):
        self.find_element(*self.title_loc).send_keys(title)

    #输入链接内容，调用send_keys对象
    def  add_link(self,link):
        self.find_element(*self.titlelink_loc).send_keys(link)

    #调用find_elemet对象点击保存
    def sava(self):

        self.find_element(*self.savebutton_loc).click()

    def neiron(self,txt):
        self.find_element(*self.textarea_loc).send_keys(txt)


    def count(self):
        text1=self.find_element(*self.count_loc).text
        return text1[-5]

    def refush(self):
        self.find_element(*self.refush_loc).click()

    def ctime_click(self):
        self.find_element(*self.ctime_loc).click()

    def first_check(self):
        self.find_element(*self.check_loc).clicK()


    def deltitle_click(self):
        self.find_element(*self.deltitle_loc).click()

    def q_click(self):
        self.find_element(*self.quren_loc).click()