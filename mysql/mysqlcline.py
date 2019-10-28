import pymysql
import os
from xpinyin import Pinyin
from time import strftime


class SQL_Connect(object):
    def __init__(self):
        # 初始化数据库连接信息
        self.db = pymysql.connect('192.168.3.250', 'root', 'root', 'youdan')
        # 获取游标
        self.cursor = self.db.cursor()
        # 初始化店铺地址
        self.address = None
        # 员工姓名
        self.staff = None
        # 广告位主信息
        self.advertising = None
        # 身份信息
        self.id_card = None
        # 电话号码
        self.tel = None
        # 绝对地址
        self.abspath = None

    def read_adress(self, paths):
        """
        :param paths: 传递文件的路劲
        :return:
        """
        # 循环遍历paths路劲下的所有文件及文件夹
        for i in os.listdir(paths):
            # 拼接地址
            self.abspath = paths + '\\' + i
            # 判断拼接的绝对路劲后缀是否为.txt结尾
            if self.abspath.endswith('.txt'):
                # 打开txt文件
                with open(self.abspath, 'r', encoding='utf-8') as f:
                    # 读取第一行地址信息
                    self.address = f.readline()
                    # 读取第二行地推人员姓名
                    self.staff = f.readline()
                    # 读取第三行广告位主
                    self.advertising = f.readline()
                    # 读取第四行身份证号码
                    self.id_card = f.readline()
                    # 读取第五行电话号码
                    self.tel = f.readline()
                # 向advertising_position表中插入一条读取数据
                sql = "insert into advertising_position (linkman, link_tel, install_location) VALUES('%s', '%s', '%s')"\
                      % (self.advertising, self.tel, self.address)
                # 获取游标
                cursor = self.db.cursor()
                # 执行sql语句
                cursor.execute(sql)
                # 事务提交
                self.db.commit()
                # 关闭数据连接
                # self.db.close()

    def select_position(self):
        """
        :return:Returns the collection of dictionaries for which data was just inserted
        """
        # 查询advertising_position表中查询刚插入的数据
        sql = "select * from advertising_position where linkman='%s'" % self.advertising
        # 获取游标
        cursor = self.db.cursor()
        # 执行sql语句
        cursor.execute(sql)
        # 获取字段的描述，默认获取数据库字段名称，重新定义时通过AS关键重新命名即可
        desc = cursor.description
        # 列表表达式把数据组装起来
        data_dict = [dict(zip([col[0] for col in desc], row)) for row in cursor.fetchall()]
        # print(data_dict[0]['id'])
        with open('text.txt', 'w', encoding='utf-8') as f:
            f.write(str(data_dict))
        # self.db.close()
        # return data_dict

    def insert_user(self):
        if self.staff == '':
            pass
        else:
            sql1 = "select * from base_staff order by ID desc limit 1"
            self.cursor.execute(sql1)
            desc = self.cursor.description
            data_dict = [dict(zip([col[0] for col in desc], row)) for row in self.cursor.fetchall()]
            pram_key = data_dict[0]['ID']
            py = Pinyin()
            userlogin = py.get_pinyin(self.advertising, splitter="")
            sql = "insert into base_user (staff_id, user_name, user_login, post, tel, address, activate, sex) values" \
                  " ('%s','%s','%s','地推','%s','四川',1,1)" % (pram_key, self.advertising, userlogin, self.tel)
            cursor = self.db.cursor()
            cursor.execute(sql)
            self.db.commit()
            # self.db.close()

    def insert_property(self):
        """
        :return:property
        """
        list_abspath = self.abspath.split('\\')
        sql = "insert into advertising_property (adress, property_type, property_info) values ('%s',46,'%s')" % (
            self.address, list_abspath[-2])
        cursor = self.db.cursor()
        cursor.execute(sql)
        self.db.commit()
        # self.db.close()

    def insert_master(self):
        """
        :return:master
        """
        sql = "insert into advertising_position_master (name, tel) values ('%s','%s')" % (self.advertising, self.tel)
        self.cursor.execute(sql)
        self.db.commit()
        # self.db.close()

    def select_master(self):
        """
        :return: select * from advertising_position_master order by id DESC limit 1
        """
        sql = "select * from advertising_position_master order by id DESC limit 1"
        self.cursor.execute(sql)
        desc = self.cursor.description
        data_dict = [dict(zip([col[0] for col in desc], row)) for row in self.cursor.fetchall()]
        pram_key = data_dict[0][id]
        return pram_key

    def insert_staff(self):
        if self.staff == "":
            pass
        else:
            # birthday_time = strftime('"%Y-%m-%d %H:%M:%S"')
            sql = "insert into base_staff (name, sex, post, address, telephone) values ('%s'," \
                  "1,'地推','保密','18382414444')" % self.staff
            self.cursor.execute(sql)
            self.db.commit()

    def insert_accessory(self):
        sql1 = "select * from advertising_position_master order by id DESC limit 1"
        self.cursor.execute(sql1)
        desc = self.cursor.description
        data_dict = [dict(zip([col[0] for col in desc], row)) for row in self.cursor.fetchall()]
        sql = "insert into advertising_property_accessory (accessory_type, file_url, position_master_id) values (" \
              "18,'http://img.zhongguoyoudan.com/2af4130f53ba45edacb9d509f767d2d7.jpg','%s')" % data_dict[0]['id']
        self.cursor.execute(sql)
        self.db.commit()
        self.db.close()

    def pinyin(self):
        py = Pinyin()
        userlogin = py.get_pinyin(self.advertising, splitter="")
        print(userlogin)


if __name__ == '__main__':
    # 定义文件路劲
    path = r'E:\商家资料\永川\中山路街道\曾明华经营部'
    # 初始化对象
    sc = SQL_Connect()
    # 调用方法并传入参数
    sc.read_adress(path)
    # 查询产业表刚插入的信息
    sc.select_position()
    # 把广告位主名字变为拼音
    sc.pinyin()
    # 向员工表中插入一条信息
    sc.insert_staff()
    # 向用户表插入一条数据
    sc.insert_user()
    # 向产权表中插入一条数据
    sc.insert_property()
    # 向广告位主插入一条数据
    sc.insert_master()
    # 向附件中插入一条数据
    sc.insert_accessory()


