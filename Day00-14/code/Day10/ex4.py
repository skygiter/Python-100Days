"""
引发异常和异常栈


Date: 2018-03-13
"""


def f1():
    raise AssertionError('发生异常')


def f2():
    f1()


def f3():
    f2()


f3()
