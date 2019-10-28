import os


class Video_Address(object):
    def __init__(self):
        self.num = 0

    def add_VA(self, dirname):
        print(dirname)
        """
        视频地址添加
        :param dirname:
        :return:
        """
        two_folder = os.listdir(dirname)
        print(two_folder)
        for i in two_folder:
            three_folder = dirname+"\\"+i
            with open(three_folder + r'\详细地址.txt', 'w', encoding='utf-8') as f:
                f.write("四川省成都市")
            for j in os.listdir(three_folder):
                abspath = three_folder + '\\' + j
                if abspath.endswith('.mp4'):
                    video_name = three_folder + '\\' + '现场视频00' + str(self.num) + '.mp4'
                    self.num += 1
                    os.rename(abspath, video_name)


if __name__ == '__main__':
    va = Video_Address()
    path = r'E:\成都内江\1'
    r = os.listdir(path)
    for w in r:
        b = path+'\\'+w

        va.add_VA(b)
