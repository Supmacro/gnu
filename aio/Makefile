aio : aio.o
	gcc -o $@ $^ -lrt
aio.o : aio.c
	gcc -g -c $^

.PHONY:clean
clean:
	rm -f *.o aio
