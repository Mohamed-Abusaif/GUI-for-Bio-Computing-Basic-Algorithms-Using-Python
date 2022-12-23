import numpy as np
import time
from tkinter import *
import customtkinter


def match(seq,sub_seq , resultLabel):
    seq = (seq.get())
    sub_seq = (sub_seq.get())

    x=-1
    for i in range(len(seq)-len(sub_seq)+1):
        if sub_seq==seq[i:i+len(sub_seq)]:
            x=i
    resultLabel.configure(text="Match: " + str(x))
    return x







def Badchars(seq,sub_seq,resultLabel):
    seq = (seq.get())
    sub_seq = (sub_seq.get())
    table=np.zeros([4,len(sub_seq)])     
    row=["A","C","G","T"]
    for i in range (4):
        num=-1
        for j in range (len(sub_seq)):
            if row[i]==sub_seq[j]:
                table[i,j]=-1
                num=-1
            else:
                num+=1
                table[i,j]=num
    x=-1
    i=0
    while(i<len(seq)-len(sub_seq)+1):
        if sub_seq==seq[i:i+len(sub_seq)]:
            x=i
        
        else:
            for j in range(len(sub_seq)-1,-1,-1):
                if seq[i+j] != sub_seq[j]:
                    k=row.index(seq[i+j])
                    i+=table[k,j]
                    break
                
        '''
        else:
            for j in range(i+len(sub_seq)-1,i-1,-1):
                if seq[j] != sub_seq[int(j-i)]:
                    k=row.index(seq[j])
                    i+=table[k,j-i]
                    break
        '''
        i=int(i+1)
    resultLabel.configure(text="Bad Chars: " + str(x))
    return x







