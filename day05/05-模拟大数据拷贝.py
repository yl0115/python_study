# coding=gbk
# 1����Դ�ļ���ȡ����
# rbģʽ�ǱȽ�ͨ�õ�ģʽ���Լ��ݲ�ͬ���ļ�
file_src = open('1.txt', 'rb')
# 2����Ŀ���ļ�д������
# ����ָ���ļ�����·��
dst_file = open('3����.txt', 'wb')
# ѭ����ȡ
while True:
    file_data = file_src.read(1024)
    # �ж������Ƿ����
    # if len(file_data) > 0:
    if file_data:
        # ��ʾ������
        # ��ԭ�ļ�������д�뵽Ŀ���ļ�
        dst_file.write(file_data)
    else:
        print("���ݶ�ȡ��ɣ�", file_data)
        break


dst_file.close()
file_src.close()



