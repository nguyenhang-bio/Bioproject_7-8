import os
import pandas as pd
from openpyxl.workbook import Workbook
my_dict = {'Querry': [], 'sequence': [],  'Description': [], 'Species': [], 'inclusion_threshold': [], 'N': [], 'exp': [], 'full_E-value': [], 'full_score': [], 'full_bias': [], 'best-1-domain_E-value': [], 'best-1-domain_score': [], 'best_1_domain_bias': [] }
path=r"C:\Users\Hang\AppData\Local\Packages\CanonicalGroupLimited.Ubuntu_79rhkp1fndgsc\LocalState\rootfs\home\hang\project\pro_7-8\phmmer_results"
files = os.listdir(path)
# get order of result files
print(files)
def get_order(list):
    return int(list.split('_')[1])
sorted_files = sorted(files, key=get_order)

def list_to_string(list):
    string=''
    for i in range(1, len(list)):
        a = list[i]
        string = string + a + ' '
    return string.strip()

for file_name in sorted_files:
    file_path = os.path.join(path, file_name)
    print(file_path)
    with open(file_path, 'r') as file:
        lines = file.readlines()
    Querry = lines[9].split('Query:')[1].split('[L')[0].strip()
    # Add querry
    count_sequence = 0
    if "No hits detected that satisfy reporting thresholds" in lines[16]:
        pass
    else:
        for index, line in enumerate(lines):
            if ">>" in line:
                count_sequence += 1
        for i in range(1, count_sequence + 1):
            my_dict['Querry'].append(Querry)
        # Add sequence
        for i in range(15, 15 + count_sequence + 1):
            if "inclusion threshold" in lines[i]:
                pass
            else:
                sequence = lines[i].split()[8]
                my_dict['sequence'].append(sequence)
                print(sequence)
                # Add N
                N = lines[i].split()[7]
                my_dict['N'].append(N)
                print('N:', N)
                # Add exp
                exp = lines[i].split()[6]
                my_dict['exp'].append(exp)
                print('exp:', exp)
                # Add E-value  score  bias of full sequence
                full_E = lines[i].split()[0]
                my_dict['full_E-value'].append(full_E)
                print('full_E-value:', full_E)

                full_score = lines[i].split()[1]
                my_dict['full_score'].append(full_score)
                print('full_score:', full_score)

                full_bias = lines[i].split()[2]
                my_dict['full_bias'].append(full_bias)
                print('full_bias:', full_bias)
                # Add E-value  score  bias of best 1 domain
                best_E = lines[i].split()[3]
                my_dict['best-1-domain_E-value'].append(best_E)
                print('best-1-domain_E-value:', best_E)

                best_score = lines[i].split()[4]
                my_dict['best-1-domain_score'].append(best_score)
                print('best-1-domain_score:', best_score)

                best_bias = lines[i].split()[5]
                my_dict['best_1_domain_bias'].append(best_bias)
                print('best_1_domain_bias:', best_bias)

        # Add inclusion_threshold
        for j in range(15, 16 + count_sequence + 1):
            if 'inclusion threshold' in lines[j]:
                if j == 15:
                    for a in range(1, count_sequence + 1):
                        my_dict['inclusion_threshold'].append('-')
                else:
                    for c in range(1, j - 15 + 1):
                        my_dict['inclusion_threshold'].append('+')
                    for d in range(1, count_sequence - j + 15 + 1):
                        my_dict['inclusion_threshold'].append('-')
            else:
                pass
        # annotation
        for index, line in enumerate(lines):
            if ">>" in line:
                annotation = lines[index]
                print(annotation)
                # add Description
                pre_Description = annotation.split('OS=')[0].split(' ')[2:]
                Description = list_to_string(pre_Description)
                print('Description:', Description)
                my_dict['Description'].append(Description)
                # add species
                Species = annotation.split('OS=')[1].strip()
                print(Species)
                my_dict['Species'].append(Species)
print(my_dict)
df = pd.DataFrame(my_dict)
print(df)
datatoexcel = pd.ExcelWriter(r"H:\Bio project\phmmer.xlsx")
df.to_excel(datatoexcel, index=False)
datatoexcel.close()


