# coding=gbk
# 1����Դ�ļ���ȡ����
# rbģʽ�ǱȽ�ͨ�õ�ģʽ���Լ��ݲ�ͬ���ļ�
file_src = open('1.txt', 'rb')
# ��ȡ�ļ�ȫ������
file_data = file_src.read()
# 2����Ŀ���ļ�д������
# ����ָ���ļ�����·��
dst_file = open('3����.txt', 'wb')
# ��ԭ�ļ�������д�뵽Ŀ���ļ�
dst_file.write(file_data)

dst_file.close()
file_src.close()



