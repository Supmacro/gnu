#include <stdio.h>
#include <stdlib.h>

#include <aio.h>
#include <fcntl.h>
#include <signal.h>
#include <string.h>

#include <time.h>
#include <errno.h>

void dosig(int signo, siginfo_t *si, void *data)
{
    struct aiocb *paio = (struct aiocb *)si->si_value.sival_ptr;
    while(aio_error(paio) == EINPROGRESS){};

    fprintf(stdout, "AIO read size: %u byte\n", aio_return(paio));
    exit(0);
}


int main(int argc, char *agv[])
{
    struct sigaction sa;

    sa.sa_flags = SA_SIGINFO;
    sa.sa_sigaction = dosig;

    int ret = sigaction(SIGIO, &sa, NULL);
    if(ret < 0){
        printf("%s\n", strerror(errno));
        exit(-1);
    }

    struct aiocb aio;
    char faio[64] = "./test.txt";

    bzero(&aio, sizeof(aio));
    aio.aio_fildes = open(faio, O_RDONLY);
    if(!aio.aio_fildes){
        printf("%s\n", strerror(errno));
        exit(-1);
    }

    struct stat sta;

    bzero(&sta, sizeof(sta));
    if(stat(faio, &sta)){
        printf("%s\n", strerror(errno));
        exit(-1);
    }

    aio.aio_buf = calloc(1, sta.st_size+1);
    if(!aio.aio_buf){
        printf("%s\n", strerror(errno));
        exit(-1);
    }

    aio.aio_nbytes = sta.st_size;
    //aio.aio_lio_opcode = LIO_READ; //LIO_WRITE
    
    /*
     * int lio_listio(int mode, struct aiocb *list[], int nent, struct sigevent *sig);
     *
     * mode: LIO_WAIT
     *       LIO_NOWAIT
     * */

    struct sigevent sigev;
    bzero(&sigev, sizeof(sigev));

    /*
     * struct sigevent{
     *      int  sigev_notify;
     *      int  sigev_signo;
     *      union sigval sigev_value;
     *      void(*sigev_notify_function)(union sigval);
     *      pthread_t  *sigev_notify_attributes;
     * }
     *
     * */

    sigev.sigev_notify = SIGEV_SIGNAL;
    sigev.sigev_signo = SIGIO;
    sigev.sigev_value.sival_ptr = (void*)&aio;
    aio.aio_sigevent = sigev;

    ret = aio_read(&aio);
    if(ret < 0){
        printf("%s\n", strerror(errno));
        exit(-1);
    }

    while(1){
        printf("waiting SIGIO signal ... \n");
        sleep(1);
    }

}


