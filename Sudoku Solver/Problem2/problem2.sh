file="finalanswer.txt"
rm $file

x=$(wc -w < "p.txt")
for ((i=0;i<x;i++))
do
	python q2final.py $i
	minisat answer.txt answer2.txt
	python q2helper.py
done
