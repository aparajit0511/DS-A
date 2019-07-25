

bool checkRecord(char * s){
    
    // s = strupr(s);
    
    // if(strlen(s) == 0)
    //     return true;
    
    int i,count_A = 0;
    
    for(i=0;i<strlen(s);i++){
        
        if(s[i] == 'A')
            count_A++;
        
        if(count_A > 1)
            return false;
        
        if(s[i] == 'L' && s[i+1] == 'L' && s[i+2] == 'L' && strlen(s) >= 3)
            return false;
    }
    
    return true;

}

