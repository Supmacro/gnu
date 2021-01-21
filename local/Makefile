
all : locale

%.o : %.c
	gcc -g -c $<

locale : locale.o
	gcc -o $@ $^

.PHONY:clean
clean:
	rm -f *.o locale
