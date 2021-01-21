
all : sock_srv sock_clt sock_tty

sock_clt : sock_client.o
	gcc -o $@ $^
sock_client.o : sock_client.c
	gcc -g -c $^

sock_srv : sock_serv.o
	gcc -o $@ $^
sock_serv.o : sock_serv.c
	gcc -g -c $^

sock_tty : sock_terml.o
	gcc -o $@ $^
sock_terml.o : sock_terml.c
	gcc -g -c $^


.PHONY : clean
clean:
	rm -f *.o sock_srv sock_clt sock_tty
