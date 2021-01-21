
all : fifoA fifoB

fifoA : fifoA.o
	gcc -o $@ $^
fifoB : fifoB.o
	gcc -o $@ $^
fifoA.o : fifoA.c
	gcc -g -c $^
fifoB.o : fifoB.c
	gcc -g -c $^

.PHONY:clean
clean:
	rm -f fifoA fifoB *.o
