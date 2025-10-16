/**
 * This file implements parallel mergesort.
 */

#include <stdio.h>
#include <string.h> /* for memcpy */
#include <stdlib.h> /* for malloc */
#include "mergesort.h"

/* this function will be called by mergesort() and also by parallel_mergesort(). */
void merge(int leftstart, int leftend, int rightstart, int rightend) {
    int l = leftstart;
    int r = rightstart;
    int index = leftstart;

    while (l <= leftend && r <= rightend) {
        if (A[l] <= A[r]) {
            B[index] = A[l];
            l++;
            index++;
        } else {
            B[index] = A[r];
            r++;
            index++;
        }
    }

    while (l <= leftend) {
        B[index++] = A[l++];
    }

    while (r <= rightend) {
        B[index++] = A[r++];
    }

    memcpy(A + leftstart, B + leftstart,
           sizeof(int) * (rightend - leftstart + 1));
    return;
}

/* this function will be called by parallel_mergesort() as its base case. */
void my_mergesort(int left, int right){
		if(left<right){
			int mid=(left+right)/2;
			my_mergesort(left,mid);
			my_mergesort(mid+1,right);
			merge(left,mid,mid+1,right);
		}
	return;
}

/* this function will be called by the testing program. */
void * parallel_mergesort(void *arg){
		return NULL;
}

/* we build the argument for the parallel_mergesort function. */
struct argument * buildArgs(int left, int right, int level){
		struct argument *args = (struct argument *) malloc(sizeof(struct argument));	
		args->left=left;
		args->right=right;
		args->level=level;
	return args;
}

