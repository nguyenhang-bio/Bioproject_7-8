count=0
while read line
do
 if [[ $line = *">"* ]]; then
  ((count++))
  echo $line >> ~/project/pro_7-8/ALL_CDS/CDS_$count.fasta
 else
  echo $line >> ~/project/pro_7-8/ALL_CDS/CDS_$count.fasta
 fi
done < ~/project/pro_7-8/annotation/PVN02.ffn
