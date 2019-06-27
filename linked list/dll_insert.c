#include <stdio.h>
#include <stdlib.h>

struct node{

	int data;
	struct node* left;
	struct node* right;
};

struct node* head=NULL;

void insert(int x);
void display();

int main(void){


int t,z;
scanf("%d",&t);

for(z=0;z<t;z++){

	int n,i;
	scanf("%d",&n);

	int a[n];

	for(i=0;i<n;i++){

		scanf("%d",&a[i]);
		insert(a[i]);
	}

	display();

	head=NULL;
}
	return 0;
}

void insert(int x){

	struct node* temp= (struct node*)malloc(sizeof(struct node));
	struct node* ptr= (struct node*)malloc(sizeof(struct node));

	temp->left=NULL;
	temp->right=NULL;
	temp->data=x;

	if(head == NULL){

		head=temp;
	}
	else{


    head->left=temp;
    temp->right=head;
    head=temp;
	}
}


void display(){

struct node* ptr= (struct node*)malloc(sizeof(struct node));

ptr=head;

while(ptr!=NULL){
    
    printf("%d ",ptr->data);
	ptr=ptr->right;
}

}

//INSERT AT END

// void insert(int x){

// 	struct node* temp= (struct node*)malloc(sizeof(struct node));
// 	struct node* ptr= (struct node*)malloc(sizeof(struct node));

// 	temp->left=NULL;
// 	temp->right=NULL;
// 	temp->data=x;

// 	if(head == NULL){

// 		head=temp;
// 	}
// 	else{

// 		ptr=head;
// 		while(ptr->right!=NULL){

// 			ptr=ptr->right;
// 		}

// 		ptr->right=temp;
//     temp->left=ptr;

    
// 	}
// }