import yaml

"""
    教程链接 https://www.cnblogs.com/lisa2016/p/11764808.html

    yaml5.1之后 需指定Loader参数
    表示通过默认加载器(FullLoader)禁止执行任意函数
    
    将yaml数据转换为python数据
    yaml.load()
    
    将python数据转换为yaml
    yaml.dump()
    
    
"""

# 将yaml数据转换为python列表
# print(yaml.load("""
#  - 白
#  - 23
#  - 男
#  - 河北
# """, Loader=yaml.FullLoader))

# 将yaml数据转换为python字典
# print(yaml.load("""
# name: bai
# age: 23
# """, Loader=yaml.FullLoader))

# 加载yaml文件内数据转换为python数据类型
# print(yaml.load(open('./data.yaml'), Loader=yaml.FullLoader))

# 将python数据转换为yaml数据
# print(yaml.dump({'b': [1, 2]}))

# 将python数据转换为yaml数据 并保存为文件
with open('./yaml_data.yaml', 'w') as file:
    yaml.dump(data={'b': [1, 2]}, stream=file)

