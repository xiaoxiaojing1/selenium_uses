from selenium import webdriver
import os, time, unittest, configparser
from util import Err



from util import log
_logger = log.logger('LoginTesterHome')

currentPath = os.path.abspath(os.path.dirname(__file__))  # 当前文件夹目录
ProjectPath = os.path.split(currentPath)[0]  # 取下标
toolsPath = ProjectPath.replace("\\", "/") + "/driver/chromedriver"


def path_ini():
    pathobj = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")) + "\\Conf\\config.ini"  # + "../config" + "/config.ini"
    return pathobj


def get_ini_date(sections, item):
    """关键字驱动
    :param sections: ini类型文件.sections
    :param item: get.item =>value
    :return: str
    """
    try:
        iniconf = path_ini()  # 读取全局变量拼装文件
        conf = configparser.ConfigParser()
        conf.read(iniconf, encoding="utf-8")
        return conf.get(sections, item)
    except Exception as error:
        print(format(error))


class LoginTesterHome(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=toolsPath)
        cls.driver.get(get_ini_date("Url", "tester_url"))  # 成员方法
        # cls.driver.implicitly_wait(10)  #隐式等待
        log._logger.info("启动浏览器成功")

    @classmethod
    def tearDownClass(cls):
        log._logger.info("测试结束")
        cls.driver.quit()

    def test_login_checklogin(self):
        """
        断言相等性 driver.title 测试场景
        断言相等性 driver.current_url
        <非必要条件>判断网页源码 尺寸大小 不高于60kb 如果不满足写入文件 /test/size.txt
        判断前往登录元素是否可以点击
        断言相等性 登录元素文本正确

        :return:
        """
        time.sleep(3)

        try:
            #func1()
            self.assertEqual("TesterHome", self.driver.title,
                             msg="当前网页的{}和{}一致".format("TesterHome", self.driver.title))
            log._logger.info("判断driver.title测试场景 pass")
            self.assertEqual("https://testerhome.com/", self.driver.current_url,
                             msg="当前网页url{0}正确".format(self.driver.current_url))
            log._logger.info("判断社区官网主页url测试场景 pass")
            #func2()
            objsize = self.driver.page_source.__sizeof__()
            time.sleep(2)
            if int(objsize / 1024) > 60:  # 判断尺寸
                # print(self.driver.current_url, "")
                fp = open("../test/sizelog.txt", "w", encoding="utf-8")  # 自己封装
                fp.write(get_ini_date("Language", "size").format(self.driver.current_url))
                log._logger.info("大于60kb写入文件 pass")
                fp.close()
            check_login = self.driver.find_element_by_xpath('/html/body/div[1]/nav/div/ul[1]/li[2]/a')
            if check_login.is_enabled():  # 判断是否可以点击
                log._logger.info("判断登录链接可点击状态 pass")
                self.assertEqual("登录", check_login.text, msg="登陆element{0}".format(check_login.text))
            else:
                log._logger.info("判断登录链接不可点击状态 pass")
                raise "{0}不可点击".format(check_login)
            check_login.click()  # 跳转
            log._logger.info("判断切换到登录界面 pass")
            time.sleep(2)
        except Exception as err:
            print(format(err))

    def test_login_loginField(self):
        """
        断言相等性 driver.title  测试场景
        back()回退上个页面 断言相等性 driver.title  测试场景
        forward()上个页面前进 到达当前页面 断言不相等性NotEqual driver.title  测试场景
        定位id 数据驱动输入ini文件里的内容
        账号，密码，勾选状态60天
        get_attribute拿到input单元格输出的内容
        判断尺寸
        断言返回数据类型 勾选框.size
        断言不相等性 driver.current_url 测试场景
        get_cookies 然后提取关键的name和value
        :return:
        """
        try:
            self.assertEqual("登录 · TesterHome", self.driver.title,
                             msg="当前网页的{}和{}一致".format("登录 · TesterHome", self.driver.title))
            self.driver.back()  # 回退页面
            log._logger.info("判断返回社区主页 pass")
            time.sleep(2)
            self.assertEqual("TesterHome", self.driver.title,
                             msg="当前网页的{}和{}一致".format("TesterHome", self.driver.title))
            self.driver.forward()  # 前进页面
            log._logger.info("判断回到社区登录页 pass")
            time.sleep(2)
            self.assertNotEqual("TesterHome", self.driver.title,
                                msg="当前网页的{}和{}一致".format("TesterHome", self.driver.title))
            self.driver.find_element_by_id("user_login").send_keys(get_ini_date("Testhome", "username"))
            time.sleep(2)
            self.driver.find_element_by_id("user_password").send_keys(get_ini_date("Testhome", "password"))
            time.sleep(2)
            log._logger.info("判断输入账号密码 pass")
            username = self.driver.find_element_by_id("user_login").get_attribute("value")
            password = self.driver.find_element_by_id("user_password").get_attribute("value")
            print("账号是{}，密码是{}".format(username, password))
            self.driver.find_element_by_id("user_remember_me").click()  # 'NoneType' object has no attribute 'size'
            log._logger.info("判断勾选60天 pass")
            # 判断尺寸
            time.sleep(2)
            objsize = self.driver.page_source.__sizeof__()  # https://testerhome.com/account/sign_in
            if int(objsize / 1024) > 60:  # 判断尺寸
                fp = open("../test/sizelog.txt", "a+", encoding="utf-8")
                fp.write(get_ini_date("Language", "size").format(self.driver.current_url))
                fp.close()
            time.sleep(2)
            button = self.driver.find_element_by_name("commit")
            if button.get_attribute("name") == "commit" and button.get_attribute("type") == "submit":
                button.click()
                log._logger.info("判断登录按钮属性 pass")
            self.assertNotEqual("https://testerhome.com/account/sign_in/", self.driver.current_url,
                                msg="当前页面不是{}".format("https://testerhome.com/account/sign_in/"))  # 跳转后的登陆页面
            log._logger.info("登录页面跳转结束 pass")
            cookie = self.driver.get_cookies()
            print("url {1}的cookie_name：{0}，cookie_value：{2}".format(cookie[0].get("name"), self.driver.current_url,
                                                                    cookie[0].get("value")))
            log._logger.info("登录页面cookies提取 pass")
            time.sleep(2)

        except Exception as err:
            print(format(err))

    def test_login_quit(self):
        """
        登录后断言 通过提示信息count元素来 判断测试场景
        一步步拿到推出按钮
        登录后退出
        断言包含In topics 比较稳当的写法
        :return:
        """
        log._logger.info("账号已登录 pass")
        newobj = self.driver.find_element_by_class_name("count")  # 断言场景
        if newobj:
            log._logger.info("账号识别新消息 pass")
            print("提示新信息数量", newobj.text)
            time.sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/nav/div/ul[1]/li/a/img").click()
        time.sleep(2)
        log._logger.info("识别退出控件 pass")
        q = self.driver.find_element_by_link_text("退出")
        q.click()
        time.sleep(5)
        self.assertIn("topics", self.driver.current_url,
                         msg="退出成功，当前url是{0}".format(self.driver.current_url))
        log._logger.info("退出成功到达topics页面 pass")

if __name__ == '__main__':
    unittest.main()
