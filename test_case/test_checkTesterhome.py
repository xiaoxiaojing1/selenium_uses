

from util.Base import Base

base = Base()
try:
    from util.ClientSelenium import ClientSelenium
    import unittest,time

except ImportError as error:
    print(error)
client = ClientSelenium()

class TestDemo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        client.get_driver("Ch","https://testerhome.com/")
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        client.quit()

    def test_login(self):
        ele = client.get_window_handle() #打印句柄
        print("ele[0]", ele)
        client.start("https://testerhome.com/questions","https://testerhome.com")
        client.click_element("xpath=>/html/body/div[1]/nav/div/ul[1]/li[2]/a")
        time.sleep(2)

    def test_send_keys(self):
        """
        xxxx
        :return:
        """
        try:
            client.check_element("id=>user_login","yejin-son")
            time.sleep(2)
            client.check_element("id=>user_password", "zhangquandan")
            time.sleep(2)
            client.click_element("id=>user_remember_me")
            time.sleep(2)
            client.click_element("name=>commit")
        except Exception as error:
            client.get_windows_img(r"D:\selenium_uses\Pic\test_send_keys.png")

if __name__ == '__main__':
    unittest.main()


