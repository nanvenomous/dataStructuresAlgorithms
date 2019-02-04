#include <stdio.h>
#include "arrayOperations/all.h"

int main() {
	// Declare an array to a certain size
	int len = 10;
	int arr[len];
	// Point arrPtr to the address of array's first element
	int *arrPtr = &arr[0];

	// Initialize arrPtr
	int i;
	for (i = 0; i < len; i++) {
		arrPtr[i] = 100*i;
	}

}
