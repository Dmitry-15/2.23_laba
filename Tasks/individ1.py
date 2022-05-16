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


def value_x(x=0.35):
    return math.log(math.sqrt((1 + x) / (1 - x)))


def value_y(x=1.2):
    return 1/(2 + x)


def sum_1(x):
    s = 0
    n = 0
    curr = 0
    while True:
        previous = (math.pow(x, (2 * n - 1)) / (2 * n - 1))
        n += 1
        if abs(curr - previous) < CONST_ABSOLUTE:
            break
        curr = (math.pow(x, (2 * n - 1)) / (2 * n - 1))
        s += curr
    return s


def sum_2(x):
    s = 0
    n = 0
    curr = 0
    while True:
        previous = (math.pow(x, n) * math.pow(math.log(3), n)) / math.factorial(n)
        n += 1
        if abs(curr - previous) < CONST_ABSOLUTE:
            break
        curr = (math.pow(x, n) * math.pow(math.log(3), n)) / math.factorial(n)
        s += curr
    return s


def compare(first, second, x):
    result = first(x) - second(x)
    print(f"Результат сравнения {result}")


if __name__ == '__main__':
    th1 = Thread(target=compare(sum_1, value_x, 0.35))
    th2 = Thread(target=compare(sum_2, value_y, 1.2))
    th1.start()
    th2.start()
    th1.join()
    th2.join()