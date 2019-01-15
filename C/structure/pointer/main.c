#include <stdio.h>
#include "headers/dec.h"
#include "headers/types.h"

void layer(Address *adr) {
	displayAddress(adr);
}

int main() {
	Address adr = {"Matt", "Kenmore", "Elm", "IL", 486};
	layer(&adr);
	return 0;
};