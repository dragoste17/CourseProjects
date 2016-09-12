import sys

fo = open("answer2.txt","r")
finq = open("finalanswer.txt","a")
lines=fo.read().split("\n")
if lines[0]=="UNSAT":
	finq.write("UNSAT\n")
	sys.exit()
del lines[0]
del lines[-1]
lines=lines[0].split(" ")
del lines[-1]
for i in lines:
	if i[0]!= '-':
		if int(i)%9!=0:
			finq.write(str(int(i)%9))
		else : finq.write("9")
finq.write("\n")
