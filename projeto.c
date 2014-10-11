#include <stdio.h>
#include <stdlib.h>

float *alocar_vetor(int colunas)
{
    float *vetor_termo;
    
    vetor_termo = malloc(colunas*sizeof(float)) ;
    
    return vetor_termo;

}

float **alocar_matriz(int linhas, int colunas)
{
    float **matriz_coeficiente;
    
    int i;
    
    matriz_coeficiente = malloc(linhas*(float*));
    
    for(i = 0 ; i < colunas; i++)
    {
        matriz_coeficiente[i] = malloc(colunas*sizeof(float));
    }
    
    return matriz_coeficiente;

}

void preencher_vetor_termo(float *vetor_termo, int colunas)
{
        printf("Digite o vetor, separando os valores por espaço:\n")
        
        int i;
        
        for(i = 0; i < colunas; i++)
        {
            scanf("%f ",&vetor_termo[i]);
        }
}

void preencher_matriz_coeficiente(float **matriz_coeficiente, int linhas)
{
    int i,j;

        for(i = 0; i < linhas; i++)
        {
            for(j = 0; j < linhas; j++)
            {
                 printf("Digite a matriz[%d][%d]: ",i+1,j+1);
                 scanf("%f", &matriz_coeficiente[i][j]);
            }
        }
    printf("\n");
}

void metodo_jordan(**matriz coeficiente,*vetor_termo,int n)
{
    int i,j;
    float m;
    for(j = 0; j < n; j++)
    {
        for(i = 0; i < n; i++)
        {
            
        }
    }


}


int main()
{


}
