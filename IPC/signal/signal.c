#include <stdio.h>
#include <stdlib.h>

#include <signal.h>
#include <errno.h>
#include <string.h>

/* typedef struct {
 *      
 *      int  si_signo;   //signal number
 *      int  si_errno;   //An error value
 *      int  si_code;    //signal code
 *      int  si_trapno;
 *
 *      pid_t  si_pid;
 *      uid_t  si_uid;
 *      int  si_status;
 *      clock_t  si_utime;
 *      clock_t  si_stime;
 *
 *      ------------------
 *      sigval_t  si_value;
 *      int    si_int;
 *      void  *si_ptr;
 *      ------------------
 *
 *      int  si_overrun;
 *      int  si_timerid;
 *
 *      void  *si_addr;
 *      long   si_band;
 *
 *      int  si_fd;
 *      short  si_addr_lsb;
 *
 *      void  *si_call_addr;
 *      int  si_syscall;
 *
 *      unsigned int si_arch;
 *
 * }siginfo_t;
 *
 * */

void dosignal(int signo, siginfo_t *si, void *data)
{
    if(signo = SIGUSR1){
    
        printf("recetve signal: SIGUSR1\n");
    }
    printf("              +--------------------+\n");
    printf("              | data: %s |\n", si->si_ptr);
    printf("              |                    |\n");
    printf("              +--------------- ----+\n");

    exit(0);
}


int main(int argc, char *argv[])
{
    char *rp = strdup("hello, world");

    int pid = fork();
    if(pid < 0){
        printf("%s\n", strerror(errno));
        exit(-1);
    }
   
    /* parenet process */
    if(pid){
        
        struct sigaction sa; 
                               
        sa.sa_sigaction = dosignal;
        sa.sa_flags = SA_SIGINFO;
        //            SA_RESTART

        int ret = sigaction(SIGUSR1, &sa, NULL);
        if(ret < 0){
            printf("%s\n", strerror(errno)); 
            exit(-1);
        }

        while(1){
        
            sleep(1);
        }

    }

    if(!pid){
        
        union sigval sv;
        /*
         * typedef union sigval{
         *      int sival_int;
         *      void *sival_ptr;
         * }sigval_t;
         *
         * */

        sv.sival_ptr = rp;
        /* kill(pid_t pid, int signo);
         * raise(int signo);
         * sigqueue(pid_t pid, int signo, union sigval);
         * alarm(unsigned second); -> SIGALRM
         * settimer(int witch, const struct itimerval *value, 
         *                           struct itimerval *ovalue);
         * abort(); ->SIGABORT */
        int ret = sigqueue(getppid(), SIGUSR1, sv);
        if(ret < 0){
            printf("%s\n", strerror(errno));
            exit(-1);
        }
    }

}
