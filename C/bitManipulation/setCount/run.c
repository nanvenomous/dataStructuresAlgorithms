#include <stdio.h>

typedef unsigned int uint;

uint returnBitCount(uint n) {
	uint c; // the total bits set in n
	for (c = 0; n; n >>= 1) {
		c += n & 1;
	}
	return c;
}

void main() {
	uint asciiNum = 8;
	uint result;
	result = returnBitCount(asciiNum);
	printf("result: %d\n", result);
}