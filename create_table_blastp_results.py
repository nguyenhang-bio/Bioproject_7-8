import os
import pandas as pd
from openpyxl.workbook import Workbook
my_dict = {'Locus_tag': [], 'Proteins': [], 'Species': [] }
path=r"C:\Users\Hang\AppData\Local\Packages\CanonicalGroupLimited.Ubuntu_79rhkp1fndgsc\LocalState\rootfs\home\hang\project\pro_7-8\blastp_results"
result_path=r"C:\Users\Hang\AppData\Local\Packages\CanonicalGroupLimited.Ubuntu_79rhkp1fndgsc\LocalState\rootfs\home\hang\project\pro_7-8\ALL_PRO_2"
files = os.listdir(path)
def get_order(list):
    return int(list.split('_')[1].split('.')[0])
sorted_files = sorted(files, key=get_order)

def list_to_string(list,stt):
    string = ''
    for i in range(stt,stt+6):
        a = list[i].strip('\n')
        string = string + a
    return string

for file_name in sorted_files:
        file_path = os.path.join(path, file_name)
        with open(file_path, 'r') as file:
                lines = file.readlines()
        print(file_name)
        if len(lines[28].strip()) == 0:
                Locus_tag = (lines[23].split(' ')[1].strip('\n'))
                count = 0
                for char in lines:
                        if ">" in char:
                                count += 1
                for i in range(1, count + 1):
                        my_dict['Locus_tag'].append(Locus_tag)
                for index, line in enumerate(lines):
                        if ">" in line:
                                a = list_to_string(lines, index)
                                annotation = (a.split('>')[1].split('Length')[0])
                                Proteins = annotation.split('[')[0]
                                Species = annotation.split('[')[1].strip(']')
                                my_dict['Proteins'].append(Proteins)
                                my_dict['Species'].append(Species)
        else:
#Locus_tag
                Locus_tag = (lines[23].split(' ')[1].strip('\n'))
                my_dict['Locus_tag'].append(Locus_tag)
#Protein và Species
                my_dict['Proteins'].append([])
                my_dict['Species'].append([])

print(len(my_dict['Locus_tag']))
print(len(my_dict['Species']))
print(len(my_dict['Proteins']))

df = pd.DataFrame(my_dict)
datatoexcel = pd.ExcelWriter(r"H:\Bio project\blastp_results.xlsx")
df.to_excel(datatoexcel, index=False)
datatoexcel.close()





