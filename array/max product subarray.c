#include<stdio.h>
#include<limits.h>

int main(){

	int test_case,z;

	scanf("%d",&test_case);

	for(z=0;z<test_case;z++){

		int n,i;

		scanf("%d",&n);

		int a[n];
		for(i=0;i<n;i++)
			scanf("%d",&a[i]);

		int max_product;

		max_product = maxProduct(a,n);

		printf("%d\n",max_product);

	}

	return 0;
}

int maxProduct(int* nums, int numsSize){

	int max_val = nums[0],min_val = nums[0], max_pro = nums[0],i,temp;

	for(i=1;i<numsSize;i++){

		if(nums[i] < 0){
			temp = max_val;
			max_val = min_val;
			min_val = temp;
		}

		max_val = max(nums[i],max_val * nums[i]);
		min_val = min(nums[i],min_val * nums[i]);

		max_pro = max(max_pro,max_val);

	}

	return max_pro;
}

int max(int a,int b){

	if(a > b)
		return a;
	return b;
}

int min(int a,int b){

	if(a < b)
		return a;
	return b;
}