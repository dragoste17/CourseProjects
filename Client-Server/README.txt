Shinde Lav Chandrakant
2013CSB1032

=======================================================================================================================================================
CONTENTS:
1) What the program does
2) How to build and execute
3) Sample Test Cases
4) Design Decisions

=======================================================================================================================================================
1) What the program does:
	This program implements the system calls in POSIX for inter-process communication. It passes a series of inter-dependent calculations among one central and four external processes for the computation of the temperature of the process. The system is declared to be stable when the previous states of temperatures and the new set of temperatures of each of the processes become the same. It then exits the processes only after clearing the message queues or mailboxes created by each of the processes.

=======================================================================================================================================================
2) How to build and execute:
	Unzip the given file and change the directory in the terminal to inside the unzipped folder.
	
	Compile by: gcc external.c -o external
		    gcc central.c -o central

	Execute as: ./external 100 1 & ./external 22 2 & ./external 50 3 & ./external 40 4 & ./central 60

		    where the first parameter is the temperature and the second is the process id designated by us.

	Output is: List of all the stages of the temperatures of all the processes followed by a System is stable and the final stable temperature 			   once it occurs

=======================================================================================================================================================
3) Sample Test Cases:
	
	i) ./external 10 1 & ./external 20 2 & ./external 30 3 & ./external 40 4 & ./central 50      Output Stable Temperature: 25
	ii) ./external 105 1 & ./external 245 2 & ./external 150 3 & ./external 90 4 & ./central 30    Output Stable Temperature: 122
	iii) ./external 2 1 & ./external 24 2 & ./external 125 3 & ./external 900 4 & ./central 1000    Output Stable Temperature: 378

=======================================================================================================================================================
4) Design Decisions:
	A struct was used so as to conviniently oraganise and manage the data passed by the various processes by using the inter-process communication system calls. Error handling was done for cases of inappropriate arguments so that the code does not run with wrong values but escapes from the code and shows what was invalid. The decision that the operations will be synchronous was preferred over keepin it asynchronous so that the sender will block if the message queue is full.
