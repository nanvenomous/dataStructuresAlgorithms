#include <stdio.h>

#include "macro.h"
#include "function.h"
#include "declareSrc.h"

#define NUM -7

int main() {

	printf("(|%d| - 4)*2 = %d\n", NUM, multiplyByTwo(subtractFour(ABS(NUM))));
	return 0;
}
