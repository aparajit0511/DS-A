#include <stdio.h>
#include <stdlib.h>

struct node{

	int data;
	struct node* next;
};

struct node* head;

void insert_cll(int x);
void display();
void delete(int n);


int main(void) {

  printf("Hello World\n");

  int t,z;

  scanf("%d",&t);

  for(z=0;z<t;z++){

  	int n,i;

  	scanf("%d",&n);

  	int a[n];

  	for(i=0;i<n;i++){

  		scanf("%d",&a[i]);

  		insert_cll(a[i]);
  	}
    display();

    delete(n);

    display();

    head=NULL;

  }
  return 0;
}

void insert_cll(int x){

	struct node* temp = (struct node*)malloc(sizeof(struct node));
    struct node* ptr = (struct node*)malloc(sizeof(struct node));

	temp->data = x;
	temp->next = NULL;

	if(head == NULL){

		head= temp;
    temp->next=head;
    // printf("Hello World1\n");
	}

	else{
       
      ptr = head;

      while(ptr->next!=head){

      	ptr=ptr->next;
      }

      ptr->next = temp;
      temp->next = head;
      // printf("Hello World2\n");
	}
}

void display(){

	struct node* temp = (struct node*)malloc(sizeof(struct node));
  // printf("sflsjsj\n");
	temp = head;

 printf("data->%d ",head->data);
 temp=temp->next;

	while(temp!=head){
		printf("data->%d ",temp->data);

		temp=temp->next;
	}

	printf("\n");
}

void delete(int n){
    
    int x,i;
	printf("Enter the element to be deleted: \n");
  scanf("%d",&x);

	struct node* temp = (struct node*)malloc(sizeof(struct node));
	struct node* ptr = (struct node*)malloc(sizeof(struct node));
	temp=head;
    ptr=temp;
	for(i=2;i<=n;i++){

		if(i == x){
        
         temp=temp->next->next;
         ptr->next=temp;

		}
		else{
            ptr=temp;
			temp=temp->next;
		}
	}
}