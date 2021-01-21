#include <stdio.h>
#include <stdlib.h>

#include <string.h>
#include <errno.h>

int main(int argc, char *argv[])
{
    int pipefd[2] = {0};

    int ret = pipe(pipefd);
    if(ret < 0){
        printf("fatal:%s\n", strerror(errno));
        exit(1);
    }

    char data[64] = "GNU IS NOT UNIX ...";
    int pid = fork();
    if(pid < 0){
        printf("fatal:%s\n", strerror(errno));
        exit(1);
    }else if(pid > 0){
        
        for(;;)
        {
            int size = write(pipefd[1], data, strlen(data));
            if(size < 0){
                printf("fatal:%s\n", strerror(errno));
                exit(1);
            }

            sleep(1);
        }
    }else{
        
        for(;;)
        {
            int size = read(pipefd[0], data, 64);
            if(size < 0){
                printf("fatal:%s\n", strerror(errno));
                exit(1);
            }
           
            fprintf(stdout, "%s [%d]\n", data, getpid());
        }
    }
    
}
