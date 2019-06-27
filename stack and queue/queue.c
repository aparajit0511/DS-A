#include <stdio.h>

int front = -1, rear = -1;

void insert_queue(int x,int queue[]);
void display(int queue[]);
void dequeue();

int main(void){

    int t,z;
    
    scanf("%d",&t);

    for(z=0;z<t;z++){

    	int n,i;

    	scanf("%d",&n);

    	int a[n],queue[n];
        

        for(i=0;i<n;i++){

        	scanf("%d",&a[i]);

        	insert_queue(a[i],queue);
        }

        display(queue);

        dequeue();

        display(queue);

        dequeue();

        display(queue);

        front = -1,rear = -1;

    }
	return 0;
}


void insert_queue(int x,int queue[]){

	if(front == -1 && rear == -1){

		queue[++rear] = x;
		front++;
	}
	else {

		queue[++rear] = x;
	}
}



void display(int queue[]){

    int i;

    for(i=front;i<=rear;i++){

    	printf("%d ",queue[i]);
    }

    print("\n");
}



void dequeue(){

	front++;
}