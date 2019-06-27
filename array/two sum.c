	#include<stdio.h>
	#include<stdbool.h>
	#define MAX 10000

	int main(){
		
		int t,z;

		scanf("%d",&t);

		for(z=0;z<t;z++){

			int n,target,S[MAX] = {0},temp,flag = 0;

			scanf("%d",&n);

			int a[n];

			for(int i=0;i<n;i++)
				scanf("%d",&a[i]);

			scanf("%d",&target);

			for(int i=0;i<n;i++){

				temp = target - a[i];
				 if(S[temp] == 1){
				 	printf("%d %d\n",temp,a[i]);
				 	printf("Yes\n");
				 	flag = 1;
				 }
				 S[temp] = 1;


			}

			if(flag == 0)
				printf("No\n");


		}

		return 0;


	}