#include<stdio.h>
void add(int *a, int *b);
void subtract(int *a,int *b);

int main(){
	int x=2;
	int y=4;
	add(&x,&y);
	subtract(&x,&y);
	
	
	
	return 0;
}void add(int *a,int *b){
	int *i;
	*i=(*a)+(*b);
	printf("The sum is %d\n",*i);
}
void subtract(int *a, int *b){
	int *i;
	*i=(*a)-(*b);
	printf("The subtract is %d\n",*i);
	
}