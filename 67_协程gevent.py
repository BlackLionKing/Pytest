import gevent
from gevent import monkey
test
""" 
    gevent
        能够自动切换任务
        当greenlet遇到io操作时 就自动切换到其他的greenlet 等到io操作完成 再在适当的时候切换回来继续执行
        
    greenlet
        需要人工切换
     
    gevent常用方法   
    启动协程
    # join()
    休眠
    # sleep()
    返回当前正在执行的greenlet
    # getcurrent()
    创建协程 放进协程池
    # spawn()
    
    打补丁 monkey
    monkey.patch_all()
    会自动将python的一些标准模块替换成gevent框架
    
"""


def func_1(n):
    for i in range(n):
        # 返回当前正在执行的greenlet
        print(gevent.getcurrent(), i)
        gevent.sleep(1)


# 创建三个gevent 放进协程池
g1 = gevent.spawn(func_1, 5)
g2 = gevent.spawn(func_1, 5)
g3 = gevent.spawn(func_1, 5)

# 启动协程
g1.join()
g2.join()
g3.join()
