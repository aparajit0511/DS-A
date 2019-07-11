

int fib(int N){
    
    if(N == 1)
        return 1;
    
    int i,a=0,b=1,c=0;
    
    for(i=1;i<N;i++){
        
        c = a + b;
        a = b;
        b = c;
    }
    
    return c;

}

