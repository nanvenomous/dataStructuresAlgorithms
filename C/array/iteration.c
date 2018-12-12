#include <stdio.h>

int main() {
	// Declare an array to a certain size
	int arr[10];
	int *arrPtr = &arr[0];
	int i;
	for (i = 0; i < 10; i++) {
		arr[i] = 100*i;
	}
	for (i = 0; i < 10; i++) {
		printf("element[%d] = %d\n", i, arr[i]);
	}
}
