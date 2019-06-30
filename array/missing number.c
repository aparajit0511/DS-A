#include<stdio.h>

int missingNumber(int* nums, int numsSize);
int main()
{ 

	int t,z;

	scanf("%d",&t);

	for(z=0;z<t;z++){

		int n,i;

		scanf("%d",&n);

		int a[n];

		for(i=0;i<n;i++)
			scanf("%d",&a[i]);

		int k = missingNumber(a,n);

		printf("%d\n",k);

	}
	//code
	return 0;
}



int missingNumber(int* nums, int numsSize){

	int i,sum = 0,actual_sum = 0;

	actual_sum = (numsSize * numsSize + numsSize )/2;

	for(i=0;i<numsSize;i++){

		sum = sum + nums[i];
	}

	return actual_sum - sum;

}

