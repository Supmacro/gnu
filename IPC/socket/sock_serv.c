
/*
 *  sock_serv.c
 *
 * */

#include <sys/epoll.h>
#include <sys/shm.h>
#include <sys/ipc.h>
#include <sys/socket.h>

#include <arpa/inet.h>

#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <unistd.h>

#include "sock_def.h"

#define login(host,port) \
        login_svr(host,port)


/* registeration epoll event */
void reg_epoll_event(int epof, int fd);

/* return share memory addr */
void *rt_shm_addr(int ipc, int *sid, int flag);

/* main */
int main(int argc, char *argv[]){

    struct sockaddr_in sockaddr; 
   
    /* keep a clean data space */
    memset(&sockaddr, 0x0, sizeof(struct sockaddr_in));
    /*
     * AF_INET (TCP/IP-IPV4)
     * AF_INET6(TCP/IP-IPV6)
     * AF_UNIX (LOCAL)
     * */
    sockaddr.sin_family = AF_INET;
    sockaddr.sin_port = htons(5230);
    sockaddr.sin_addr.s_addr = htonl(INADDR_ANY); 

    setvbuf(stdout, NULL, _IONBF, 0);
    /*
     * SOCK_STREAM (TCP stream)
     * SOCK_DGRAM  (UDP stream)
     * SOCK_RAW    (SORCE)
     * */
    int nsock = socket(AF_INET, SOCK_STREAM, 0);                                  
    if(nsock < 0){
        fatal("socket()");
    }

    /* non-blocking socket */
    //setnonblocking(nsock);
    int ret = bind(nsock, 
                   (struct sockaddr*)&sockaddr, 
                   sizeof(sockaddr));
    if(ret < 0){
        fatal("bind()");
    }
  
    printf("Waiting for client connection request ...\n"); 
    listen(nsock, UNIX_BOCKLOG);

    int key;
    void *maddr = rt_shm_addr(1, &key, 
                            IPC_CREAT | IPC_EXCL);
    *((int*)maddr) = -1;

    for(;;)
    {
        struct sockaddr_in client;
        socklen_t  socklen = sizeof(client);

        int conn = accept(nsock, 
                 (struct sockaddr*)&client, 
                 &socklen);
        if(conn < 0){
            fatal("accept()");
        }
    
        pid_t pid = fork(); 
        if(!pid){
            
            struct sockaddr_in *clt = (struct sockaddr_in *)&client;
            /*
             * print head info
             * */
            login(inet_ntoa(clt->sin_addr), 
                            ntohs(clt->sin_port));

            /* epoll_create() */
            int epof = epoll_create(UNIX_EPOLL_SIZE); 
            
            reg_epoll_event(epof, conn);

            int  skey;
            int *saddr = (int*)rt_shm_addr(1, &skey, IPC_CREAT);
            if(saddr == NULL){
                fatal("rt_shm_addr()");
            }

            while(1){
       
                struct epoll_event kern_evs[UNIX_EPOLL_SIZE] = {0};

                /* epoll_wait() */
                int evc = epoll_wait(epof, 
                                    kern_evs, 
                                    UNIX_EPOLL_SIZE, 
                                    200);

                int i;
                for(i=0; i!=evc; i++){
        
                    char msg[MSG_BUFF_SIZE] = {0};

                    if(kern_evs[i].events == EPOLLIN){
                        int rc = read(kern_evs[i].data.fd, 
                                      msg, 
                                      MSG_BUFF_SIZE);
                
                        if(rc > 0){
                  
                            /* protocol */
                            if(strstr(msg, "/tty/")){

                                if(*saddr != -1){
                                    fatal("message terminal already exists");    
                                }

                                *saddr = kern_evs[i].data.fd;
                                goto next;
                                
                            }

                            if(*saddr == -1){
                                fatal("terminal is not connected");
                            }

                            if(msg[0] == '@'){
                                write(*saddr, msg+1, MSG_BUFF_SIZE);
                            }

                        }

next:

                        kern_evs[i].events = EPOLLIN ;
                        epoll_ctl(epof, 
                                  EPOLL_CTL_MOD, 
                                  kern_evs[i].data.fd, 
                                  &kern_evs[i]);

                    }else if(kern_evs[i].events == EPOLLOUT){
               
                        int rc = write(kern_evs[i].data.fd, 
                                       msg, 
                                       MSG_BUFF_SIZE);

                        kern_evs[i].events = EPOLLIN ;
                        epoll_ctl(epof, 
                                  EPOLL_CTL_MOD, 
                                  kern_evs[i].data.fd, 
                                  &kern_evs[i]);
                    }
            
                }
            }

            // shmdt()
            ret = shmdt((void*)saddr);
            if(ret < 0){
                fatal("shmdt()");
            }
            
            close(epof);
            close(conn);

        }

    }

    ret = shmctl(key, IPC_RMID, NULL);
    if(ret < 0){
        fatal("shmctl");
    }

    close(nsock);
    
}


void reg_epoll_event(int epof, int fd){

    struct epoll_event eve;

    memset(&eve, 0x0, sizeof(eve));
    eve.data.fd = fd;
    
    /*
     * EPOLLIN       * file descriptor can be read 
     * EPOLLOUT      * file descriptor can be write
     * EPOLLPRI      * the file descriptor has urgent data readable
     * EPOLLERR      * file descriptor error
     * EPOLLHUP      * file descriptor is hung up
     * EPOLLET       * edge triggered mod
     * EPOLLONESHOT  * only listen to events once
     * */
    eve.events = EPOLLIN ;

    /*
     * EPOLL_CTL_ADD  
     * EPOLL_CTL_MOD
     * EPOLL_CTL_DEL
     * */
    epoll_ctl(epof, EPOLL_CTL_ADD, fd, &eve);   

}


void *rt_shm_addr(int ipc, int *sid, int flag){

    *sid = shmget((key_t)ipc, 
                      UNIX_KERN_PAGE, 
                      flag);
    if(*sid < 0){
        fatal("shmget()");
    }    

    return shmat(*sid, NULL, 0);
}



