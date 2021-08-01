#include <stdlib.h>
#include <stdio.h>

unsigned int collatz(unsigned int num, unsigned int *ppasso);

int main(void){
	unsigned int num = 0, passo = 0;

	printf("Numero: ");
	scanf(" %d", &num);

	while(num != 1){
		num = collatz(num, &passo);
	}

	return(0);
}

unsigned int collatz(unsigned int num, unsigned int *ppasso){
	if(num % 2 == 0) {
		num = num / 2;
	} else {
		num = (num * 3) + 1;
	}
	*ppasso = *ppasso + 1;
	printf("Passo %d - %d\n", *ppasso, num);

	return num;
}
