#include <stdio.h>
#include <stdlib.h>

#include <string.h>
#include <sys/sem.h>
#include <sys/shm.h>
#include <sys/types.h>
#include <fcntl.h>


#define fatal(s) { \
        printf("fatal error: %s %s:%d\n", s, __FILE__, __LINE__); \
        exit(-1);  \
}

#include <errno.h>

union semnu {
    struct semid_ds *buf;
    unsigned short *array;

    int val;
};

/* P */
int sem_op(int semid)
{
    struct sembuf op = {.sem_num = 0, 
                        .sem_op = -1, 
                        .sem_flg = SEM_UNDO};

    return semop(semid, &op, 1);
}

/* V */
int sem_ov(int semid)
{
    struct sembuf ov = {.sem_num = 0, 
                        .sem_op = 1, 
                        .sem_flg = SEM_UNDO};

    return semop(semid, &ov, 1);
}


int main(int argc, char *argv[])
{
    int semid = semget((key_t)996, 1, IPC_CREAT | IPC_EXCL);
    if(semid < 0)
        fatal(strerror(errno));

    union semnu mysem;

    mysem.val = 1;
    /* 
     * IPC_STAT |  memcpy(mysem.buf, kernel.semid_ds);
     * IPC_SET  |  memcpy(kernel.semid_ds.ipc_perm, mysem.buf.ipc_perm);
     * IPC_RMID |  remove semaphore, and wake up all process.
     * GETALL   |  
     * GETNCNT  |  Returns the number of processes waiting for resources.
     * GETPID   |  Returns the ID of the last process that executed 'semop'
     * GETVAL   |  Returns the value of a single semaphore.
     * SETVAL   |  Set the value of a single semaphore.
     * SETALL   |
     */
    int ret = semctl(semid, 0, SETVAL, mysem);
    if(ret < 0){
        semctl(semid, 0, IPC_RMID, mysem);
        fatal(strerror(errno));
    }

    /* share memory */
    int shmid = shmget((key_t)666, 64, IPC_CREAT | IPC_EXCL);
    if(shmid < 0){
    
        semctl(semid, 0, IPC_RMID, mysem);
        fatal(strerror(errno));
    }

    void *rp = shmat(shmid, NULL, 0);
    if(!rp){
            
        shmctl(shmid, IPC_RMID, NULL);
        semctl(semid, 0, IPC_RMID, mysem);
        fatal(strerror(errno));
    }

    bzero(rp, 64);

    ret = fork();
    if(ret < 0){

        shmdt(rp);
        shmctl(shmid, IPC_RMID, NULL);
        
        semctl(semid, 0, IPC_RMID, mysem);
        fatal(strerror(errno));
    }

    if(ret){

        for(; *((int*)rp) < 10;){
            if(*((int*)rp)%2){
                printf("Child+ Process: %d\n", *((int*)rp));
            }    

            sleep(1);
            sem_op(semid);

            *((int*)rp) = *((int*)rp) + 1;
            sem_ov(semid);
        }
    }

    if(!ret){

        for(; *((int*)rp) < 10;){
            if(*((int*)rp)%2 == 0){
                printf("Parent Process: %d\n", *((int*)rp));
            }      

            sleep(1);
            sem_op(semid);

            *((int*)rp) = *((int*)rp) + 1;
            sem_ov(semid);
        }
    }
   
    shmdt(rp);
    shmctl(shmid, IPC_RMID, NULL);

    semctl(semid, 0, IPC_RMID, mysem);

    return 0;
}



