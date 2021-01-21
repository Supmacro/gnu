
#include <locale.h>
#include <stdio.h>

#include <string.h>

typedef struct locale {
    int   category;
    char *name;
}lc_type;


lc_type lconst[] = {  
        {LC_ALL,      "LC_ALL"},
        {LC_COLLATE,  "LC_COLLATE"},
        {LC_CTYPE,    "LC_CTYPE"},
        {LC_MONETARY, "LC_MONETARY"},
        {LC_NUMERIC,  "LC_NUMERIC"},
        {LC_TIME,     "LC_TIME"}};


void lc_print_locale(int category, const char *locale)
{
    char *p = setlocale(category, locale);
    if(!p){
        return;
    }
    int j;
    for(j = 0; j < sizeof(lconst)/sizeof(lc_type); j++){
        if(lconst[j].category == category){
            fprintf(stdout, "%7s %s = %s\n", " ", lconst[j].name, p);
        }
    }
}


int main(int argc, char *argv[])
{
    //setenv("LC_TIME", "zh_CN.gb2312", 1);
    fprintf(stdout, "\"C\"\n");
    lc_print_locale(LC_ALL, "C"); 
    lc_print_locale(LC_COLLATE, "C"); 
    lc_print_locale(LC_CTYPE, "C"); 
    lc_print_locale(LC_MONETARY, "C"); 
    lc_print_locale(LC_NUMERIC, "C"); 
    lc_print_locale(LC_TIME, "C"); 

    fprintf(stdout, "\"\"\n");
    lc_print_locale(LC_ALL, ""); 
    lc_print_locale(LC_COLLATE, ""); 
    lc_print_locale(LC_CTYPE, ""); 
    lc_print_locale(LC_MONETARY, ""); 
    lc_print_locale(LC_NUMERIC, ""); 
    lc_print_locale(LC_TIME, ""); 
    printf("%7s:%s\n", "", zh_CH);

    fprintf(stdout, "\"NULL\"\n");
    lc_print_locale(LC_ALL, NULL); 
    lc_print_locale(LC_COLLATE, NULL); 
    lc_print_locale(LC_CTYPE, NULL); 
    lc_print_locale(LC_MONETARY, NULL); 
    lc_print_locale(LC_NUMERIC, NULL); 
    lc_print_locale(LC_TIME, NULL); 

    return 0;
}
