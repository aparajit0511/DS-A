

int countBinarySubstrings(char * s){
    
    if(strlen(s) == 1)
        return 0;

    int count_zero = 0,count_one = 0,total_substrings = 0,i;

    for(i = 0;i< strlen(s);i++){

    	if(i+1 < strlen(s)){

    		if((s[i] == "0" && s[i+1] == "1") || (s[i] == "1" && s[i+1] == "0"))
    			total_substrings++;
    	} 

    	if(s[i] == "0")
    		count_zero++;

    	if(s[i] == "1")
    		count_one++;

    	if(count_zero == count_one){

    		total_substrings++;

    		if(s[i] == "1")
    			count_zero = 0;
    		else
    			count_one = 0;
    	}
    }

    return total_substrings;
    
}

