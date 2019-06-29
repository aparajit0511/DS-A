#include<stdio.h>

double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size);

int main(){

	int t,z;

	scanf("%d",&t);

	for(z=0;z<t;z++){

		int n,m,i;
		scanf("%d %d",&n,&m);

		int arr1[n],arr2[m];

		for( i=0;i<n;i++)
			scanf("%d",&arr1[i]);

		for(i=0;i<m;i++)
			scanf("%d",&arr2[i]);

		double median;

		median = double findMedianSortedArrays(arr1,n,arr2,m);
	}

	return 0;
}




double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size){

	int i = 0,j = 0, count;

	double m1 = -1 ,m2 = -1;

	if((nums1Size + nums2Size)%2 == 1){


	for(count = 0; count <= (nums1Size + nums2Size)/2; count++){

		if(i != nums1Size && j != nums2Size){


		m1 = (nums1[i] > nums2[j])? nums2[j++]: nums1[i++];

		}
		else if(i < nums1Size){
			m1 = nums1[i++];
		}
		else{

			m1 = nums2[j++];
		}

	}

	return m1;
	}

	else{
			for(count = 0; count <= (nums1Size + nums2Size)/2; count++){
				m2 = m1;

		if(i != nums1Size && j != nums2Size){


		m1 = (nums1[i] > nums2[j])? nums2[j++]: nums1[i++];

		}
		else if(i < nums1Size){
			m1 = nums1[i++];
		}
		else{

			m1 = nums2[j++];
		}

	}

	return (m1+m2)/2;


	}


}

