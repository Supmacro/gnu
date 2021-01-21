
all : pipe popen 

popen : popen.o
	gcc -o $@ $^
pipe : pipe.o
	gcc -o $@ $^

%.o : %.c 
	gcc -g -c $<

.PHONY:clean
clean:
	rm -f pipe popen *.o
