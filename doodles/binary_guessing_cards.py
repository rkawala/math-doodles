#!/usr/local/bin/python3
# -*- coding: utf-8 -*-


def power_of_two_generator(final_exponent):
    return (1 << p for p in range(0, final_exponent + 1))
