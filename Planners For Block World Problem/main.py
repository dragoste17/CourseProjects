import astar
import bfs
import gsp
import sys

if len(sys.argv) != 2:
	print "Invalid Arguments"
	sys.exit()

else:
	linesArray = open(sys.argv[1],"r").read().splitlines()
	if linesArray[1] == "f":
		bfs.gsp(sys.argv[1])
	elif linesArray[1] == "a":
		astar.gsp(sys.argv[1])
	elif linesArray[1] == "g":
		gsp.gsp(sys.argv[1])
	else:
		print "Invalid Planner"
		sys.exit()
