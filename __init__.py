"""
    __init__.py常用的作用是标识一个文件夹是一个 python包。
    另一个作用是定义模糊导入时要导入的内容
        当我们使用类似 from package import * 的导入语句的时候就是在使用模糊导入了，
        这时包的编写者就可以在__init__.py文件中定义 __all__ 来限制模糊导入的内容。
        这样可以避免将一些只在包内使用的方法或变量暴露给用户

"""
