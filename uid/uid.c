#include <stdio.h>
#include <stdlib.h>

#include <string.h>
#include <fcntl.h>
#include <sys/types.h>
#include <errno.h>
#include <pwd.h>

int main(int argc, char *argv[])
{
    uid_t user_id = geteuid();   
    errno = 0;

    struct passwd *pw = getpwuid(user_id);
    if(!pw){
        printf("fatal error: %s\n", strerror(errno));
        exit(1);
    }

    /* struct passwd {
     *
     *      char  *pw_name;     ::user name
     *      char  *pw_passwd;   ::user password 
     *      uid_t *pw_uid;      ::user id
     *      gid_t *pw_gid;      ::group id
     *      char  *pw_gecos;    ::user real name
     *      char  *pw_dir;      ::home dir
     *      char  *pw_shell;    ::shell
     * };
     *
     * */

    char fmt[64] = {0} ;
    int j = 0;

    for(; j < 34 ; j++){fmt[j] = '-';}
    fmt[0] = fmt[strlen(fmt)] = '+';

    fprintf(stdout, "%s \n", fmt);
    fprintf(stdout, "| user name: %-20s |\n", pw->pw_name);
    fprintf(stdout, "| user pass: %-20s |\n", pw->pw_passwd);
    fprintf(stdout, "| user id:   %-20d |\n", pw->pw_uid);
    fprintf(stdout, "| group id:  %-20d |\n", pw->pw_gid);
    fprintf(stdout, "| user real: %-20s |\n", pw->pw_gecos);
    fprintf(stdout, "| home dir:  %-20s |\n", pw->pw_dir);
    fprintf(stdout, "| shell:     %-20s |\n", pw->pw_shell);
    fprintf(stdout, "%s \n", fmt);

    return 0;
}


