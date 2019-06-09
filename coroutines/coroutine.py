# !/usr/bin/python3.6
# -*- coding:utf-8 -*-
'''
Project: coroutines
Author: jc feng (jcfeng2013@gmail.com)
File Created: 2019-06-10 00:25:31
Last Modified: 2019-06-10 00:52:54
'''

from inspect import getgeneratorstate


def simple_coroutine():
    print('start coroutine')
    x = yield
    print(f'coroutine get {x}')


def def_test():
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


# 子生成器
def avg_gen():
    avg = 0
    count = 0
    total = 0
    while True:
        new_num = yield avg
        if new_num is None:
            break
        count += 1
        total += new_num
        avg = total / count
    return avg


# 委托生成器
def proxy_gen():
    while True:
        # 只有子生成器要结束（return）了，yield from左边的变量才会被赋值，后面的代码才会执行。
        res = yield from avg_gen()  # yield from 后接 (generator object)
        print(f'res is {res}')


# 调用方
def test_gen_avg():
    calc_avg = proxy_gen()
    next(calc_avg)
    print(calc_avg.send(10))
    print(calc_avg.send(20))
    print(calc_avg.send(30))
    print(calc_avg.send(None))


if __name__ == "__main__":
    # def_test()
    test_gen_avg()
