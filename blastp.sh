for file in ~/project/pro_7-8/ALL_PRO_2/*
do
    # Tạo tên tệp đầu ra dựa trên tên tệp đầu vào
    output_file="~/project/pro_7-8/blastp_results/$(basename "$file" | sed 's/\.fasta$//')_blastp.txt"

    blastp -query $file -db ~//databases/swissprot/swissprot -evalue 0.001 -out ~/project/pro_7-8/blastp_results/$(basename $file | sed 's/\.fasta$//')_blastp.txt

    # Kiểm tra lỗi
    if [[ $? -ne 0 ]]; then
        echo "Error running BLAST for file: $file"
    fi
done
