// Running on other ide's without any error.
// Ran all the 5 test cases successfully but in leetcode its giving run time error.

#include<stdio.h>
#include<stdbool.h>

bool isMonotonic(int* A, int ASize);
int main(){

    int test_case,z;

    scanf("%d",&test_case);

    for(z=0;z<test_case;z++){

        int n,i;

        scanf("%d",&n);

        int a[n];
        bool answer;

        for(i=0;i<n;i++)
            scanf("%d",&a[i]);

        answer = isMonotonic(a,n);

        printf("%d\n",answer);


    }

    return 0;
}


bool isMonotonic(int* A, int ASize){
    
    int i;
    
    if(A[0] <= A[1]){
        
        for(i=1;i<ASize;i++){
            if(A[i] > A[i+1] && i+1 != ASize)
                return false;
        }
    }
    else if(A[0] >= A[1]){
        for(i=1;i<ASize;i++){
            if(A[i] < A[i+1] && i+1 != ASize)
                return false;
        }
    }
    
    return true;

}

