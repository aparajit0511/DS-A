double max(double a,double b);

double findMaxAverage(int* nums, int numsSize, int k){
    
    int find = 0,count =0,i;
    double avg = 0.0,sum = 0.0,max_sum = INT_MIN;
    
    if(numsSize == 1){
        sum += nums[0];
        return sum / k;
    }
    
    for(i=0;i<numsSize;i++){
        
        sum = sum + nums[i];
        count++;
        
        if(count == k){
            max_sum = max(max_sum,sum);
            count--;
           
            sum = sum - nums[find];
            find++;
        }
    }
    
    avg = max_sum / k;
    
    return avg;

}

double max(double a,double b){
    
    if(a >= b)
        return a;
    return b;
}

