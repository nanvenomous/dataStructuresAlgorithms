#include <stdio.h>

typedef	unsigned	long uint32;

#define ESCI0_BASEADDR      ((uint32)0xFFFB0000UL)
#define ESCI1_BASEADDR      ((uint32)0xFFFB4000UL)
#define ESCI2_BASEADDR      ((uint32)0xFFFB8000UL)

void main() {
	const int arr[] = {1, 2, 3};
	printf("%d\n", arr[1]);
}
