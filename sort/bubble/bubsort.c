
/*
 *  +======================+
 *  |     Bubble Sort      |
 *  +======================+
 *
 * */

#include <stdio.h>
#include <stdlib.h>

#include "times3tc.h"

#define scap 20 

int main(int argc, char *argv[])
{
    /* ini random num seed */
    srand((unsigned)time(NULL));

    int elem[scap] = {0}, i = 0;

    while(1){
        
        if(i == scap)
            break;

        elem[i++] = rand()%1000;
    }

    int j = 0;

    struct timespec tbegin, tend;
    bzero(&tbegin, sizeof(tbegin)); 

    timer_start(&tbegin);

    /* Bubble Sort Algorithm */
    for(i = 0; i != scap; i++){
        for(j = 0; j != scap-i-1; j++){

            if(elem[j] <= elem[j+1])
                continue;

            int swap = elem[j];
    
            elem[j] = elem[j+1];
            elem[j+1] = swap;

        }
    }

    bzero(&tend, sizeof(tend));
    timer_end(&tend);

    time_t cpu_sec = 0, cpu_msec = 0;

    if(tend.tv_nsec < tbegin.tv_nsec){
        long nsec = tend.tv_nsec - tbegin.tv_nsec + 1000000000;
        
        tend.tv_sec--;
        cpu_msec = NS2MS(nsec);
        cpu_sec = tend.tv_sec - tbegin.tv_sec;
        
    }else{
       
        long nsec = tend.tv_nsec - tbegin.tv_nsec;
        cpu_msec = NS2MS(nsec);
        cpu_sec = tend.tv_sec - tbegin.tv_sec;
    }

    
    printf("Bubble Sort:");
    for(i = 0; i!=scap; i++){

        if(i == scap - 1){
            printf("%d.\n", elem[i]);
            break;
        }

        printf("%d, ", elem[i]);
    }
   

    printf("+-----------------------------+\n"); 
    printf("| Bubble Sort                 |\n"); 
    printf("+=============================+\n"); 
    printf("| time : %4d:%03d s.          |\n", cpu_sec, cpu_msec);
    printf("+-----------------------------+\n"); 
    
    return 0;
}


