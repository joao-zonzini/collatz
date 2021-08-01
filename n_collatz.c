#include <stdlib.h>
#include <stdio.h>

unsigned int collatz(unsigned int num, unsigned int *ppasso);

int main(int argc, char *argv[]){

	if(argc < 2){
		exit(0);
	}

	unsigned int num = 0, passo = 0;

	num = atoi(argv[1]);

	while(num != 1){
		num = collatz(num, &passo);
	}

	printf("%d\n", passo);
	
	return(0);
}

unsigned int collatz(unsigned int num, unsigned int *ppasso){
	if(num % 2 == 0) {
		num = num / 2;
	} else {
		num = (num * 3) + 1;
	}
	*ppasso = *ppasso + 1;

	return num;
}
