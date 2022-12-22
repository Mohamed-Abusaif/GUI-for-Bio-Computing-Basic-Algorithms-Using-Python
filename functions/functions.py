import tkinter as tk
from functools import partial
def call_result(label_result, n1, n2):
    num1 = (n1.get())
    num2 = (n2.get())
    result = int(num1)+int(num2)
    label_result.config(text="Result is %d" % result)
    return
def GC_Content(label_result, seq):
    seq = (seq.get())
    l=float(len(seq))
    num_G=seq.count("G")
    num_C=seq.count("C")
    total=float((num_C)+num_G)/l
    label_result.config(text="Result is " + str(total))
    return     
def Complement(seq):
    dic={"G":"C","C":"G","A":"T","T":"A"}
    s=list(seq)
    for i in range(len(seq)):
        s[i]=str(dic[seq[i]])
    s="".join(s)
    return s    
def Reverse(seq):
    s=list(seq)
    s=reversed(s)
    s="".join(s)
    return s
def Reverse_Complement(label_result,seq):
    seq = (seq.get())
    L=label_result
    seq=Reverse(seq)
    seq=Complement(seq)
    label_result.config(text="Result is " + seq)
    return 
def Translation_Table(label_result,seq):
    seq = (seq.get())
    dic = {"TTT" : "F", "CTT" : "L", "ATT" : "I", "GTT" : "V",
           "TTC" : "F", "CTC" : "L", "ATC" : "I", "GTC" : "V",
           "TTA" : "L", "CTA" : "L", "ATA" : "I", "GTA" : "V",
           "TTG" : "L", "CTG" : "L", "ATG" : "M", "GTG" : "V",
           "TCT" : "S", "CCT" : "P", "ACT" : "T", "GCT" : "A",
           "TCC" : "S", "CCC" : "P", "ACC" : "T", "GCC" : "A",
           "TCA" : "S", "CCA" : "P", "ACA" : "T", "GCA" : "A",
           "TCG" : "S", "CCG" : "P", "ACG" : "T", "GCG" : "A",
           "TAT" : "Y", "CAT" : "H", "AAT" : "N", "GAT" : "D",
           "TAC" : "Y", "CAC" : "H", "AAC" : "N", "GAC" : "D",
           "TAA" : "*", "CAA" : "Q", "AAA" : "K", "GAA" : "E",
           "TAG" : "*", "CAG" : "Q", "AAG" : "K", "GAG" : "E",
           "TGT" : "C", "CGT" : "R", "AGT" : "S", "GGT" : "G",
           "TGC" : "C", "CGC" : "R", "AGC" : "S", "GGC" : "G",
           "TGA" : "*", "CGA" : "R", "AGA" : "R", "GGA" : "G",
           "TGG" : "W", "CGG" : "R", "AGG" : "R", "GGG" : "G" 
           }
    s=""
    for i in range(0,len(seq)-3,3):
        s+=dic[seq[i:i+3]]
    label_result.config(text="Result is " + s)
    return 
def match(label_result,seq,sub_seq):
    seq = (seq.get())
    sub_seq = (sub_seq.get())
    x=-1
    for i in range(len(seq)-len(sub_seq)+1):
        if sub_seq==seq[i:i+len(sub_seq)]:
            x=i
    label_result.config(text="Result is " + str(x))
    return  
import numpy as np     
def Badchars(label_result,seq,sub_seq):
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
        i=int(i+1)
    label_result.config(text="Result is " + str(x))
    return
# Python3 program for Boyer Moore Algorithm with
# Good Suffix heuristic to find pattern in
# given text string

# preprocessing for strong good suffix rule
def preprocess_strong_suffix(shift, bpos, pat, m):

	# m is the length of pattern
	i = m
	j = m + 1
	bpos[i] = j

	while i > 0:
		
		'''if character at position i-1 is
		not equivalent to character at j-1,
		then continue searching to right
		of the pattern for border '''
		while j <= m and pat[i - 1] != pat[j - 1]:
			
			''' the character preceding the occurrence
			of t in pattern P is different than the
			mismatching character in P, we stop skipping
			the occurrences and shift the pattern
			from i to j '''
			if shift[j] == 0:
				shift[j] = j - i

			# Update the position of next border
			j = bpos[j]
			
		''' p[i-1] matched with p[j-1], border is found.
		store the beginning position of border '''
		i -= 1
		j -= 1
		bpos[i] = j

# Preprocessing for case 2
def preprocess_case2(shift, bpos, pat, m):
	j = bpos[0]
	for i in range(m + 1):
		
		''' set the border position of the first character
		of the pattern to all indices in array shift
		having shift[i] = 0 '''
		if shift[i] == 0:
			shift[i] = j
			
		''' suffix becomes shorter than bpos[0],
		use the position of next widest border
		as value of j '''
		if i == j:
			j = bpos[j]

'''Search for a pattern in given text using
Boyer Moore algorithm with Good suffix rule '''
def GS_search(label_result,seq,sub_seq):
        seq = (seq.get())
        sub_seq = (sub_seq.get())
        # s is shift of the pattern with respect to text
        s = 0
        m = len(sub_seq)
        n = len(seq)

        bpos = [0] * (m + 1)

        # initialize all occurrence of shift to 0
        shift = [0] * (m + 1)

	# do preprocessing
        preprocess_strong_suffix(shift, bpos, sub_seq, m)
        preprocess_case2(shift, bpos, sub_seq, m)

        while s <= n - m:
            j = m - 1
            
            ''' Keep reducing index j of pattern while characters of
                pattern and text are matching at this shift s'''
            while j >= 0 and sub_seq[j] == seq[s + j]:
                j -= 1
                
            ''' If the pattern is present at the current shift,
                then index j will become -1 after the above loop '''
            if j < 0:
                 label_result.config(text="Result is " + str(s))
                 s += shift[0]
                 return
            else:
                
                '''pat[i] != pat[s+j] so shift the pattern
                shift[j+1] times '''
                s += shift[j + 1]
        



     
root = tk.Tk()
root.geometry('400x200+100+200')
root.title('BIO TASK')
number1 = tk.StringVar()
number2 = tk.StringVar()
labelTitle = tk.Label(root, text="BIOCOMPUTING").grid(row=0, column=2)
labelNum1 = tk.Label(root, text="Enter the pattern").grid(row=1, column=0)
labelNum2 = tk.Label(root, text="Enter the text").grid(row=2, column=0)
labelResult = tk.Label(root)
labelResult.grid(row=17, column=2)
entryNum1 = tk.Entry(root, textvariable=number1).grid(row=1, column=2)
entryNum2 = tk.Entry(root, textvariable=number2).grid(row=2, column=2)
call_result = partial(call_result, labelResult, number1, number2)
GC_Content = partial(GC_Content, labelResult, number1)
Translation_Table= partial(Translation_Table, labelResult, number1)
Reverse_Complement= partial(Reverse_Complement, labelResult, number1)
match=partial(match, labelResult, number2,number1)
Badchars=partial(Badchars, labelResult, number2,number1)
GS_search=partial(GS_search, labelResult, number2,number1)
buttonCal = tk.Button(root, text="Reverse_Complement", command=Reverse_Complement).grid(row=6, column=2)
buttonCal1 = tk.Button(root, text="Translation_Table", command=Translation_Table).grid(row=5, column=2)
buttonCal2 =tk.Button(root, text="GC_Content", command=GC_Content).grid(row=4, column=2)
match=tk.Button(root, text="match", command=match).grid(row=7, column=2)
Badchars=tk.Button(root, text="Badchars", command=Badchars).grid(row=8, column=2)
GS_search=tk.Button(root, text="GS_search", command=GS_search).grid(row=9, column=2)


root.mainloop()