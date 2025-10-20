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

    // Compare and merge the two halves into B
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

    // Copy any remaining elements from the left half
    while (l <= leftend) {
        B[index++] = A[l++];
    }

    // Copy any remaining elements from the right half
    while (r <= rightend) {
        B[index++] = A[r++];
    }

    // Copy the merged elements from B back to A
    memcpy(A + leftstart, B + leftstart,
           sizeof(int) * (rightend - leftstart + 1));
    return;
}

/* this function will be called by parallel_mergesort() as its base case. */
void my_mergesort(int left, int right){
		if(left<right){
			int mid=(left+right)/2;

            // Recursively sort left and right halves
			my_mergesort(left,mid);
			my_mergesort(mid+1,right);

            // Merge the sorted halves
			merge(left,mid,mid+1,right);
		}
	return;
}

/* this function will be called by the testing program. */
void * parallel_mergesort(void *arg){
    struct argument *args = (struct argument *) arg;
    int left = args->left;
    int right = args->right;
    int level = args->level;

    if (left < right) {
        // check if we can create more threads
        if (level < cutoff) {
            int mid = (left + right) / 2;

            // build arguments for left and right subarrays
            struct argument *left_args = buildArgs(left, mid, level + 1);
            struct argument *right_args = buildArgs(mid + 1, right, level + 1);

            pthread_t left_thread;
            pthread_t right_thread;

            // create threads for left and right subarrays so they can be sorted in parallel
            pthread_create(&left_thread, NULL, parallel_mergesort,
                           (void *)left_args);
            pthread_create(&right_thread, NULL, parallel_mergesort,
                           (void *)right_args);

            // wait for both threads to finish
            pthread_join(left_thread, NULL);
            pthread_join(right_thread, NULL);

            // merge the sorted subarrays
            merge(left, mid, mid + 1, right);
        } else {
            // max number of threads reached, use regular mergesort
            my_mergesort(left, right);
        }
    }
    return NULL;
}

/**
 *  we build the argument for the parallel_mergesort function. 
 * 
 *  Parameters:
 *  left:  starting index of subarray
 *  right: ending index of subarray
 *  level: current recursion level
 * */
struct argument * buildArgs(int left, int right, int level){
		struct argument *args = (struct argument *) malloc(sizeof(struct argument));	
		args->left=left;
		args->right=right;
		args->level=level;
	return args;
}

