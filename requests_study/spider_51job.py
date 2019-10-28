import requests
from lxml import etree
from pandas import DataFrame


class Job_Test(object):

    __slots__ = ['urls']

    def __init__(self, urls):
        self.urls = urls

    def xpath_analysis(self):
        res = requests.get(self.urls)
        # 设置编码格式
        res.encoding = 'gbk'
        # 利用etree初始化生成一个Xpath解析对象
        root = etree.HTML(res.text)
        return root

    @staticmethod
    def spider_51job(root):
        """
        利用Xpath提取网页信息
        :param root: 初始化生成的一个Xpath解析对象
        """
        # 招聘职位名
        position = root.xpath('//div/p/span/a/@title')
        # 提取公司名称
        company = root.xpath('//span[@class="t2"]/a/@title')
        # 提取工作地点
        address = root.xpath('//div[@class="el"]/span[@class="t3"]/text()')
        # 提取价格
        java_price = root.xpath('//div[@class="el"]/span[@class="t4"]/text()')
        # 把取出的数据放到数据框中
        job_info = DataFrame([position, company, address, java_price]).T
        job_info.columns = ['职位名称', '公司名称', '工作地点', '薪资']
        return job_info

    @staticmethod
    def write_csv(job_info):
        """
        将数据保存到本地
        :param job_info: 传入的格式化数据
        :return:
        """
        job_info.to_csv('软件测试招聘职位.csv', encoding='utf_8_sig', index=False)


if __name__ == '__main__':
    # 确定爬取目标，网址
    url = r'https://search.51job.com/list/090200,000000,0000,32,9,99,%25E6%25B5%258B%25E8%25AF%2595%25E5%25B7%25' \
          r'A5%25E7%25A8%258B%25E5%25B8%2588,2,1.html'
    # 实例化类
    jt = Job_Test(url)
    # 获取解析对象
    analysis = jt.xpath_analysis()
    # 提取网页数据
    data_51job = jt.spider_51job(analysis)
    # 将数据保存到本地
    jt.write_csv(data_51job)

