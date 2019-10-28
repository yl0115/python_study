import os


def all_path(dirname):
    result = os.listdir(dirname)
    for i in result:
        num = 1
        result = dirname+"\\"+i
        r = os.listdir(result)
        for value in r:
            old_name = result + '\\' + value
            if value.endswith('.jpg'):
                if '营业执照' in value:
                    continue
                elif '优单合同' in value:
                    continue
                elif '店铺' in old_name:
                    continue
                elif '广告位示意图' in old_name:
                    pass
                else:
                    new_name = result + '\\广告位示意图' + str(num) + '.jpg'
                    os.rename(old_name, new_name)
                    num += 1


if __name__ == '__main__':
    path = r'e:\成都内江\1'
    r_list = os.listdir(path)
    for w in r_list:
        b = path+'\\'+w
        all_path(b)
