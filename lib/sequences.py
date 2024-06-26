#!/usr/bin/env python3
import ipdb

def print_fibonacci(length):
    if length == 0:
        print('[]')
        return
    elif length == 1:
        print('[0]')
        return
    elif length == 2:
        print('[0, 1]')
        return
    else:
        fib_sequence = [0, 1]
        for _ in range(2, length):
            fib_sequence.append(fib_sequence[-1] + fib_sequence [-2])
        print(fib_sequence)
        