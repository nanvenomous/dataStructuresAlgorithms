#include <stdio.h>

#include "headers/macro.h"
#include "headers/functionInHeader.h"

#define NUM -7

int main() {

	printf("|%d| - 4: %d\n", NUM, subtractFour(ABS(NUM)));
	return 0;
}
