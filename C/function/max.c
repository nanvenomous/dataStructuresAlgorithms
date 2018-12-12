#include <stdio.h>

int max(int x, int y) {
    if (x > y) 
      return x; 
    else
      return y; 
} 

int main() {
	int x = 1;
	int y = 2;

	printf("find larger of %d and %d\n\n", x, y);

	int largest;
	largest = max(x, y);
	printf("the larger was: %d\n", largest);
	return 0;
}
