
#include <stdio.h>
#include <stdlib.h>

#include <errno.h>
#include <signal.h>
#include <fcntl.h>
#include <string.h>

#define fatal(s) { \
        printf("fatal error: %s %s:%d\n", s, __FILE__, __LINE__); \
        exit(-1);  \
}

void dosignal(int agv)
{
    if(agv == SIGINT)
        printf("\nsignal:SIGINT\n");

    unlink("fifo");
    printf("close fifo ok\n");
    exit(0);
}


int main(int argc, char *argv[])
{
    int ret = mkfifo("fifo", 0644);   
    if(ret < 0)
        fatal(strerror(errno));

    signal(SIGINT, dosignal);

    int fd = open("fifo", O_WRONLY, 0644);
    if(fd < 0){
        unlink("fifo");
        fatal(strerror(errno));
    }

    printf("Please enter your information:\n");

    while(1){
        char buf[1024] = {0};

        if(!gets(buf)){
            unlink("fifo");
            fatal(strerror(errno));
        }
        
        int sz = write(fd, buf, strlen(buf));
        if(sz != strlen(buf)){
            unlink("fifo");
            fatal(strerror(errno));
        }
    }

}


