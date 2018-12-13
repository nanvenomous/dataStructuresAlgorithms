#include <stdio.h>
//#include "length.c"

void printArray(int arr[], int len) {
	printf("{");
	int i;
	for (i = 0; i < len; i++) {
		printf(" %d", arr[i]);
	}
	printf(" }\n");
	return;
}
