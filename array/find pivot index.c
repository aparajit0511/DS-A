#include<stdio.h>

int pivotIndex(int* nums, int numsSize);
int main(){

	int test_case,z;
	scanf("%d",&test_case);

	for(z=0;z<test_case;z++){

		int n,i,item;

		scanf("%d",&n);

		int a[n];

		for(i=0;i<n;i++)
			scanf("%d",&a[i]);

		item = pivotIndex(a,n);

		printf("%d\n",item);
	}

	return 0;
}




int pivotIndex(int* nums, int numsSize){
    
    if(numsSize == 0)
        return -1;
    
    	int i,cum_sum = 0,left_cum_sum = 0;

	for(i=0;i<numsSize;i++)
		cum_sum = cum_sum + nums[i];

	

	for(i=0;i<numsSize;i++){

		if(left_cum_sum == (cum_sum - nums[i] - left_cum_sum))
			return i;

		
		left_cum_sum = left_cum_sum + nums[i];
	}

	return -1;

}

