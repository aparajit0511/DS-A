// # Logic and Approach:
// # I used two arrays count_array and seq_array. count_array to capture the sequence for the nth term and sequence array as an input array.
// # Sequence array has a base input as "1", after that i calculate the sequence and append it to count_array.

// Python solution is working.

char * countAndSay(int n){

	if( n == 1)
		return "1";

	char* seq_array = (char*)malloc(sizeof(char)*1);
	char* count_array = (char*)malloc(sizeof(char)*30);

	seq_array[0] = 49;

	int count_char = 1,count_n = 1,i,j = 0;

	while(count_n < n){

		for(i = 0; i < strlen(seq_array); i++){

			if(seq_array[i] == seq_array[i+1] && i+1 < strlen(seq_array)){

				count_char++;
				i++;
				continue;
			}

			count_array[j] = ('0' + count_char);
			j++;
			count_array[j] = seq_array[i];
			j++;
			count_char = 1;
			i++;
		}

		free(seq_array);
		char* seq_array = (char*)malloc(sizeof(char)*j);

		strncpy(seq_array,count_array,j);
		j = 0;

		free(count_array);
		char* count_array = (char*)malloc(sizeof(char)*30);

		count_n++;
	}
    
    free(count_array);

	return seq_array;

}

