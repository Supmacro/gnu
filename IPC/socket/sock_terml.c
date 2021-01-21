
/*
 *  sock_terml.c
 *
 * */

#include <sys/socket.h>
#include <sys/epoll.h>
#include <arpa/inet.h>

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "sock_def.h"

#define login() login_tty()

int main(int argc, char *argv[])
{

    struct sockaddr_in sockaddr;

    sockaddr.sin_addr.s_addr = inet_addr("192.168.2.40");
    sockaddr.sin_port = htons(5230);
    sockaddr.sin_family = AF_INET;

    int csock = socket(AF_INET, SOCK_STREAM, 0);
    if(csock < 0){
        fatal("socket()");
    }

    setvbuf(stdout, NULL, _IONBF, 0);
    int ret = connect(csock, 
                    (struct sockaddr *)&sockaddr, 
                    sizeof(sockaddr));
    if(ret < 0){
        fatal("Can't to server");
    }

    login();
    char ptocol[] = "/tty/";
    write(csock, ptocol, sizeof(ptocol));

    for(;;){
    
        char msg[MSG_BUFF_SIZE] = {0};

        int rc = read(csock, msg, MSG_BUFF_SIZE);
        if(rc > 0){
            
            fprintf(stdout, "%s", msg);
        }

    }

    close(csock);

    return 0;
}
