try:
    from util.ClientSelenium import ClientSelenium
    from util.ParserConfig import ParserConfig
    from Conf.setting import *
    from Conf1.setting import *
    #导入的是Conf模块文件夹下面的setting里面所有内容，setting.py的内容可以直接使用
except ImportError as error:
    print(error)

commond =ClientSelenium()
pc =ParserConfig("D:\selenium_uses\Conf\config.ini")
from util import log
_logger = log.logger('Baidu_Api')

class Baidu_Api(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver =commond.get_driver("chrome","https://www.baidu.com")
        log._logger.info("启动浏览器")
        commond.time_sleep(3)

    @classmethod
    def tearDownClass(cls):
        log._logger.info("执行，关闭浏览器")
        commond.quit()

    #条件满足则不会跳过
    #@unittest.skipIf(exe_or_not['assert_title'],'判断assert_title:%s'%exe_or_not['assert_title'])
    def test_a_Tittle(self):
        #print("调式title",pc.get_option_value("Title","baidu_tt"))
        #res修改了
        try:
            log._logger.info("验证网站的tittle")
            res =commond.assert_title(pc.get_option_value("Title","baidu_tt")) #断言title
            self.assertTrue(res,"百度的title验证正确")
        except Exception as error:
            commond.get_windows_img(r"E:\selenium_uses\Pic\test_a_Tittle")
            #os.path.join()
    # 条件不满足则跳过
    #@unittest.skipIf(exe_or_not['assert_source'], '判断assert_source:%s' % exe_or_not['assert_sourcess'])
    def test_a_pagesource(self):
        log._logger.info("把百度设为主页")
        commond.assert_source(["把百度设为主页", "关于百度", "About  Baidu"])

    def test_a_F5(self):
        log._logger.info("刷新百度")
        commond.F5("https://www.baidu.com/") #包含了断言当前网页的功能

    def test_a_setSize(self):
        "先设置最大，在按一定分辨率设置"
        commond.set_size(1024,600)
        log._logger.info("浏览器设置了默认分辨率")
        commond.max_size()

    def test_url_back(self):
        commond.start("http://tieba.baidu.com/","http://tieba.baidu.com/")
        commond.back("https://www.baidu.com")

    def test_url_forward(self):
        commond.forward("http://tieba.baidu.com/")
