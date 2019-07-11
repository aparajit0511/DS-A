

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

int cmpfunc (const void * a, const void * b) ;

int* sortedSquares(int* A, int ASize, int* returnSize){

	int i;
	*returnSize = ASize;

	for(i=0;i<ASize;i++)
		A[i] = A[i] * A[i];

	qsort(A, ASize, sizeof(int), cmpfunc);

	return A;
}

int cmpfunc (const void * a, const void * b) {
   return ( *(int*)a - *(int*)b );
}

