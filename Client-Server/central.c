#include<stdio.h>
#include<stdlib.h>
#include<sys/types.h>
#include<sys/ipc.h>
#include<sys/msg.h>
#include<errno.h>

#define X 1000    /*Constant for central proc mailbox name*/

int main(int argc, char* argv[]) {
	
	int stat=1,stat1=1,stat2=1,stat3=1,stat4=1;
	int msqid_central, msqid_proc1, msqid_proc2, msqid_proc3, msqid_proc4;
	if (argc != 2){
		printf("Incorrect arguments!\n");
		return 0;
	}
	
	printf("Central Process and Server Started!\n");

	/*Creating message queues for all the processes and central proc*/
	msqid_central = msgget(X,0600 | IPC_CREAT);   //Where 1000 is mailbox no. for central proc
	msqid_proc1 = msgget(X+1,0600 | IPC_CREAT);  //Where 1001 is mailbox no. for proc 1
	msqid_proc2 = msgget(X+2,0600 | IPC_CREAT);
	msqid_proc3 = msgget(X+3,0600 | IPC_CREAT);
	msqid_proc4 = msgget(X+4,0600 | IPC_CREAT);
	
	/*Error Handling if queue is not created properly*/
	if (msqid_central<0 || msqid_proc1<0 || msqid_proc2< 0 || msqid_proc3<0 || msqid_proc4<0){
		printf("Error making message queue: %s\n",strerror(errno));
		return 0;
	}


	/*struct for passing as an argument in msgsnd*/
	struct{
		long priority;
		int temp;   	/*Temperature being sent*/
		int pid;    	/*Number of the process. 0 for central*/
		int stable;     /*Set to 0 but then central make it 1 once stability is achieved*/
	} msgp,msgr;


	/*Initializing Values of msgp*/
	msgp.priority = 2;	//This is the second last param in msgrcv
	msgp.temp = atoi(argv[1]);
	msgp.pid = 0;
	msgp.stable = 0;


	int o_temp[] = {1,1,1,1};
	int i = 0,count = 0,tot_temp = 0;
	/*Message sending part*/
	while (msgp.stable != 1){
		tot_temp = 0;
		count = 0;
		/*if (stat1<0 || stat2<0 || stat3<0 || stat4<0){
			printf("Message sending failed! %s\n",strerror(errno));
			return 0;
		}*/
		printf("Central Process pid:0	temp: %i\n",msgp.temp);
		for (i=0;i<4;i++){
			stat = msgrcv(msqid_central, &msgr, sizeof(msgr) - sizeof(long), 2, 0);
			if (o_temp[msgr.pid - 1] == msgr.temp){
				count += 1;
				tot_temp += msgr.temp;
				printf("pid:%i	temp:%i\n",msgr.pid,msgr.temp);
			} else{
				tot_temp += msgr.temp;
				o_temp[msgr.pid - 1] = msgr.temp;
				printf("pid:%i	temp:%i\n",msgr.pid,msgr.temp);
			}
		}
		if (count == 4){
			msgp.stable = 1;
		} else {
			msgp.temp = (2 * msgp.temp + tot_temp) / 6;
		}
		stat1 = msgsnd(msqid_proc1, &msgp, sizeof(msgp) - sizeof(long), 0);
		stat2 = msgsnd(msqid_proc2, &msgp, sizeof(msgp) - sizeof(long), 0);
		stat3 = msgsnd(msqid_proc3, &msgp, sizeof(msgp) - sizeof(long), 0);
		stat4 = msgsnd(msqid_proc4, &msgp, sizeof(msgp) - sizeof(long), 0);
		
	}
	printf("System is Stable!	Temperature:%i\n",msgr.temp);
	printf("Deleting Message queues...\n");
	/*Delete message queues*/
	stat = msgctl(msqid_central, IPC_RMID, 0);
	printf("System exited\n");

}
