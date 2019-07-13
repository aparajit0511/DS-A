

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* numbers, int numbersSize, int target, int* returnSize){

	*returnSize = 2;
	int *arr = malloc(*returnSize * sizeof(int));

	int left = 0,right = numbersSize - 1,i,sum;

	while(left < right){

		sum = numbers[left] + numbers[right];

		if(sum == target){
			arr[0] = left+1;
			arr[1] = right+1;
			break;
		}

		if(sum >= target)
			right --;
		else
			left++;
	}

	return arr;

	}


