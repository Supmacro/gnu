#include <stdio.h>
#include <stdlib.h>

#include <string.h>
#include <sys/msg.h>
#include <fcntl.h>

#include <errno.h>

#define fatal(s) { \
        printf("fatal error: %s %s:%d\n", s, __FILE__, __LINE__); \
        exit(-1);  \
}

struct msgque_t {

    long int msgtyp;
    char msg[1024];
};


int main(int agc, char *argv[])
{
    int msgid = msgget((key_t)996, IPC_CREAT);
    if(msgid < 0)
        fatal(strerror(errno)); 
   
    struct msgque_t msgque;

    while(1){
    
        bzero(msgque.msg, 1024);

        int ret = msgrcv(msgid, &msgque, 1024, 2, 0);
        if(ret < 0){
            msgctl(msgid, IPC_RMID, NULL);
            fatal(strerror(errno));
        }

        if(strlen(msgque.msg)){
            printf("ipc-msg: %s", msgque.msg);
        }

    } 
}
