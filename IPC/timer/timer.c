#include <stdio.h>
#include <stdlib.h>

#include <sys/time.h>
#include <time.h>
#include <string.h>
#include <signal.h>

#include <errno.h>


void dosignal(int signo, siginfo_t *si, void *data)
{
    struct itimerspec *pt = si->si_value.sival_ptr;
    printf("+--------------------------+\n");
    printf("|  clock cycle: %3d:%03d s. |\n", pt->it_interval.tv_sec, 0);
    printf("+--------------------------+\n");

    //exit(0);
}


int main(int argc, char *argv[])
{
    struct sigaction sa;

    bzero(&sa, sizeof(sa));
    sa.sa_sigaction = dosignal;
    sa.sa_flags = SA_SIGINFO;

    int ret = sigaction(SIGINT, &sa, NULL);
    if(ret < 0){
        printf("error:%s\n", strerror(errno));
        return 1;
    }

    struct itimerspec timer;
    timer_t tmid;

    timer.it_interval.tv_sec = 10;
    timer.it_interval.tv_nsec = 0;

    timer.it_value.tv_sec = 10;
    timer.it_value.tv_nsec = 0;

    struct sigevent sigev;

    bzero(&sigev, sizeof(sigev));
    sigev.sigev_notify = SIGEV_SIGNAL;
    sigev.sigev_signo = SIGINT;
    sigev.sigev_value.sival_ptr = &timer;

    /*
     * CLOCK_REALTIME              // Systeim realtime clock.
     * CLOCK_MONOTONIC             // Represents monotonic time. Cannot be set
     * CLOCK_PROCESS_CPUTIME_ID    // High resolution per-process timer.
     * CLOCK_THREAD_CPUTIME_ID     // Thread-specific timer.
     * CLOCK_REALTIME_HR           // High resolution version of CLOCK_REALTIME.
     * CLOCK_MONOTONIC_HR          // High resolution version of CLOCK_MONOTONIC.
     *
     * */

    ret = timer_create(CLOCK_REALTIME, &sigev, &tmid);
    if(ret < 0){
        printf("error:%s\n", strerror(errno));
        return 1;
    }

    ret = timer_settime(tmid, 0, &timer, NULL);
    if(ret < 0){
        printf("error:%s\n", strerror(errno));
        return 1;
    }

    while(1){
    
        printf("clock ...\n");
        sleep(1);

        //ret = timer_settime(tmid, 0, &timer, NULL);
        //if(ret < 0){
        //    printf("error:%s\n", strerror(errno));
        //    return 1;
        //}

    }

}

