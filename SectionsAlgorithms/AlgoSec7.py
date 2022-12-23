import numpy as np
from itertools import permutations
import customtkinter

dec = {
    '$': 0,
    'A': 1,
    'C': 2,
    'G': 3,
    'T': 4
}


def indexingFunction(T, resultLabel):
    T = (T.get())
    table = []
    i = 2**0
    n = 0
    while True:
        l = []
        dec2 = {}
        if i > 1:
            for j in range(len(T)):
                if not (table[n-1][j:j+i] in l):
                    l.append(table[n-1][j:j+i])
            l.sort()
            l
            for j in range(len(l)):
                dec2[tuple(l[j])] = j
        row = []
        for j in range(len(T)):
            if i == 1:
                row.append(dec[T[j]])
            else:
                row.append(dec2[tuple(table[n-1][j:j+i])])
        table.append(row)
        flag = 0
        for j in range(len(row)):
            c = 0
            c = row.count(j)
            if c > 1:
                flag = 1
                break
        print(str(row))
        resultLabel.configure(text="Indexing:" + str(row))

        if flag == 0:
            break
        n += 1
        i = 2**n
