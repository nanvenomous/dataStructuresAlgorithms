#include <stdio.h>

int main() {
	int i = 1; 
	char c ='G'; 
	double d = 3.14; 
	short s = 32767;

	//printing the variables defined above along with their sizes 
	printf("Integer:\n");
	printf("\tValue: %i, Size: %lu bytes.\n", i, sizeof(i)); 

	printf("Character:\n");
	printf("\tValue: %c, Size: %lu bytes.\n", c, sizeof(c)); 

	printf("Floating Point:\n");
	printf("\tValue: %lf, Size: %lu bytes.\n", d, sizeof(d)); 

	printf("Short:\n");
	printf("\tValue: %d, Size: %lu bytes.\n", s, sizeof(s)); 

	return 0; 
}
