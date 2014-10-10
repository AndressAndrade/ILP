#include <stdio.h>

int main()
{ 
	int i,j,n;
	printf("Qual tamanho da sua matriz quadrada?\n");
	scanf("%i", &n);
	int mtrx[n][n];
	printf("Digite os valores de sua matriz separando os valores por linha,tecle enter ao terminar a linha:\n");
	for (i = 0; i < n; i++)
	{
		printf("\n");		
		for(j = 0; j < n; j++)
		{
			scanf("%i", &mtrx[i][j]);
			printf("%i", mtrx[i][j]);
		}
	}
	return 0;
}
