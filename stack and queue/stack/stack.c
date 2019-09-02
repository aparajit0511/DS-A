#include <stdio.h>

int top = -1;

void push(int x,int stack[]);
void display(int stack[]);
void pop();

int main(void){

	int t,z;
    
    scanf("%d",&t);

    for(z=0;z<t;z++){

    	int n,i;

    	scanf("%d",&n);

    	int a[n],stack[n];

    	for(i=0;i<n;i++){

    		scanf("%d",&a[i]);

    		push(a[i],stack);
    	}

    	display(stack);

    	pop();

    	display(stack);

    	pop();

    	display(stack);

      top = -1;
    }

	return 0;
}

void push(int x,int stack[]){

	if(top == -1){

		stack[++top] = x;
	}
	else{

		stack[++top] = x;
	}
}

void pop(){

	top--;
}

void display(int stack[]){

	int i;

	for(i=0;i<=top;i++){
		printf("%d ",stack[i]);
	}
  printf("\n");
}