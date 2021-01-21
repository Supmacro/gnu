#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct star{
    int  n;
    char ch;
};

typedef enum{
    false,
    true,
}bool;

bool isMatch(char * s, char * p){

    int i,j,k=0,ls = strlen(s), lp = strlen(p);
    struct star star = {.n=0,.ch=' '};
    char prev = ' ';

    for(i=0,j=0; j<lp; j++){

        if(p[j] == '.'){
            if(k)
                return false;

            prev = '.';
            if(i < ls)
                i++;
            else 
                k=1;
          
            continue;
        }

        if(p[j] == '*'){

            if(prev == '.'){
                if(j == lp-1)
                    return true;

                int n = 0;
                for(n = i; n < ls; n++){
                    if(isMatch(s+n, p+j+1))
                        return true;
                }

                if(i > 0){
                    return isMatch(s+i-1, p+j+1);
                }

                continue;
            }

            struct star st={.n=0, .ch=' '};
            for(; i < ls; i++){
                if(prev != s[i]){
                    break;
                }
                st.n++;
                st.ch = prev;
            }

            if(!k){
                st.n++;
                st.ch = prev;
            }

            if(st.n){
                star.n = st.n;
                star.ch = st.ch;
            }

            k = 0;
            continue;
        }

        if(k)
            return false;

        prev = p[j];
        if(p[j] == star.ch){
            if(--star.n < 0)
               return false; 
             
            continue;
        }

        if(p[j] != s[i]){
            k = 1;
            continue;
        }

        if(i < ls)
            i++;
    }

    if(i < ls || k)
        return false;

    return true;
}

int main(){

    char s[] = "aabcbcbcaccbcaabc", p[] = ".*a*aa*.*b*.c*.*a*";
    bool bv = isMatch(s, p);
    
    return 0;
}


