#include<stdio.h>
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

		long int product=1;

		int p[n];

		for(i=0;i<n;i++){

			product = product * a[i];
		}

		for(i=0;i<n;i++){

			p[i] = product / a[i];
		}

		for(i=0;i<n;i++)
			printf("%d ",p[i]);
		printf("\n");
	}
	return 0;
}