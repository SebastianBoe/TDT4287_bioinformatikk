#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <omp.h>

#define lines (1000000)
#define sequence_length (50)
#define input_size (lines * (sequence_length + 1))

static char adapter [] = "GCCTCTGGATGCGGTAATTGTCCCTGAGTGGGAACAGGCACCACCCGCTG";

int main( void ){	
 	//allocate memory for input
 	char* input_buffer =  (char*) calloc(input_size, sizeof(char)); 	
 	char* output_buffer = (char*) malloc(lines * 3);
 	
	//read input from standard input and write to memory
	fread(input_buffer, sizeof(char), input_size, stdin);
	
 	//#pragma omp parallel for schedule(static)
 	for(int i = 0; i < lines; i++){
 		int match_length = 0;
		for(int j = 0; j < sequence_length; j++){
	 		if(strncmp(adapter, &input_buffer[j + i * (sequence_length + 1)], sequence_length - j) == 0){
	 			match_length = sequence_length - j;
	 			break;
	 		}
	 	}
		sprintf(output_buffer + i * 3, "%02d\n", sequence_length - match_length);
	}
	
	fputs(output_buffer, stdout);
	
 	//release resources
 	free(input_buffer);
 	free(output_buffer);
}

