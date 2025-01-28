#!/usr/bin/python3

import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

n = sys.argv[1]

if not n.isdigit():
    print("N must be a number")
    exit(1)

n = int(n)
if n < 4:
    print("N must be at least 4")
    exit(1)


def queens(n, i=0, a=[], b=[], c=[]):
    """Find possible positions"""
    if i < n:
        for j in range(n):
            if j not in a and i + j not in b and i - j not in c:
                yield from queens(n, i + 1, a + [j], b + [i + j], c + [i - j])
    else:
        yield a


def solve(n):
    """Solve the N-queens problem"""
    for solution in queens(n):
        print([[i, solution[i]] for i in range(n)])


solve(n)
