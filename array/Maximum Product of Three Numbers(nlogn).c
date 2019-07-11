int cmpfunc (const void * a, const void * b);

int maximumProduct(int* nums, int numsSize){
    
    qsort(nums, numsSize, sizeof(int), cmpfunc);
    
    return max(nums[numsSize-1] * nums[numsSize-2] * nums[numsSize-3],nums[numsSize-1] * nums[0] * nums[1]);

}

int cmpfunc (const void * a, const void * b) {
   return ( *(int*)a - *(int*)b );
}

int max(int a,int b){
    if(a >= b)
        return a;
    return b;
}