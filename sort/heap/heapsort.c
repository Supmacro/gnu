
/*
 * +==============================+
 * |   Heap Sort Algorithm        |
 * +------------------------------+
 *
 * */

#include <stdio.h>
#include <stdlib.h>

#include "times3tc.h" 
#define SORTCAP 20 


void showsort(int elem[], int plen){
   
    int i;

    for(i=0; i!=plen; i++){

        if(i == plen-1){
            printf("%d.\n", elem[i]);
            break;
        }

        printf("%d, ", elem[i]);        
    }
}


void Heap(int elem[], int plen)
{
    int i;

    for(i=plen/2-1; i >= 0; i--){
        
        int lpos = 2*i+1, rpos = 2*(i+1);

        if(lpos < plen && elem[lpos] > elem[i]){
            int tmp = elem[i];
            elem[i] = elem[lpos];
            elem[lpos] = tmp;
        }

        if(rpos < plen && elem[rpos] > elem[i]){
            int tmp = elem[i];
            elem[i] = elem[rpos];
            elem[rpos] = tmp;
        }

        if(!i){
            i = (--plen)/2;

            int tmp = elem[0];
            elem[0] = elem[plen];
            elem[plen] = tmp;

            //printf("Sorting: ");
            //showsort(elem, plen);
        }

        if(plen == 1)
            break;
    }

}


int main(int argc, char *argv[])
{
    srand((unsigned)time(NULL));
    
    int elem[SORTCAP] = {0}, i=0;
    while(1){
        if(i == SORTCAP)
            break;

        elem[i] = rand()%1000;
        i++;
    }

    printf("Source Sort: ");
    showsort(elem, SORTCAP);

    struct timespec tbegin, tend;

    bzero(&tbegin, sizeof(tbegin));
    timer_start(&tbegin);

    /* Heap sort */
    Heap(elem, SORTCAP);

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

    printf("Heap Sort: ");
    showsort(elem, SORTCAP);

    printf("+-----------------------------+\n"); 
    printf("| Heap Sort                   |\n"); 
    printf("+=============================+\n"); 
    printf("| time : %4d:%03d s.          |\n", cpu_sec, cpu_msec);
    printf("+-----------------------------+\n"); 

    return 0; 
}
