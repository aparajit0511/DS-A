

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* searchRange(int* nums, int numsSize, int target, int* returnSize){
    
    *returnSize = 2;
    int *arr = malloc(*returnSize * sizeof(int));
    arr[0] = -1, arr[1] = -1;
    
    int left = 0,right = numsSize - 1,flag = 0,slag = 0;
    
    while(left <= right){
        
        if(nums[left] != target)
            left++;
        else{
            arr[0] = left;
            flag = 1;
        }
        
        if(nums[right] != target)
            right--;
        else{
            arr[1] = right;
            slag = 1;
        }
        
        if(flag == 1 && slag == 1)
            break;
    }
    
    return arr;

}

