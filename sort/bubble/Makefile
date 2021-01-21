
bubsort : bubsort.o
	gcc -o $@ $^
bubsort.o : bubsort.c
	gcc -g -c $^

.PHONY:clean
clean:
	rm -f *.o bubsort
