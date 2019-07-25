
bool detectCapitalUse(char * word){

    int i,count_upper = 0;

    for(i=0;i<strlen(word);i++){

        if(isupper(word[i]))
            count_upper++;
    }

    printf("%d",count_upper);

    if(count_upper == strlen(word) || count_upper == 0)
        return true;
    else if(isupper(word[0]) != 0 && count_upper == 1)
        return true;

    return false;

}



