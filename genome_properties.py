from Bio import SeqIO
import numpy as np
import matplotlib.pyplot as plt
path=r"H:\Bio project\LR813619.1.fasta"
record = SeqIO.read(path, "fasta")
sequence = str(record.seq)
print('len:',len(sequence))

def gc_content(seq):
    G = seq.count('G')
    C = seq.count('C')
    total = len(seq)
    return ((G + C) / total * 100)
print('GC content:',gc_content(sequence))

#create G-C content plot with window_size=100bp
array = {}
for i in range(0, len(sequence) - 100 + 1):
    window = sequence[i:i + 100]
    array[i]=gc_content(window)

position = list(array.keys())
GC_content = list(array.values())
plt.axhline(y=50, color='blue', linestyle='-', linewidth=2, zorder=10)
plt.plot(position, GC_content)
plt.xlabel('Position(bp)')
plt.ylabel('GC content (%)')
plt.show()

#create G-C skew plot
def gc_skew(seq):
    G = seq.count('G')
    C = seq.count('C')
    total = len(seq)
    return ((G - C) / (G + C))

array_2 = {}
for j in range(0, len(sequence) - 100 + 1):
    window = sequence[j:j + 100]
    array_2[j]=gc_skew(window)

position_2 = list(array_2.keys())
GC_skew = list(array_2.values())
plt.axhline(y=0, color='blue', linestyle='-', linewidth=2,zorder=10)
plt.plot(position_2, GC_skew)
plt.xlabel('Position(bp)')
plt.ylabel('GC skew')
plt.show()


