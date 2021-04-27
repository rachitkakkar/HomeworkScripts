#!/usr/bin/env python

# TOGGLE THESE VALUES
equation1 = '10 - x' # y = 10 - x
equation2 = 'x / (5 / 8)' # y = x / (5 / 8)

check_until = 100 # We check all the fractions from 1/1 to check_until / check_until. So for example it would go 1 / 1, 1 / 2, ..., 1 / 100, ..., 100 / 1, 100 / 2, ..., 100 / 100
depth = 3 # The amount we round answers to (we need to set this otherwise super small decimals might break this program)

# CALCULATE
for i in range(1, check_until):
    for j in range(1, check_until):
        formated1 = equation1.replace('x', str(i / j))
        formated2 = equation2.replace('x', str(i / j))

        if round(eval(formated1), depth) == round(eval(formated2), depth):
            print(f'Intersection found at x: {i}/{j} y: ~{round(eval(formated1), depth)}!')