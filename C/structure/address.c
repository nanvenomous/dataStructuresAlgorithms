#include <stdio.h>

struct Address {
	char name[50]; 
	char street[100]; 
	char city[50]; 
	char state[20]; 
	int pin; 
} Address;

int main() {
	struct Address adr = {"Matt", "Kenmore", "Elm", "IL", 486};
	printf("City: %s\n", adr.city);
	return 0;
};
