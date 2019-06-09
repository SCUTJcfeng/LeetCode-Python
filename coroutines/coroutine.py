# !/usr/bin/python3.6
# -*- coding:utf-8 -*-
'''
Project: coroutines
Author: jc feng (jcfeng2013@gmail.com)
File Created: 2019-06-10 00:25:31
Last Modified: 2019-06-10 00:33:04
'''

from inspect import getgeneratorstate


def simple_coroutine():
    print('start coroutine')
    x = yield
    print(f'coroutine get {x}')


if __name__ == "__main__":
    # GEN_CREATE:等待开始执行
    # GEN_RUNNING:解释器正在执行，这个状态一般看不到
    # GEN_SUSPENDED:在yield表达式处暂停
    # GEN_CLOSED:执行结束
    my_co = simple_coroutine()  # generator object
    print(getgeneratorstate(my_co))

    next(my_co)  # 激活协程
    print(getgeneratorstate(my_co))

    try:
        my_co.send(1)
    except StopIteration:
        pass

    print(getgeneratorstate(my_co))
