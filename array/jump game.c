#include<stdio.h>

int findjump(int a[],int n);

int main()
{
	//code

	int t,z;

	scanf("%d",&t);

	for(z=0;z<t;z++){

		int n,i;

		scanf("%d",&n);

		int a[n];

		for(i=0;i<n;i++)
			scanf("%d",&a[i]);

		int k;

		k = findjump(a,n);

		printf("%d\n",k);

	}

	return 0;
}

int findjump(int a[],int n){

	int count=0,i=0,flag=0;

	while(i < n){

		i = i + a[i];

		if(flag == i)
			break;

		if(i == n-1 || i > n)
			return count+1;

		count++;
		flag = i;
	}

	return -1;

}