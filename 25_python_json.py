"""

    Json
        轻量级的数据交换语言 用来传输由属性值活着序列性的值 组成的数据对象

    json.dumps() 将Python对象编码称Json字符串
        参数
        (obj, *, skipkeys=False, ensure_ascii=True, check_circular=True,allow_nan=True, cls=None, indent=None, separators=None,default=None, sort_keys=False, **kw)
        obj             要序列化的对象
        skipkeys        默认为false   如果为true 则将跳过不是基本类型的dict键 不会引发typeerror
        ensure_ascii    默认值True，如果dict内含有non-ASCII的字符，则会类似\uXXXX的显示数据，设置成False后，就能正常显示
        check_circular  默认值为true  若为false 则将跳过对容器类型的循环引用检查 循环引用将导致overflowerror
        allow_nan       默认值为true  若为false 则严格遵守json规范
        indent          设置缩进格式   默认值为none 选择的是最紧凑的表示
        separators      去除分隔符后面的空格 默认值为none
        sort_keys       默认值为false 如果sort_keys为true 则字典的输出将按键值排序

    json.loads() 将已编码的Json字符串解码为python对象
        参数
        (s, *, cls=None, object_hook=None, parse_float=None,parse_int=None, parse_constant=None, object_pairs_hook=None, **kw):
        s               将s反序列化为python对象
        object_hook     默认值为none 是一个可选函数 用于实现自定义解码器
        parse_float     默认值为none 如果指定了parse_float 用来对json float字符串进行解码 这可用于为json整数使用另一种数据类型或解析器
        parse_constant


    https://www.cnblogs.com/loleina/p/5623968.html

"""

import json
data = {"type": "dic1", "username": "bai", "age": 20}

# 转换为json
# 排序 且 缩进为2
js_encode = json.dumps(data, sort_keys=True, indent=2)
print(js_encode)

# 转换为python对象
js_decode = json.loads(js_encode)
print(js_decode)
