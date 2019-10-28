# 如果外界使用from  包名 import * 不会导入包里面的所有模块，需要使用__all__指定
__all__ = ['first', 'second']

from first_package import *

