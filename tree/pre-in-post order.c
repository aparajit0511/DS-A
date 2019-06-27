#include <stdio.h>
#include <stdlib.h>

struct node{

	int data;
	struct node* left;
	struct node* right;
};

struct node* root = NULL;

struct node* insert(struct node* root,int x);
struct node* getnode(int x);
void inorder(struct node* root);
void postorder(struct node* root);
void preorder(struct node* root);

int main(void){


   int t,z;

   scanf("%d",&t);

   for(z=0;z<t;z++){
    
    int n,i;

   	scanf("%d",&n);

   	int a[n];

   	for(i=0;i<n;i++){

   		scanf("%d",&a[i]);

   		root = insert(root,a[i]);

   	}
    
    printf("Inorder: ");
   	inorder(root);

   	printf("Postorder: \n");

   	postorder(root);

   	printf("Preorder: \n");

   	preorder(root);

   	printf("\n");

   	root=NULL;

   }
	return 0;
}


struct node* insert(struct node* root,int x){

	

	if(root == NULL){
       
       root = getnode(x);

	}
	else if(x <= root->data){

		root->left = insert(root->left,x);
	}
	else{

		root->right = insert(root->right,x);
	}

	return root;
}

struct node* getnode(int x){
  

  struct node* temp = (struct node*)malloc(sizeof(struct node));

  temp->data = x;
  temp->left = NULL;
  temp->right = NULL;

  return temp;
}


void inorder(struct node* root){

	if(root == NULL)
		return;

	else{

		 inorder(root->left);
		printf("%d ",root->data);
		inorder(root->right);
	}
}


void postorder(struct node* root){

	if(root == NULL)
		return;

	else{

		 inorder(root->left);
		inorder(root->right);
		printf("%d ",root->data);
	}
}


void preorder(struct node* root){

	if(root == NULL)
		return;

	else{
          
          printf("%d ",root->data);
		 inorder(root->left);
		inorder(root->right);
		
	}
}
