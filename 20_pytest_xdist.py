"""
    场景
        一千条case 一条case执行1分钟 一个程序执行需要1000分钟
        如果开十个程序执行 则只需要100分钟 这就是一种并行测试 分布式场景

    解决
        pytest分布式执行插件 pytest-xdist
        多个cpu or 主机执行

        前提：用例之间都是独立的 没有先后顺序 可随机/重复执行 且不会影响其他用例

    pytest-xdist是属于进程级别的并发


    执行命令
         pytest -s -v 21_test_pytest_html.py -n auto
            -n auto 可以自动检测系统的cpu核数

        指定需要多少个cpu来跑case 4个
            pytest -s -v 21_test_pytest_html.py -n 4

    pytest-xdist按照一定顺序执行
        pytest -s -v 21_test_pytest_html.py -n 4 --dist=loadscope
        --dist=loadscope
            将按照同一个模块module下的函数和同一个测试类class下的方法来分组
            然后将每个测试组发给可以执行的worker 确保同一个组的测试用例在同一个进程中执行
            目前无法自定义分组 按类class分组优先于按模块module分组

        --dist=loadfile
            按照同一个文件名来分组 然后将每个测试组发给可以执行的worker
            确保同一个组的测试用例在同一个进程中执行

"""

