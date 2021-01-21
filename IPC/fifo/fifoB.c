
#include <stdio.h>
#include <stdlib.h>

#include <signal.h>
#include <errno.h>
#include <fcntl.h>
#include <string.h>

#define fatal(s) { \
        printf("fatal error: %s %s:%d\n", s, __FILE__, __LINE__); \
        exit(-1);  \
}

int main(int argc, char *argv[])
{
    int fd = open("fifo", O_RDONLY, 0644);
    if(fd < 0)
        fatal(strerror(errno));

    while(1){
    
        char msg[1024] = {0};

        int sz = read(fd, msg, 1024);
        if(sz < 0){
            close(fd);
            fatal(strerror(errno));
        }

        if(strlen(msg)){
        
            printf("> %s\n", msg);
        }

    }
}

