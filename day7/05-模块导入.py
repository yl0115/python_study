# # ---------------------import导入模块
# import first_module
#
# stu = first_module.Student('张胜', 14)
# print(stu.name, stu.age)

# ---------------------from 模块名 import 导入模块
# from first_module import Student
# stu = Student('王五', 34)
# print(stu.name, stu.age)


# ---------------------from 模块名 import * 使用__all__限定导入的功能代码
# from first_module import *
#
# print(g_num)
# show()

# ---------import 模块名设置别名--
import first_module as first  # 设置模块别名
print(first.g_num)
#







