

int numSubarrayProductLessThanK(int* nums, int numsSize, int k){
    
    if(k <= 1)
        return 0;
    
    int r,l=0,ans=0,pro=1;
    
    for(r=0;r<numsSize;r++){
        
        pro = pro * nums[r];
        while(pro >= k){
            
            pro = pro / nums[l++];
        }
        
        ans += r - l + 1;
    }
    
    return ans;

}

