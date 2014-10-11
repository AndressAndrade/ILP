#include <stdio.h>
#include <stdlib.h>

float *alocar_vetor_termo(int colunas)
{
    float *vetor_termo;

    vetor_termo = malloc(colunas*sizeof(float));//verifica os bytes, e se temos esse espaco na memoria para alocar

    return vetor_termo;
}

float **alocar_matriz_coeficiente(int linhas, int colunas)
{
    float **matriz_coeficiente;

    int i;

    matriz_coeficiente = malloc(linhas*sizeof(float*));//asterisco aloca um ponteiro de float(aponta para um vetor),primeiro aloca todas as linhas

    for(i = 0; i < linhas; i++)
    {
        matriz_coeficiente[i] = malloc(colunas*sizeof(float));//para cada linha eu vou chamar malloc
    }

    return matriz_coeficiente;
}

//feito isso ja alocamos a matriz a dos coeficientes e o nosso vetor b de respostas
//agora iremos preencher a matriz b e matriz a

void preencher_vetor_termo(float *vetor_termo, int colunas)//retorna nada(void), dois parametros a matriz em si e seu numero de colunas
{
        int i;

        for(i = 0; i < colunas; i++)
        {
            printf("Digite o vetor[%d]: ",i+1);
            scanf("%f",&vetor_termo[i]);
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

//void eliminacao_de_gauss(float **matriz_coeficiente,float *vetor_termo, int n)
//{
//    int x,y,k,i,j,z;
//    float m,calculo,vetor[n];
//
//    for(i=0;i<n-1;i++)
//    {
//        for(j = i+1;j<n;j++)
//        {
//            m = matriz_coeficiente[j][i]/matriz_coeficiente[i][i];
//            matriz_coeficiente[j][i] = 0;
//
//        for(k = i+1;k<n;k++)
//        {
//            matriz_coeficiente[j][k] = matriz_coeficiente[j][k] - m*matriz_coeficiente[i][k];
//        }
//        vetor_termo[j] = vetor_termo[j] - m*vetor_termo[i];
//        }
//    }
//    vetor[n-1] = vetor_termo[n-1]/matriz_coeficiente[n-1][n-1];
//    for(i = n-2;i >= 0; i--)
//    {
//        calculo = 0;
//        for(j= i+1;j<n;j++)
//        {
//            calculo = calculo + matriz_coeficiente[i][j]*vetor[j];
//        }
//        vetor[i] = (vetor_termo[i] - calculo)/matriz_coeficiente[i][i];
//    }
//    printf("A resposta do SISTEMA LINEAR eh:\n\n");
//    for(z=0;z<n;z++)
//    {
//        if(vetor[z] < 0.000001 && vetor[z] > -0.000001)
//        {
//        printf("x[%d]i: %f\n",z+1,-1*vetor[z]);
//        }
//        else
//        {
//        printf("x[%d]e: %f\n",z+1,vetor[z]);
//        }
//
//    }
//        printf("X3: %f\n",-1*vetor[n - 1]);
//}
void eliminacao_de_gauss(float **matriz_coefieciente,float *vetor_termo,int linha)
{
    int i,j,k,a,b,q;
    float soma,m;
    double x[linha];
    float **matriz_coeficiente;

    for(i = 0; i < linha -1; i++)
    {
        for(j = i + 1; j < linha; j++)
        {
           m = matriz_coeficiente[j][i] / matriz_coeficiente[i][i];
           matriz_coeficiente[j][i] = 0;

           for(k = i + 1; k < linha; k++)
           {
                matriz_coeficiente[j][k] = matriz_coeficiente[j][k] - m*matriz_coeficiente[i][k];
           }
           vetor_termo[j] = vetor_termo[j] -  m*vetor_termo[i];//tambem pode se utilizar -=
        }
    }
    x[linha-1] = vetor_termo[linha-1]/matriz_coeficiente[linha-1][linha-1];
    for(a = linha-2; a >= 0; a--)//vai entrar linha por linha
    {
        soma = 0;//nao pode acumular a cada ciclo de interacao, deve ser zerado
        for(b = a + 1; b < linha; b++)//a começa em 1 e b em 2
        {
            soma = soma + matriz_coeficiente[a][b]*x[b];// Ex a12*x2
        }
        x[a] = (vetor_termo[a] - soma)/matriz_coeficiente[a][a];
    }
    printf("A solucao do SISTEMA LINEAR será:\n");
    for(q = 0; q<linha; q++)
    {
        printf("Vetor[%d]: %f\n",q+1,x[q]);

    }
//    printf("X3: %f\n",vetor[linha - 1]);

}

int main()
{
    float *vetor_termo;
    float **matriz_coeficiente;
    int linha,coluna;

    printf("Digite o numero de linhas de sua matriz:\n");
    scanf("%d",&linha);

    printf("Digite o numero de colunas de sua matriz:\n");
    scanf("%d",&coluna);
    printf("\n");

    if(linha == coluna)
    {
        if(linha >= 2 || coluna >= 2)
        {
            vetor_termo = alocar_vetor_termo (linha);
            matriz_coeficiente = alocar_matriz_coeficiente(linha,coluna);

            preencher_matriz_coeficiente(matriz_coeficiente, linha);
            preencher_vetor_termo(vetor_termo, linha);

            eliminacao_de_gauss(matriz_coeficiente,vetor_termo,linha);
        }
        else
        {
            printf("Digite os parametros corretos.");
        }
    }
    else
    {
        printf("Digite os parametros corretos.Matriz deve ser quadrada.");
    }


    return 0;

}


