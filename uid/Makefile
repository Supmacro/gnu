
uid : uid.o
	gcc -o $@ $^
uid.o : uid.c
	gcc -g -c $^

.PHONY:clean
clean:
	rm -f *.o uid
