#include <stdio.h>
#include <stdlib.h>

struct node{

	int data;
	struct node* left;
	struct node* right;
};

struct node* root = NULL;
// struct node* front = NULL;
// struct node* rear = NULL;

int n;

struct node* insert(int x,struct node* root);
void levelorder(struct node* root);
struct node* createqueue(int* front,int* rear);
void enqueue(struct node* queue,int* rear,struct node* temp);
struct node* dequeue(struct node* queue,int* front);

int main(void)
{
	/* code */

	int t,z;

	scanf("%d",&t);

	for(z=0;z<t;z++){

		int i;

		scanf("%d",&n);

		int a[n];

		for(i=0;i<n;i++){

			scanf("%d",&a[i]);

			root = insert(a[i],root);
		}

		levelorder(root);
	}
	return 0;
}


struct node* insert(int x,struct node* root){

	struct node* temp = (struct node*)malloc(sizeof(struct node));
	struct node* ptr = (struct node*)malloc(sizeof(struct node));

    temp->data = x;
    temp->left = NULL;
    temp->right = NULL;

    if(root == NULL){
    	
    	root = temp;
    }
    else if(temp->data <= root->data){
    
     root->left=insert(temp->data,root->left);
    } 
    else if(temp->data > root->data){
    	root->right=insert(temp->data,root->right);
    }	

    return root;
}

void levelorder(struct node* root){
      
      int rear,front;
    struct node* temp = (struct node*)malloc(sizeof(struct node));
    struct node* queue = createqueue(&front,&rear);

    temp = root;

    while(temp){

    	printf("%d ",temp->data);

    	if(temp->left){

    		enqueue(queue,&rear,temp->left);
    	}

    	if(temp->right){

    		enqueue(queue,&rear,temp->right);
    	}

    	temp = dequeue(queue,&front);
    }

}

struct node* createqueue(int* front,int* rear){

       
       struct node* queue = (struct node*)malloc(sizeof(struct node)*n);

       *rear = 0,front = 0;

       return queue;

}


void enqueue(struct node* queue,int* rear,struct node* temp){

	queue[*rear] = temp;
	(*rear)++;
}

struct node* dequeue(struct node* queue,int* front){

	(*front)++;

	return queue[*front-1]
}