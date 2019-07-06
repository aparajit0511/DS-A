Line 50: Char 12: runtime error: index 3 out of bounds for type 'int [*]' (solution.c)
Test Case: [1,2,4]

#include<stdio.h>
#include<limits.h>


int maxProfit(int* prices, int pricesSize);

int main(){

	int test_case,z;

	scanf("%d",&test_case);

	for(z=0;z<test_case;z++){

		int pricesSize;

		scanf("%d",&pricesSize);

		int i,price[pricesSize];

		for(i=0;i<pricesSize;i++)
			scanf("%d",&price[i]);

		int profit;

		profit = maxProfit(price,pricesSize);

		printf("%d",profit);
		printf("\n");

	}

	return 0;
}


int maxProfit(int* prices, int pricesSize){

	int value[pricesSize],c=0,profit = 0,maxProfit = 0,i,z,alt_profit = 0;

	for(i=0;i<pricesSize;i++){

    if(i+1 == pricesSize)
    break;

		if(prices[i] < prices[i+1]){

      if(value[c-1] != prices[i])
         value[c++] = prices[i];
      
      value[c++] = prices[i+1];


		profit = value[c-1] - value[c-2];
    printf("Buy: %d\n",value[c-2]);
    printf("Sell: %d\n",value[c-1]);
    printf("Profit: %d\n",profit);

    for(z=0;z<c-2;z++){
        
        alt_profit = value[c-1] - value[z];
        if(profit < alt_profit)
        profit = alt_profit;
    }

		if(profit > maxProfit)
			maxProfit = profit;

	}

    }

  printf("%d\n",maxProfit);

	return maxProfit;
}