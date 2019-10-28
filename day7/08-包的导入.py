# -----import导入包里面的模块----
# import first_package.first
# import first_package.second
#
# first_package.first.show()
# first_package.second.show_msg()

# -----import导入包里面的模块设置别名----
# import first_package.first as one
# import first_package.second as two
# one.show()
# two.show_msg()

# from导入包名  import 模块名
# from first_package import first as one
# from first_package import second as two
#
# one.show()
# two.show_msg()

# from 包名.模块名 import 功能代码
# from first_package.first import show
# from first_package.second import show_msg
#
# show()
# show_msg()

# ----from  包名 import *,默认不会导入包里面的所有模块，需要在init指定
# from first_package import *
# first.show()
# second.show_msg()


# import first_package  # 直接导入包，不会导入对应的模块，需要在init文件导入
# first_package.first.show()

