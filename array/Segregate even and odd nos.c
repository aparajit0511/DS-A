#include<stdio.h>
#include<malloc.h>

int*  sortArrayByParity(int* A, int ASize, int* returnSize);
int main(){

	int test_case,z;

	scanf("%d",&test_case);

	for(z=0;z<test_case;z++){

		int n,i;

		scanf("%d",&n);

    int a[n];

		for(i=0;i<n;i++)
			scanf("%d",&a[i]);

      int* returnSize = (int*)malloc(n* sizeof(int));

		 returnSize = sortArrayByParity(a,n,returnSize);

     	for(i=0;i<n;i++)
	printf("%d ",returnSize[i]);
	printf("\n");
	}

	return 0;
}

int*  sortArrayByParity(int* A, int ASize, int* returnSize){

	int left = 0,right = ASize-1,i;

	// ptr = (int*) malloc(100 * sizeof(int))
	 returnSize = (int*)malloc(ASize* sizeof(int));

	for(i=0;i<ASize;i++){

		if(A[i] % 2 == 0){
      returnSize[left] = A[i];
      left++;
    }
			else{
		returnSize[right] = A[i];
    right--;
      }
	}

	return returnSize;
}