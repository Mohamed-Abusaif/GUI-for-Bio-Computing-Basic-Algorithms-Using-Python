def dist(Seq1, Seq2, resultLabel):
    seq1 = Seq1.get()
    seq2 = Seq2.get()
    tag = 10
    dic = {}
    for i in range(0, len(seq1)-tag):
        dic[seq1[i:i+tag]] = dic.get(seq1[i:i+tag], 0)+1

    dic2 = {}
    for i in range(0, len(seq2)-tag):
        dic2[seq2[i:i+tag]] = dic2.get(seq2[i:i+tag], 0)+1

    k = list(dic.keys())
    for i in range(len(k)):
        dic2[k[i]] = (dic2.get(k[i], 0)-dic[k[i]])
    d = list(dic2.values())

    Sum = 0
    for i in range(len(d)):
        Sum += d[i]**2
    distance = float(Sum)**(0.5)
    resultLabel.configure(
        text="Distance between two dna sequences ="+str(distance))
    return
