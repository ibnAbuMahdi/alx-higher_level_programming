#!/usr/bin/python3
""" 101-nqueens.py """


from sys import exit, argv as av
if len(av) != 2:
    print("Usage: nqueens N")
    exit(1)

if not str.isdigit(av[1]):
    print("N must be a number")
    exit(1)

N = int(av[1])

if N < 4:
    print("N must be at least 4")
    exit(1)

sol = []
st = 0
col = []
ldiag = []
rdiag = []
for i in range(N):
    for j in range(st, N):
        tm = min(j + i, N)
        tm2 = max(0, i - (N - j))
        if j not in col and i - j not in ldiag and i - (N - j):
            sol.append([i, j])
            break
