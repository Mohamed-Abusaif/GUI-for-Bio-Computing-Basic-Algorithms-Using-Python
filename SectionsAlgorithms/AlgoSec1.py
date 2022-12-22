import numpy as np
import pandas as pd
import tkinter
def section1func1(dataset):
    print("hello from section 1 algorithm")
    print("hello form:" + dataset)
    infile = open(dataset)
    tb=[]
    for line in infile:
        if line[0]==">":
            s=line.split("|lcl|")
        else:
            if s[3]=='non-hemolytic' or s[3]=='non-hemolytic\n':
                tb.append([line[:-1],0])
            else:
                tb.append([line[:-1],1])

    print(tb)
    head=['Sequence','y']
    df=pd.DataFrame(tb,columns=head)
    df.to_csv("HAPPENN.csv")
    print(df)
    df = pd.read_csv('./HAPPENN.csv', index_col=0)
    df
    print("new file happen.csv created!")
    return df

    
# def section1func2(file):
#     infile = open('seq.fasta')
#     tb=[]
#     l=[]
#     for line in infile:
#         if line[0]==">":
#             l.append(line[1:-1])
#         else:
#             seq=line[:-1]
#             tb.append(seq)

#     head=['ID','Sequence']
#     df=pd.DataFrame({"ID":l,"Sequence":tb})
#     df.to_csv("seq.csv")


#     df