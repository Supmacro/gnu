#include <stdlib.h>
#include <stdio.h>

#include <sys/msg.h>
#include <string.h>
#include <fcntl.h>
#include <errno.h>

#define fatal(s) { \
        printf("fatal error: %s %s:%d\n", s, __FILE__, __LINE__); \
        exit(-1);  \
}


struct msgque_t {

    long int msgtype;
    char msg[1024];
};


int main(int argc, char *argv[])
{
    int msgid = msgget((key_t)996, IPC_CREAT | IPC_EXCL);
    if(msgid < 0)
        fatal(strerror(errno));

    struct msgque_t msgque;
    msgque.msgtype = 2;

    printf("Please enter your message:\n");
    while(1){

        char *rp = fgets(msgque.msg, 1024, stdin);
        if(rp){

            int ret = msgsnd(msgid, &msgque, 1024, 0);
            if(ret < 0){
                msgctl(msgid, IPC_RMID, NULL);
                fatal(strerror(errno));
            }

            bzero(msgque.msg, 1024);    
        }
    }

}



