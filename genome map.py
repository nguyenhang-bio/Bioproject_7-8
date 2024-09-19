import pandas as pd
from Bio import SeqIO
import matplotlib.pyplot as plt

#calculate genome_length:
path=r"H:\Bio project\LR813619.1.fasta"
record = SeqIO.read(path, "fasta")
sequence = str(record.seq)
print('len:',len(sequence))

# Process PVN02.tbl data
path=r"H:\Bio project\PVN02.tbl"
with open(path, 'r') as file:
    lines = file.readlines()

#create array
count=0
array={'Locus_tag': [], 'Start': [], 'End': [], 'Length': [] }
for index,line in enumerate(lines):
    if 'CDS' in line:
        count += 1
        array['Locus_tag'].append("CDS_" + f"{count}")
        start=lines[index].split()[1]
        array['Start'].append(int(start))
        end=lines[index].split()[0]
        array['End'].append(int(end))
        length=int(end)-int(start)
        array['Length'].append(length)
print(array)

#create map
plt.figure(figsize=(12, 2))  # Adjust figure size as needed

plt.axhline(y=0, color='black', linewidth=0.5)
for i in range(len(array['Locus_tag'])):
    # Draw length of CDS
    plt.hlines(y=0, xmin=array['Start'][i], xmax=array['End'][i], linewidth=2, color='blue')

    # Draw vertical lines limiting the length of CDS
    plt.vlines(x=[array['Start'][i], array['End'][i]], ymin=-0.01, ymax=0.01, linewidth=1, colors='black')

    # Names of CDS
    plt.text((int(array['Start'][i]) + int(array['End'][i])) / 2, -0.05, array['Locus_tag'][i], va='center', ha='center', fontsize=8, color='black', alpha=0.8, fontweight='bold')  # Adjust alpha as needed

# Tạo một danh sách chứa tất cả các vị trí cần hiển thị
xtick_positions = []
for j in range(len(array['Locus_tag'])):
    xtick_positions.append(array['Start'][j])
    xtick_positions.append(array['End'][j])

# Thiết lập các nhãn trên trục x
plt.xticks(xtick_positions)
plt.xlabel('Physical genome map')

# Undisplay y-axis and set limit for y-axis
plt.yticks([])
plt.ylim(-0.08, 1)
plt.gca().spines['left'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)

#display map
plt.show()



