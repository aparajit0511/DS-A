

bool canConstruct(char * ransomNote, char * magazine){
    
    if(strlen(ransomNote) == 0 && strlen(magazine) == 0 || strlen(ransomNote) == 0 && strlen(magazine) > 0)
        return true;
    
    int i,j=0;
    
    for(i=0;i<strlen(magazine);i++){
        
        if(ransomNote[j] == magazine[i] ){
            
            j++;
            if( j == strlen(ransomNote))
                return true;
        }
        else{
            
        }
            
    }
    
    return false;
}

