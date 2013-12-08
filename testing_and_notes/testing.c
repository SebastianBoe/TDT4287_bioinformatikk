#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <omp.h>

#define lines (1000000)
#define sequence_length (50)
#define input_size (lines * (sequence_length + 1))

static char adapter [] = "TGGAATTCTCGGGTGCCAAGGAACTCCAGTCACACAGTGATCTCGTATGCCGTCTTCTGCTTG";

int main( void ){
	char output_buffer[15];
	for(int i = 0; i < 5; i++){
		sprintf(output_buffer + i * 3, "%02d\n", i);
	}
	
	for(int i = 0; i < 15; i++){
		putchar(output_buffer[i]);
	}
}

