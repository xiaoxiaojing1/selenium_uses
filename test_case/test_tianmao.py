# -*- coding: utf-8 -*-
'a practice of ...'
import time,os
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
import unittest
import configparser
from util.ClientSelenium import ClientSelenium
from util import log

_logger = log.logger('TiamMaoMethods')

def path_ini():
    path_ini = os.path.abspath(os.path.dirname(__file__)) + "/../Conf" + "/config.ini"
    return path_ini

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
    except NoSuchElementException as error:
        raise (error)
    return conf.get(sections.lower(), item.lower())  # ini那头全部写成小写，加这句配置大小写填错也无所谓



DEBUG = True
client =ClientSelenium()

class TiamMaoMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        url = "https://www.tmall.com/"
        #cls.driver = webdriver.Chrome(executable_path=get_ini_date('chrome', 'path'))
        client.get_driver("ch",url)
        _logger.info("启动浏览器成功")

    @classmethod
    def tearDownClass(cls):
        time.sleep(10)  # 等待加载，时间根据业务来
        client.quit()

    def test_a_indexUrl(self):
        """

        :return:
        """
        try:
            if DEBUG:#展示锁
                time.sleep(5)
            tt = client.assert_title("理想生活")
            self.assertTrue(tt,msg="判断正确")
            if DEBUG:
                _logger.info("进入天猫")
        except NoSuchElementException as err:
            print(format(err))

    def test_b_searchBooks(self):
        """
        查询天猫 java编程思想这本书
        使用封装这里节省了7行代码
        :return:
        """
        try:
            if DEBUG:#展示锁
                time.sleep(5)
            client.check_element('css=>#mq','java编程思想')
            client.click_element("css=>#mallSearch > form > fieldset > div > button")
            _logger.info("进入搜索界面")
        except NoSuchElementException as err:
            print(format(err))

    def test_c_checkBooks(self):
        """
        简单的断言
        :return:
        """
        try:
            if DEBUG:#展示锁
                time.sleep(5)
            tt = client.assert_title("java编程思想")
            #//*[@id="J_ItemList"]/div[2]/div/div[1]/a/img
            self.assertTrue(tt, msg="存在")
            client.click_element('xpath=>//*[@id="J_ItemList"]/div[2]/div/div[1]/a/img')
            if DEBUG:
                _logger.info("进入订单界面")

        except NoSuchElementException as err:
            print(format(err))


if __name__ == '__main__':
    unittest.main()
