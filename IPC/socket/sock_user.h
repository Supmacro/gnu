

#include <stdlib.h>
#include <time.h>


#define USER_NAME_SIZE 10

char uhome[][USER_NAME_SIZE] = {

    "Bob",
    "Alice",
    "Dema",
    "Kene",
    "Jack",
    "Lee",
    "Alpha",
    "Peter",
    "George",
    "Obama",
    "Trump",
    "Titan",
    "Jess",
    "Fitz",
    "Rich",
    "Bach"
};

char *active_user(char *user){

    // init RNG 
    srand(time(NULL));

    int sz = sizeof(uhome)/USER_NAME_SIZE;
    int pos = rand()%sz;

    if(sizeof(user) <= strlen(uhome[pos])){
        return NULL;
    }
    strcpy(user, uhome[pos]);

    return user;

}


