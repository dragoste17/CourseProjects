#include<stdio.h>
#include<stdlib.h>
#include<sys/types.h>
#include<sys/ipc.h>
#include<sys/msg.h>
#include<errno.h>

#define X 1000

int main(int argc, char* argv[]){
	
	int stat=1,stat1=1,stat2=1,stat3=1,stat4=1;
	int msqid_proc1 = -1, msqid_proc2 = -1, msqid_proc3 = -1, msqid_proc4 = -1;
	if (argc != 3){
		printf("Incorrect arguments\n");  //For error in I/P
		return 0;
	}

	int msqid_central = -1;
	msqid_central = msgget(X,0600 | IPC_CREAT);
	//printf("%i\n",msqid_central);


	/*For the creation of unique qids of message queues*/
	if (atoi(argv[2]) == 1){
		msqid_proc1 = msgget(X+1,0600 | IPC_CREAT);
		//printf("%i\n",msqid_proc1);
	}
	else if (atoi(argv[2]) == 2){
		msqid_proc2 = msgget(X+2,0600 | IPC_CREAT);
		//printf("%i\n",msqid_proc2);
	}
	else if (atoi(argv[2]) == 3){
		msqid_proc3 = msgget(X+3,0600 | IPC_CREAT);
		//printf("%i\n",msqid_proc3);
	}
	else if (atoi(argv[2]) == 4){
		msqid_proc4 = msgget(X+4,0600 | IPC_CREAT);
		//printf("%i\n",msqid_proc4);
	}
	else {
		printf("Error!\n");
		return 0;
	}


	/*Error Handling if queue is not created*/
	if (msqid_proc1<0 && msqid_proc2<0 && msqid_proc3<0 && msqid_proc4<0 && msqid_central<0){
		printf("Error making message queues: %s\n",strerror(errno));
		return 0;
	}



	/*Similar struct as that of central to copy data into*/
	struct{
                long priority;
                int temp;
                int pid;
                int stable;
        } msgp,msgr;	


	/*Initializing Values of msgr*/
	msgr.priority = 2;
	msgr.temp = atoi(argv[1]);
	msgr.pid = atoi(argv[2]);
	msgr.stable = 0;

	msgp.stable = 0;


	int stab_temp1,stab_temp2,stab_temp3,stab_temp4;
	/*Receiving and Sending Messages sent by central*/
	while(msgp.stable != 1){
		
		stat = msgsnd(msqid_central, &msgr, sizeof(msgr) - sizeof(long), 0);
		
		if (atoi(argv[2]) == 1){
			stat1 = msgrcv(msqid_proc1, &msgp, sizeof(msgp) - sizeof(long), 2, 0);
			/*Calc of temperature for proc1*/
			msgr.temp = (msgr.temp * 3 + 2 * msgp.temp) / 5;
			stab_temp1 = msgr.temp;
		}
		else if (atoi(argv[2]) == 2){
			stat2 = msgrcv(msqid_proc2, &msgp, sizeof(msgp) - sizeof(long), 2, 0);
			/*Calc of temperature for proc1*/
			msgr.temp = (msgr.temp * 3 + 2 * msgp.temp) / 5;
			stab_temp2 = msgr.temp;
		}
		else if (atoi(argv[2]) == 3){
			stat3 = msgrcv(msqid_proc3, &msgp, sizeof(msgp) - sizeof(long), 2, 0);
			/*Calc of temperature for proc1*/
			msgr.temp = (msgr.temp * 3 + 2 * msgp.temp) / 5;
			stab_temp3 = msgr.temp;
		}
		else if (atoi(argv[2]) == 4){
			stat4 = msgrcv(msqid_proc4, &msgp, sizeof(msgp) - sizeof(long), 2, 0);
			/*Calc of temperature for proc1*/
			msgr.temp = (msgr.temp * 3 + 2 * msgp.temp) / 5;
			stab_temp4 = msgr.temp;
		}
	

		/*if (stat1<0 || stat2<0 || stat3<0 || stat4<0 || stat<0){
			printf("Error passing Messages!\n");
			return 0;
		}*/
	}
	if (atoi(argv[2]) == 1)
		stat = msgctl(msqid_proc1, IPC_RMID, 0);
	else if (atoi(argv[2]) == 2)
        	stat = msgctl(msqid_proc2, IPC_RMID, 0);
	else if (atoi(argv[2]) == 3)
        	stat = msgctl(msqid_proc3, IPC_RMID, 0);
	else if (atoi(argv[2]) == 4)
        	stat = msgctl(msqid_proc4, IPC_RMID, 0);

}
