# coding=gbk
# ��ʾ�������쳣�඼�Ǽ̳�Exception
# try:
#     # ���ܷ����쳣�Ĵ��룬�ŵ�try�������
#     num1 = input("�������һ�����֣�")
#     num2 = input("������ڶ������֣�")
#     result = int(num1)+int(num2)
#     print(result)
# except Exception as e:  # e��ʾ�쳣����
#     # ���񵽵��쳣����except������д���
#     print("������Ϸ�����")
#     print(e)
# num1 = input("�������һ�����֣�")
# num2 = input("������ڶ������֣�")
# result = int(num1)+int(num2)
# print(result)


# �˽⣺���Բ������쳣����
try:
    name = 'zs'
    # del name
    # ��try���������˴����쳣����ô������ִ��try����Ĵ��룬��ֱ��ִ��except
    print(name)
    result = 1/1
    print(result)
except (NameError, ZeroDivisionError) as e:
    print(e, type(e))
else:
    print("û���쳣��ִ��else")
finally:
    print("��û���쳣����ִ��finally")

