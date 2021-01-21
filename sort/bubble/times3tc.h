#include <sys/time.h>
#include <time.h>

#include <string.h>

#define NS2MS(nsec) ((time_t)((nsec)/1000000))

void timer_start(struct timespec *t){
    clock_gettime(CLOCK_PROCESS_CPUTIME_ID, t);
}

void timer_end(struct timespec *t){
    clock_gettime(CLOCK_PROCESS_CPUTIME_ID, t);
}


