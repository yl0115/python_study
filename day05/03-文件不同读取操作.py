# coding=gbk
# file = open('1.txt', "r", encoding='utf-8')
# content = file.read(2)
# print(content)
# file.close()
"""
    read��readline��readlines��ȡ�ļ�����
    ��ȡָ���������ݣ���ʾ�������rģʽ��ȡ����ָ�����ݵĳ���
    ע��㣺��utf-8�����£�һ������ռ�������ֽڣ�һ���ַ�ռ��һ���ֽ�
    rb����ʱ�ֽ���
"""


# ����ָ�����ļ�ָ���ȡ����
file = open('1.txt', 'rb')
# �鿴�ļ�ָ����λ����
result = file.tell()
print(result)
# �����ļ�ָ����λ��
file.seek(4)
result = file.tell()
print(result)
result = file.read()
content = result.decode('utf-8')
print(content)
file.close()



# ��ȡһ������
file = open('1.txt', 'rb')
# ��ȡһ�����ݣ�����ȡ���ݵ�ʱ������'\n'��ʾ��ȡ���ݽ���
value = file.readline()
value = value.decode('utf-8')
print(value)
file.close()


# ����
file = open('1.txt', 'rb')
value = file.readlines()
for i in value:
    print(i.decode('utf-8'), sep="", end="")

