#include<stdio.h>
#include<stdbool.h>

bool canPlaceFlowers(int* flowerbed, int flowerbedSize, int n);

int main(){

	int test_case,z;

	scanf("%d",&test_case);

	for(z=0;z<test_case;z++){

		int n,i;
		scanf("%d",&n);

		int a[n],k;

		for(i=0;i<n;i++)
			scanf("%d",&a[i]);

		scanf("%d",&k);

		bool answer;

		answer = canPlaceFlowers(a,n,k);

		printf("%d\n",answer);
	}

	return 0;
}

bool canPlaceFlowers(int* flowerbed, int flowerbedSize, int n){
    
    if(flowerbedSize == 1 && flowerbed[0] == 0)
        return true;

	int count = 0,i;

	if(flowerbed[0] == 0 && flowerbed[1] == 0){
		flowerbed[0] = 1;
		count++;
	}

	if(flowerbed[flowerbedSize-1] == 0 && flowerbed[flowerbedSize-2] == 0){
		flowerbed[flowerbedSize-1] = 1;
		count++;
	}

	for(i=1;i<flowerbedSize-1;i++){

		if(flowerbed[i-1] == 0 && flowerbed[i+1] == 0 && flowerbed[i] == 0){
			flowerbed[i] = 1;
			count++;
		}
	}

	if(count >= n)
		return true;
	return false;
}