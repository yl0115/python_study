# 自定义模块名字和变量名的定义很类似，都是由字母、数字、下划线组成，但是不能以数字开头，否则无法导入该mok
# 模块名的命名规则和变量名的命名规则一样，统一使用下划线命名法

import first_module  # 导入模块
import second_module

# # 使用模块中的功能
# print(first_module.g_num)
# first_module.show()
# first_module.Student('李四', 20).show_msg()

result = second_module.sum_num(3, 2)
print("自定义模块", result)
