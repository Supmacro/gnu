
#include <stdio.h>
#include <stdlib.h>

#include <string.h>
#include <errno.h>

/* +-------------------------+
 * | PIPE READ LINE          |
 * +-------------------------+
 * */

int main(int argc, char *argv[])
{
    FILE *pipe = popen("echo $PATH", "r");
    if(pipe == NULL){
        printf("fatal: %s\n", strerror(errno));
        exit(1);
    }

    char line[256] = {0};
    int size = fread(line, 1, 256, pipe);
    if(size < 0){
        printf("fatal: %s\n", strerror(errno));
        exit(1);
    }

    pclose(pipe);

    fprintf(stdout, "%s", line);
    return 0;
}
