#include <stdio.h>
#include <stdlib.h>

struct node{

  int data;
  struct node* next;
};

struct node* head = NULL;

void insert(int x);
void display();
void middle();

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
    //  insert(a[i]);
    insert(a[i]);

    }
    
   display();
printf("\n");
   
   middle();


  //  display();

   head=NULL;
  }

  return 0;
}

void insert(int x){

  struct node* temp=(struct node*)malloc(sizeof(struct node));
  struct node* ptr=(struct node*)malloc(sizeof(struct node));

  temp->data = x;
  temp->next=NULL;
  if(head == NULL){

   head= temp;
  }

  else{
   
  ptr = head;
  while(ptr->next!=NULL){

    ptr=ptr->next;
  }

  ptr->next= temp;

  }
}

void display(){

struct node* ptr=(struct node*)malloc(sizeof(struct node));

ptr = head;

while(ptr!=NULL){

  printf("%d ",ptr->data);
  ptr= ptr->next;
}

}

void middle(){

    	struct node* ptr=(struct node*)malloc(sizeof(struct node));
    	struct node* temp=(struct node*)malloc(sizeof(struct node));

    	temp = head;
    	ptr = head;
        int count = 0;

    	while(temp->next!=NULL){
           
          temp = temp->next;
          count++;

          if(count % 2 == 0)
          	ptr = ptr->next;
    	} 

    	printf("middle element: %d",ptr->data);
    	printf("\n");

}