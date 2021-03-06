#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Eli Maor's book says (on page 50) that pi can be approximated with a series:
# 4 - (4 / 3) + (4 / 5) - (4 / 7) + (4 / 9) and so on.


def do_iterate(count):
    sign = 1
    total = 0
    for denom in range(1, count * 2 + 1, 2):
        total = total + 4 * sign / denom
        sign = sign * -1
    return total


if __name__ == '__main__':
    # It takes tens of millions of iterations before you even get to 3.1415926, but it works.
    # So that the tests run fast, I only do those tens of millions of iterations when the code
    # is run manually.
    print(do_iterate(25000000))
