// Used the same approach as given on the internet but wasnt able to solve it.
// Got Stuck in this test case.

// Input:
// [10,-7,13,-14,30,16,-3,-16,-27,27,19]
// Output:
// false
// Expected:
// true

// Approach used: Calculated the cumulative sum of the array, divided it by 3.
//                for i to n:
//                	checked the value of count upto cumulative_sum / 3 and set it to 0 if found a subarray.


#include<stdio.h>
#include<stdbool.h>

bool canThreePartsEqualSum(int* A, int ASize);
int main(){

	int test_case,z;

	for(z=0;z<test_case;z++){

		int n,i;

		scanf("%d",&n);

		int a[n];
		bool answer;

		for(i=0;i<n;i++)
			scanf("%d",&a[i]);

		answer = canThreePartsEqualSum(a,n);

		printf("%d\n",answer);


	}

	return 0;
}

bool canThreePartsEqualSum(int* A, int ASize){
    
    	int cumulative_sum = 0,i,count=0,div=0;

	for(i=0;i<ASize;i++)
		cumulative_sum = cumulative_sum + A[i];

	for(i=0;i<ASize;i++){

		if(count == cumulative_sum/3){

			count = 0;
            div++;
		}

		count = count + A[i];
	}

	if(count != cumulative_sum/3 && A[ASize-1] != 0)
		return false;
	return true;

}