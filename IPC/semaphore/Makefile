

ipc-sem : ipc_sem.o
	gcc -o $@ $^
ipc_sem.o : ipc_sem.c
	gcc -g -c $^

.PHONY:clean
clean:
	rm -f *.o ipc-sem
