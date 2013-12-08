#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>

#define n_lines (1000000)
#define sequence_length (50)

int main( int argc, char* argv[] )
{
 //start clock
 clock_t begin, end;
 double time_spent;
 begin = clock();
 
 //initialization
 int* buffer = malloc(sizeof(int) * 3 * n_lines);
 char* input_buffer;
 char line [80];
 char adapter [] = "TGGAATTCTCGGGTGCCAAGGAACTCCAGTCACACAGTGATCTCGTATGCCGTCTTCTGCTTG";
 long numbytes;
 
 fseek(stdin, 0L, SEEK_END);
 numbytes = ftell(stdin);
 fseek(stdin, 0L, SEEK_SET);
 input_buffer = (char*)calloc(numbytes, sizeof(char));
 fread(input_buffer, sizeof(char), numbytes, stdin);
 
 for(int i = 0; i < n_lines; i++)
 {
 	buffer[i] = 0;
 	int input_index = i * (sequence_length + 1);
 	for(int j = 0; j < sequence_length; j++)
 	{
 		if( strncmp(adapter, &input_buffer[j + input_index], sequence_length - j))
 		{
 			buffer[i] = sequence_length - j;
 			break;
 		}
 	}
 }
 
 
 //calculate into buffer
 while( (scanf("%s", line) != EOF))
 {
   //Check buffer size
   if(buffer_index + 1 == buffer_size)
   {
     buffer_size *= 2;
     buffer = realloc(buffer, buffer_size * sizeof(int));
   }
   
   buffer[buffer_index] = 0;
   int i;
   for(i = 0; i < strlen(line); i++)
   {
     if(strncmp(adapter, &line[i], strlen(line) - i) == 0)
     {
        buffer[buffer_index] = strlen(line) - i;
        break;
     }
   }
   
   buffer_index++;
 }
 
 //write answer to stdout
 int i;
 for(i = 0; i <= buffer_index; i++){
  printf("%d\n", buffer[i]);
 }
 
 //log runtime
 end = clock();
 time_spent = (double)(end - begin) / CLOCKS_PER_SEC;
 FILE* fp = fopen("runtime_data.txt", "a");
 fprintf(fp, "%f\n", time_spent);
 
 //release resources and exit
 free(buffer);
 return 0;
}
