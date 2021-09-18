#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# My nephew showed me that there was a number guessing technique based on binary math. This code prints the cards
# that let you do the trick. Or https://web.northeastern.edu/seigen/11Magic/Binary/magic_trick_instr.pdf is a
# write-up of how it works. If that link dies, try googling "binary card trick".
import math
import sys


def range_inclusive(start, end):
    return range(start, end + 1)


def power_of_two_generator(final_exponent):
    return (1 << p for p in range_inclusive(0, final_exponent))


def numbers_with_bit_set(power_of_two, max_number):
    return [i for i in range_inclusive(1, max_number) if i & power_of_two]


def generate_cards(max_number):
    card_count = int(math.log2(math.ceil(max_number)))
    return [[card_number, numbers_with_bit_set(card_number, max_number)]
            for card_number in power_of_two_generator(card_count)]

def main(args):
    if len(args) != 2:
        exit(f"Usage: {args[0]} one-to-this-value")
    for card in generate_cards(int(args[1])):
        print(card)

if __name__ == '__main__':
    main(sys.argv)
