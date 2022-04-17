#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from threading import Thread
import math

"""
С использованием многопоточности для заданного значения найти сумму ряда с точностью члена ряда по абсолютному
значению 1e-07 и произвести сравнение полученной суммы с контрольным значением функции для двух бесконечных
рядов.
"""

CONST_ABSOLUTE = 1e-07


def value_y():
    return math.log(math.sqrt((1 + 0.35) / (1 - 0.35)))


def sum_1():
    x = 0.35
    previous = 0
    s = 0
    n = 0
    curr = (math.pow(x, (2 * n - 1)) / (2 * n - 1))
    s += curr
    n += 1
    while abs(curr - previous) > CONST_ABSOLUTE:
        previous = curr
        curr = (math.pow(x, (2 * n - 1)) / (2 * n - 1))
        n += 1
        s += curr
    return s


def sum_2():
    x = 1
    previous = 0
    s = 0
    n = 0
    curr = (math.pow(x, n) * math.pow(math.log(3), n)) / math.factorial(n)
    s += curr
    n += 1
    while abs(curr - previous) > CONST_ABSOLUTE:
        previous = curr
        curr = (math.pow(x, n) * math.pow(math.log(3), n)) / math.factorial(n)
        n += 1
        s += curr
    return s


def compare(x, y):
    result = x - y
    print(f"Результат сравнения {result}")


if __name__ == '__main__':
    th1 = Thread(target=compare(sum_1(), value_y()))
    th1.start()
    th2 = Thread(target=compare(sum_2(), value_y()))
    th2.start()
    th1.join()
    th2.join()