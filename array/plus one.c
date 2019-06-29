#include<stdio.h>
#include<malloc.h>

int* plusOne(int* digits, int digitsSize, int* returnSize);

int main(){

	int t,z;

	scanf("%d",&t);

	for(z=0;z<t;z++){

		int n,i;

		scanf("%d",&n);

		int arr[n];

		for(i=0;i<n;i++)
			scanf("%d",&arr[i]);

		int* a = (int*) malloc(n+1 * sizeof(int));

		a = plusOne(arr,n,a);

		// for(i = 0; i < sizeof(a); i++)
		// 	printf("%d ",a[i]);
	}


	return 0;
}

int* plusOne(int* digits, int digitsSize, int* returnSize){

	int i,sum ;

	sum = digits[0];

	for(i=1;i<digitsSize;i++){

		sum = sum * 10;
		sum = sum + digits[i];
	}

printf("%d\n",sum);

	sum = sum + 1;
	i = 0;
	int d;

	while(sum != 0){

		returnSize[i] = sum % 10;
    printf("Go\n");
		sum /= 10;
    i++;
	}




for(i=0;i< digitsSize+1;i++)
printf("%d ",returnSize[i]);
printf("\n");

	return returnSize;


}