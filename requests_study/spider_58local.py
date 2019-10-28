import requests
from lxml import etree
from pandas import DataFrame as df


class Local_Test(object):
    def __init__(self, urls):
        self.urls = urls

    @staticmethod
    def xpath_analysis(urls):
        res = requests.get(urls)
        res.encoding = 'utf-8'
        root = etree.HTML(res.text)
        return root

    @staticmethod
    def spider_58local(root):
        # 获取成都市区县
        area = root.xpath('//p[@class="infor"]/a/text()')
        # 获取小区名字
        village_name = root.xpath('//p[@class="infor"]/a[2]/text()')
        # 获取经纪人公司
        broker = root.xpath('//span[@class="jjr_par_dp"]/@title')
        # 获取经纪人姓名
        name = []
        for i in root.xpath('//span[@class="listjjr"]/text()'):
            name.append(i.strip())
        # 获取描述信息
        describe = []
        for i in root.xpath('//div[@class="des"]/h2/a/text()'):
            describe.append(i.strip())
        # 获取价格
        price = root.xpath('//div[@class="money"]/b/text()')

        local_info = df([area, village_name, broker, name, describe, price]).T
        local_info.columns = ['区县', '小区名称', '经纪人公司', '经纪人', '描述', '价格']
        return local_info

    @staticmethod
    def write_58local(local_info):
        local_info.to_csv('58同城.csv', encoding='utf_8_sig')


if __name__ == '__main__':
    url = r'https://cd.58.com/chuzu/?PGTID=0d100000-0006-6333-1e33-0e0b5e0cee09&ClickID=2'
    lt = Local_Test(url)
    root1 = lt.xpath_analysis(url)
    spider_58local = lt.spider_58local(root1)
    lt.write_58local(spider_58local)

