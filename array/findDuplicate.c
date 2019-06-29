

int findDuplicate(int* nums, int numsSize){
    
    
    int S[numsSize],i;
    
    for(i=0;i<numsSize;i++)
        S[i] = 0;
    
    for(i=0;i<numsSize;i++){
        
        if(S[nums[i]] == 1)
           break;
        else
            S[nums[i]] = 1;
    }
    
return nums[i];
}

