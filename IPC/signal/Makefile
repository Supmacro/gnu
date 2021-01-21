all : signal

signal : sig-restart.o
	gcc -o $@ $<

%.o : %.c
	gcc -g -c $<

.PHONY:clean
clean:
	rm -f *.o signal
