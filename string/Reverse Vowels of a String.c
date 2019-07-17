
#include<string.h>
char * reverseVowels(char * s){
    
    // s= strlwr(s);
    int left = 0,right = strlen(s) - 1;
    char temp;
    
    while(left < right){
        
        if(s[left] != "a" || s[left] != 'e' || s[left] != 'i' || s[left] != 'o' || s[left] != 'u')
            left++;
        if(s[right] != "a" || s[right] != 'e' || s[right] != 'i' || s[right] != 'o' || s[right] != 'u')
            right--;
        if(s[left] == "a" || s[left] == 'e' || s[left] == 'i' || s[left] == 'o' || s[left] == 'u' && s[right] == "a" || s[right] == 'e' || s[right] == 'i' || s[right] == 'o' || s[right] == 'u'){
            
            temp = s[left];
            s[left] = s[right];
            s[right] = temp;
            left++;
            right--;
        }
    }
    
    return s;

}

