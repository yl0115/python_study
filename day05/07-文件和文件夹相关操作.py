# coding=gbk
# file = open('4.txt', 'w', encoding='utf-8')
# file.write('abc')
# file.close()
import os  # �ļ����ļ��в��������ģ��
import shutil  # �ļ������ĸ߼�ģ��

# ������,Ŀ���ļ�����Ҫ���ڣ��������������򱨴�
# os.rename('4.txt', '444.txt')
# �����ļ���
# os.mkdir("AAA")
# �޸��ļ�����
# os.rename('AAA', 'VVV')

# ���ļ���BBB�д����ļ�
# 1��ָ��·������
# file = open('VVV/t.txt', 'w', encoding='utf-8')
# file.write('ad')
# file.close()
# 2���л���BBBĿ¼������Ĭ��·����py�ļ�����Ŀ¼
# �鿴�ز���Ŀ¼��·��
# current_path = os.getcwd()
# print(current_path)
# �л���ָ��·��
# current_path = os.chdir("VVV")
# curren = os.getcwd()
# print(curren)
# file = open('3.txt', 'w', encoding='utf-8')
# file.write('ac')
# file.close()

# ----------------------------------------------------------------
# �޸��ļ��м��ļ����µ��ļ�
# os.renames('VVV/t.txt', 'CCC/3.txt')

# �鿴Ŀ¼������Щ�ļ����б���Ϣ
# file_name = os.listdir('CCC')
# print(file_name)



# os.chdir('CCC')
# c = os.getcwd()
# print(c)
# ��ǰĿ¼��д������.��ʾ��ǰĿ¼
# file_name = os.listdir(".")
# file_name = os.listdir()
# print(file_name)




# --------------------ɾ���ļ�or�ļ���---------------------------
# ɾ���ļ�
# os.remove("CCC/3.txt")
# ɾ���ļ���
# os.rmdir("CCC")
# rmdirֻ��ɾ����Ŀ¼
# os.rmdir("BBB")


# ɾ��Ŀ¼��
# shutil.rmtree("BBB")


# -----------------------------��չ--------------------------------
# ��ȡ1.txt�ľ���·�����Ӹ�Ŀ¼�����·���ͽ�������·��
# ���·�����ӵ�ǰĿ¼�����·�����ǽ������·��
path = os.path.abspath("1.txt")
print(path)

# ���ݾ���·����ȡ·���е��ļ���
file_name = os.path.basename(path)
print(file_name)

# ��ȡ�ļ������ļ���׺
file_name, file_extend = os.path.splitext(file_name)
print(file_name, file_extend, sep="@")
