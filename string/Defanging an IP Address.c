

char * defangIPaddr(char * address){
    
    int add_len = strlen(address);
    char *key = (char*)malloc(add_len+7 * sizeof(char));
    // char key[add_len+6];
    
    int i,c=0;
    
    for(i=0;i<add_len;i++){
        
        if(address[i] >= 48 && address[i] <= 57){
            key[c] = address[i];
            c++;
        }
        if(address[i] == 46){
            key[c] = '[';
            c++;
            key[c] = address[i];
            c++;
            key[c] = ']';
            c++;
        }
    }
    
    key[c] = '\0';
    return key;

}

