import numpy as np
import bisect
from tkinter import *
import customtkinter


def IndexSorted(seq, ln):
    index = []
    for i in range(len(seq)-ln+1):
        index.append((seq[i:i+ln], i))
    index.sort()
    print(index)
    return index


def query(t, p, lenVar, resultLabel):
    t = (t.get())
    p = (p.get())
    lenVar = int(lenVar.get())
    index = IndexSorted(t, lenVar)
    keys = [r[0] for r in index]
    st = bisect.bisect_left(keys, p[:len(keys[0])])

    en = bisect.bisect(keys, p[:len(keys[0])])
    hits = index[st:en]
    print(hits)
    l = [h[1] for h in hits]
    offsets = []
    for i in l:
        if t[i:i+len(p)] == p:
            offsets.append(i)

    resultLabel.configure(text="query result: " + str(offsets))
