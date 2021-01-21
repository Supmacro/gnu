
all : ipcrcv ipcsnd

ipcrcv : ipcrcv.o
	gcc -o $@ $^
ipcsnd : ipcsnd.o
	gcc -o $@ $^

ipcrcv.o : ipcrcv.c
	gcc -g -c $^
ipcsnd.o : ipcsnd.c
	gcc -g -c $^

.PHONY:clean
clean:
	rm -f *.o ipcrcv ipcsnd
