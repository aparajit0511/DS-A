

int findPeakElement(int* nums, int numsSize){
    
    if(numsSize == 1){
        return 0;
    }
    
    int start = 0, end = numsSize -1, mid;
    
    while(start < end){
        
        mid = (start + end)/2;
        
        if(nums[mid] < nums[mid+1])
            start = mid+1;
            else
                end = mid;
    }
    
    return start;

}

