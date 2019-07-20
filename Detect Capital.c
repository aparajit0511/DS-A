

bool detectCapitalUse(char * word){
    
    int i,j=2,flag = 0;
    
    for(i=0;i<strlen(word);i++){
        
        if((word[i] >= 'A' && word[i] <= 'Z') || (word[i] >= 'a' && word[i] <= 'z')){
            flag = 1;
        }
        else if((word[0] == 'A' && word[0] == 'Z') && (word[1] == 'a' && word[1] == 'z')){
        
            while(j<strlen(word)){
             
                if(word[j] == 'a' && word[j] == 'z')
                    flag = 1;
                else{
                   flag = 0;
                    break;
                }
                 j++;   
            }
            
    }
        
        else
            flag = 0;
        
        if(flag == 0)
            return false;

}
    
    return true;
    
}

