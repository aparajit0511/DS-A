bool isValid(char * T){
    
    if((T >= 'A' && T <= 'Z') || (T >= 'a' && T <= 'z')){
        
        return true;
    }
    return false;
}
char * reverseOnlyLetters(char * S){
    
    int start = 0;
    int end = strlen(S) - 1;
    char * temp;
    
    
    while (start < end){
        
        if(!(isValid(S[start]))){start++; continue;}
        if(!(isValid(S[end]))){end--; continue;}
        
        temp = S[start];
        S[start] = S[end];
        S[end] = temp;
        start++;
        end--;
        
    }
    
    return S;

}