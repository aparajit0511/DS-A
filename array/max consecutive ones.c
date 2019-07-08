

int findMaxConsecutiveOnes(int* nums, int numsSize){
    
    int i,count = 0,max_count = 0;
    
    for(i=0;i<numsSize;i++){
        
        if(nums[i] == 1)
            count++;
        else
            count = 0;
        
        if(count > max_count)
            max_count = count;
    }
    
    return max_count;

}

