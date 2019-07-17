void reverse(int b,int e,char s[]);

char * reverseWords(char * s){
    
    int i=0,j=0;
    
    for(i=0;i<=strlen(s);i++){
        
        if(s[i] == ' ' || s[i] == '\0'){
            
            reverse(j,i-1,s);
            j = i+1;
        }
    }
    
    return s;

}

void reverse(int b,int e,char s[]){
    
    while(b < e) {
         s[b] = s[b] ^ s[e];
         s[e] = s[b] ^ s[e];
         s[b] = s[b] ^ s[e];
           b++;
           e--;
      }
}