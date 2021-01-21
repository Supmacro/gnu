
timer : timer.o
	gcc -o $@ $^ -lrt
timer.o : timer.c
	gcc -g -c $^

.PHONY:clean
clean :
	rm -f *.o timer
