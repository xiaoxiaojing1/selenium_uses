from configparser import ConfigParser

#ConfigParser()实例化1个读取ini的赋予对象
#新建1个类读取ini的类 类里面成员方法cf cf绑定ConfigParser()
#cf读取teatdate下面的绝对路径，encode=utf-8

#定义了2个函数方法，完全解耦的
#第一个函数作用是拿到某个集合名称下面的所有内容
#这个通过传统json格式返回的对象是items，包裹dict()  str(int=123) "123"
#第二个函数作用一层层拿，根据某个集合名称下面options的key拿到最终的value
#根据传入的顺序
#def test(a,c,b)
#return a,b,c

class ParserConfig(object):
    def __init__(self,ini_path): #project_path+"\\..."
        self.cf = ConfigParser() #configparser库的类名
        self.cf.read(ini_path,encoding="utf-8") #ini_path读出来以后=cf.read 返回是cf

    def get_item_section(self, sectionName):
        "获取配置文件指定的section下面的所有的内容"
        optionsDict = dict(self.cf.items(sectionName))
        return optionsDict #字典

    def get_option_value(self, sectionName, optionName):
        "返回对应option键值对的value"
        value = self.cf.get(sectionName, optionName)
        return value

#实例化
#第一件事情拿到Url下面所有的集合
#第二件事情拿到阿里url的value


