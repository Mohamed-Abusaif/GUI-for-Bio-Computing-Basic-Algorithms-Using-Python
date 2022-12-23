from tkinter import *
import customtkinter


def GC_Content(seq, resultLabel):
    seq = (seq.get())
    l = float(len(seq))
    num_G = seq.count("G")
    num_C = seq.count("C")
    total = float((num_C)+num_G)/l
    resultLabel.configure(text="Result is: " + str(total))
    return total/l


def Complement(seq, resultLabel=None):
    dic = {"G": "C", "C": "G", "A": "T", "T": "A"}
    newseq = seq.get()
    s = list(newseq)
    for i in range(len(newseq)):
        s[i] = str(dic[newseq[i]])
    s = "".join(s)
    if resultLabel is None:
        return s
    else:
        resultLabel.configure(text="Result is: " + s)
        return s


def Reverse(seq, resultLabel=None):
    newseq = seq.get()
    s = list(newseq)
    s = reversed(s)
    s = "".join(s)

    if resultLabel is None:
        return s
    else:
        resultLabel.configure(text="Result is: " + s)
        return s


def RComplement(seq):
    dic = {"G": "C", "C": "G", "A": "T", "T": "A"}
    s = list(seq)
    for i in range(len(seq)):
        s[i] = str(dic[seq[i]])
    s = "".join(s)
    return s


def RReverse(seq):
    s = list(seq)
    s = reversed(s)
    s = "".join(s)
    return s


def Reverse_Complement(seq, resultLabel):
    seq = (seq.get())
    L = resultLabel
    seq = RReverse(seq)
    seq = RComplement(seq)

    resultLabel.configure(text="Result is: " + seq)
    return seq
