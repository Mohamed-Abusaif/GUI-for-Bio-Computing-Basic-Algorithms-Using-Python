import numpy as np
import pandas as pd

infile = open('HAPPENN_dataset.fasta')
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

infile = open('seq.fasta')
tb=[]
l=[]
for line in infile:
    if line[0]==">":
        l.append(line[1:-1])
    else:
        seq=line[:-1]
        tb.append(seq)

head=['ID','Sequence']
df=pd.DataFrame({"ID":l,"Sequence":tb})
df.to_csv("seq.csv")


df