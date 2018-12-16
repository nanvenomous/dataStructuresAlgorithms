#include <stdio.h>

#include "headers/macro.h"
#include "headers/functionInHeader.h"
#include "headers/declareSrc.h"

#define NUM -7

int main() {

	printf("(|%d| - 4)*2 = %d\n", NUM, multiplyByTwo(subtractFour(ABS(NUM))));
	return 0;
}
