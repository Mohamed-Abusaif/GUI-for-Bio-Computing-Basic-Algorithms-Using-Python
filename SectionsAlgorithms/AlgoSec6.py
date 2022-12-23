import numpy as np
from itertools import permutations
import customtkinter
def overlap(a,b,min_length=3):
    start=0
    while True:
        start=a.find(b[:min_length],start)
        if start==-1:
            return 0
        if b.startswith(a[start:]):
            return len(a[start:])
        start+=1


print(overlap("ACGGTAGGT", "GGTAGGTCC",3))

def helperFunction(a,b,resultLabel , min_length=3):   
    a = (a.get())
    b = (b.get())
    j=len(a)-1
    count=0
    for i in range(len(b)-1,-1,-1):
        if a[j]==b[i]:
            count+=1
            j-=1
        else:
            count=0
            j=len(a)-1
            if a[j]==b[i]:
                count+=1
                j-=1
    if count>=min_length:
        print('overlap:',count)
        resultLabel.configure(text="overlap result: " + str(count))
    else:
        print("no overlap")
        resultLabel.configure(text="no overlap!")



 
def native_overlap(reads,k):
    olap={}
    for a,b in permutations(reads,2):
        olen=overlap(a, b,k)
        if olen>0:
            olap[(a,b)]=olen
    return olap

print(native_overlap(["ACGGTA", "GGTACC","GCATACG"],3))



