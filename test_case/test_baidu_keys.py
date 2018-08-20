from selenium.webdriver.common.keys import Keys  # 需要引入 keys 包
from selenium.webdriver.support.ui import Select
from Conf.setting import *
from util.ClientSelenium import ClientSelenium
from util.ParserConfig import ParserConfig

commond = ClientSelenium()
pc = ParserConfig("E:\selenium_uses\Conf\config.ini")


class Baidu_Api(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = commond.get_driver("chrome", "https://www.baidu.com/")
        commond.time_sleep(3)

    @classmethod
    def tearDownClass(cls):
        commond.quit()

    def test_a_Enter(self):
        try:
            commond.click_element("xpath=>//*[@id='u1']/a[8]")  # 定位后在chick()
            commond.click_element("xpath=>//*[@id='wrapper']/div[6]/a[1]")
            commond.click_element("class=>item cur") #*关键部分
            time.sleep(1)
            sl=commond.click_element("xpath=>//*[@id='nr']]")
            Select(sl).first_selected_option()
            Select(sl).select_by_index(2)
            #Select(sl).select_by_visible_text("每页显示20条")
            time.sleep(2)
            # commond.get_element("xpath=>//input[@value='保存设置']").click()
            # time.sleep(2)
            # commond.switch_accept_alert() #确认弹出窗体
        #commond.get_element("id=>q").send_keys(Keys.ENTER)
        except Exception as error:
            print(format(error))


if __name__ == '__main__':
    unittest.main()
