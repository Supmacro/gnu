#include <stdio.h>
#include <stdlib.h>

#include <string.h>
#include <signal.h>
#include <errno.h>
#include <unistd.h>


void setup_dosignal(int signo, siginfo_t *sip, void *data)
{
    //if(sip && sip->si_value.sival_ptr){
    if(sip){
        fprintf(stdout, "%s\n", sip->si_ptr); 
    }

    fprintf(stdout, ".......\n");
    fflush(stdout);
}


int main(int argc, char *argv[])
{
    char message[64] = "test SA_RESTART ...";    
    int pipefd[2] = {0}; 

    setvbuf(stdout, NULL, _IONBF, 0);
    errno = 0;

    int ret = pipe(pipefd);
    if(ret < 0){
        printf("Fatal error: %s\n", strerror(errno));
        exit(1);
    }

    int pid = fork();
    if(pid < 0){
        printf("Fatal error: %s\n", strerror(errno));
        exit(1);
    }

    char *rp = strdup("recv SIGUSR1 signal !");

    if(pid)
    {
        char recv[64] = {0};
        struct sigaction sa;
        sa.sa_sigaction = setup_dosignal;
        sa.sa_flags = SA_SIGINFO;
    
        int ret = sigaction(SIGUSR1, &sa, NULL);
        if(ret < 0){
            printf("Fatal error: %s\n", strerror(errno));
            exit(1);
        }

        for(;;)
        {
            int size = read(pipefd[0], recv, 64);
            if(size < 0){
                printf("Fatal error: %s\n", strerror(errno));
                exit(1);
            }

            if(size > 0){
                fprintf(stdout, "%s\n", recv);
                bzero(recv, 64);
            }
        }

        exit(0);
    }

    union sigval sv;
    sv.sival_ptr = rp; 

    for(;;)
    {
        int cnt = 10;
        while(cnt > 0)
        {
            int size = write(pipefd[1], message, strlen(message));
            if(size < 0){
                printf("Fatal error: %s\n", strerror(errno));
                exit(1);
            }
            
            sleep(1);
            cnt--;
        }

        int ret = sigqueue(getppid(), SIGUSR1, sv);
        if(ret < 0){
            printf("Fatal error: %s\n", strerror(errno));
            exit(1);
        }

    }
}
