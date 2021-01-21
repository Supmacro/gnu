
heapsort : heapsort.o
	gcc -o $@ $^
heapsort.o : heapsort.c
	gcc -g -c $^

.PHONY:clean
clean:
	rm -f *.o heapsort
