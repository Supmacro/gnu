
/*
 * sock_client.c
 *
 * */

#include <sys/socket.h>
#include <sys/epoll.h>
#include <arpa/inet.h>

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "sock_def.h"
#include "sock_user.h"


#define login(host,port) \
        login_clt(host,port)


/* registeration epoll event */
void reg_epoll_event(int epof, int fd);


int main(int argc, char *argv[])
{
    struct sockaddr_in sockaddr;

    sockaddr.sin_addr.s_addr = inet_addr("192.168.2.40");
    sockaddr.sin_family = AF_INET;
    sockaddr.sin_port = htons(5230);

    int csock = socket(AF_INET, SOCK_STREAM, 0);
    if(csock < 0){
        fatal("socket()"); 
    }

    setvbuf(stdout, NULL, _IONBF, 0);
    int ret = connect(csock, 
                    (struct sockaddr *)&sockaddr, 
                    sizeof(sockaddr));
    if(ret < 0){
        fatal("Can't connect to server");
    }

    login(inet_ntoa(sockaddr.sin_addr), 
                    ntohs(sockaddr.sin_port));

    char user[USER_NAME_SIZE+2] = {0};

    char *pu = active_user(user);
    if(pu == NULL){
        fatal("active_user()"); 
    }

    char ptol[2*USER_NAME_SIZE] = "@";

    strcat(user, ":");
    strcat(ptol, user);

    int epof = epoll_create(UNIX_EPOLL_SIZE);
    if(epof < 0){
        fatal("epoll_create()");
    }

    reg_epoll_event(epof, fileno(stdin)); 

    for(;;)
    {
        struct epoll_event kern_evs[UNIX_EPOLL_SIZE] = {0};
        int evc = epoll_wait(epof, 
                        kern_evs, 
                        UNIX_EPOLL_SIZE, 
                        20000);
        if(evc < 0){
            fatal("epoll_wait()");
        }

        int i;
        for(i=0; i != evc; i++){
        
            char msg[MSG_BUFF_SIZE] = {0};
        
            if(kern_evs[i].events == EPOLLIN){

                /* read */
                int rc = read(kern_evs[i].data.fd, 
                                msg, 
                                MSG_BUFF_SIZE);

                if(rc > 0){
               
                    char msg_send[MSG_BUFF_SIZE] = {0};

                    strcpy(msg_send, ptol);
                    strcat(msg_send, msg);
                    write(csock, 
                          msg_send, 
                          MSG_BUFF_SIZE);
                        
                }

                kern_evs[i].events = EPOLLIN ;
                epoll_ctl(epof, 
                          EPOLL_CTL_MOD, 
                          kern_evs[i].data.fd, 
                          &kern_evs[i]);

            }

        }

    }

}

void reg_epoll_event(int epof, int fd)
{
    struct epoll_event eve;

    eve.events = EPOLLIN ;
    eve.data.fd = fd;

    int ret = epoll_ctl(epof, EPOLL_CTL_ADD, fd, &eve);
    if(ret < 0){
        fatal("Call to function epoll_ctl() failed"); 
    }
}
