for file in ~/project/pro_7-8/NFECIMNI_00018_homologous_sequences/*; do
    cat $file >> ~/project/pro_7-8/output.fasta
done
grep -v '^$' output.fasta > list_NFECIMNI_00017.fasta
