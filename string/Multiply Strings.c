char * multiply(char * num1, char * num2){
    
    if(num1[0] == '0' || num2[0] == '0')
        return "0";

	unsigned long long int n1 = 0,n2 = 0,i=0,pro;

	while(num1[i] != '\0'){

		n1 = n1*10 + (num1[i] - 48);
		i++;
	}

	i=0;

	while(num2[i] != '\0'){

		n2 = n2*10 + (num2[i] - 48);
		i++;
	}

	pro = n1 * n2;

	unsigned long long int  rem, len = 0, n;
 
    n = pro;
    while (n != 0)
    {
        len++;
        n /= 10;
    }

    char *str = (char*)malloc(len+1 * sizeof(char));

    for (i = 0; i < len; i++)
    {
        rem = pro % 10;
        pro = pro / 10;
        str[len - (i + 1)] = rem + '0';
    }
    str[len] = '\0';
    
    // for(i=0;i<len;i++)
    //     printf("%c",str[i]);

    return str;

}

