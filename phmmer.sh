for file in ~/project/pro_7-8/ALL_PRO_2/*
do
	phmmer $file /home/hang/databases/swissprot2/uniprot_sprot.fasta > ~/project/pro_7-8/phmmer_results/$(basename "$file" | sed 's/\.fasta$//')_phmmer.txt
	if [[ $? -ne 0 ]]; then
        	echo "Error running phmmer for file: $file"
    	fi
done
