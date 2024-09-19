import os
from Bio.Seq import Seq
path=r"C:\Users\Hang\AppData\Local\Packages\CanonicalGroupLimited.Ubuntu_79rhkp1fndgsc\LocalState\rootfs\home\hang\project\pro_7-8\ALL_CDS"
result_path=r"C:\Users\Hang\AppData\Local\Packages\CanonicalGroupLimited.Ubuntu_79rhkp1fndgsc\LocalState\rootfs\home\hang\project\pro_7-8\ALL_PRO_2"
#liet ke cac thu muc trong bien path
files = os.listdir(path)
#sap xep thu muc theo stt
def get_order(list):
    return int(list.split('_')[1].split('.')[0])
sorted_files = sorted(files, key=get_order)
#lam viec voi tung thu muc
for file_name in sorted_files:
    file_path = os.path.join(path, file_name)
    if os.path.isfile(file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()
        name=lines[0]
        text = ''.join(lines[1:])
        text = text.replace(" ", "").replace("\n", "")
        seq = Seq(text)
        pro = seq.translate()
#tao thu muc moi
        new_filename = f"PRO_{get_order(file_name)}.fasta"
        new_file_path = os.path.join(result_path, new_filename)
        with open(new_file_path, 'w') as new_file:
            new_file.write(f"{name}" + f"{pro}" + "\n")
    else:
        pass