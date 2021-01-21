

#define fatal(s) { \
    printf("fatal error: %s %s:%d \r\n", s,__FILE__,__LINE__); \
    exit(-1); \
}

#define login_clt(clt_ip, clt_port) { \
    printf(" \n"); \
    printf(" +---------------------------------+\n");  \
    printf(" | Connect to host %-15s |\n", clt_ip);    \
    printf(" | %-11s %-20s|\n", __DATE__, __TIME__);   \
    printf(" +---------------------------------+\n");  \
}

#define login_svr(clt_ip, clt_port) { \
    printf(" \n"); \
    printf(" +---------------------------------------+\n"); \
    printf(" | [News] %-11s %-19s|\n", __DATE__, __TIME__); \
    printf(" | Connection from client %-15s|\n", clt_ip);   \
    printf(" +---------------------------------------+\n"); \
}

#define login_tty() { \
    printf(" \n"); \
    printf(" +---------------------------------+\n"); \
    printf(" | [Message terminal] >>>>>>>>     |\n"); \
    printf(" | %-11s %-20s|\n", __DATE__, __TIME__);  \
    printf(" +---------------------------------+\n"); \
}


#define MSG_BUFF_SIZE 1024

#define UNIX_BOCKLOG     64
#define UNIX_EPOLL_SIZE  64
#define UNIX_KERN_PAGE   4096




