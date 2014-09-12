##L_1 = [2,2,1,3,1,1]
##L_2 = [4,1,4]

def cond_de(L):
    E = L[:] ## cria uma lista igual a L
    for termos_L in L: ##Analisa termo por termo
        c = 0 # contador
        j = 0 # controle
        while c < len(E): #Enquanto c eh menor que o tamanho da lista
            if not termos_L == E[c]: # se o termo nao corresponde ao item
                c = c + 1 # contador soma 1, e assim se pula para o proximo indice para analise
            elif j == 0: # se o termo corresponde ao indice e controle ainda é zero
                c = c + 1 # contador soma 1, e assim se pula para o proximo indice para analise
                j = j + 1# e o controle eh acionado para nos informamos que ha um numero
            elif j == 1: #se o controle corresponde a um, significa que o termo já existe na lista, deve se excluir
                k = c + 1# montamos uma incognita que aumente o indice em um
                E = E[:c] + E[k:]#E assim excluimos o elemente repetido
    print(E)

##cond_de(L_1)          #Teste da funcao cond_de
##cond_de(L_2)          #

def uniao_de(L1,L2):
    UNIAO = L1[:] + L2[:] # uniao simplesmente pega essas duas listas e contatena
    cond_de(UNIAO)

##uniao_de(L_1,L_2)     #Teste da funcao uniao_de

def inter_de(L1,L2):
    G1 = L1[:] # criamos uma copia da lista 1
    G2 = L2[:] # criamos uma copia para a lista 2
    Inter = [] # criamos uma lista vazia
    for termos_G in G1: # varremos os elementos da lista 1
        c = 0 # contador
        while c < len(G2): # enquanto c eh menor que a segunda lista
            if termos_G == G2[c]: #se o termo corresponde ao item
                Inter = Inter[:] + [termos_G] # adiciona o item na lista vazia
                c = c + 1 # pula para o proximo indice
            else:
                c = c + 1 # pula para o proximo indice
    cond_de(Inter)

##inter_de(L_1,L_2)     #Teste da funcao inter_de

L_1 = input("Digite um valor para sua lista 1 ou digite fim\n")
L1 = []
while L_1 != "fim":
    L1 += [L_1]
    L_1 = input("Digite um valor para sua lista 1 ou digite fim\n")

L_2 = input("Agora digite um valor para sua lista 2 ou digite fim\n")
L2 = []
while L_2 != "fim":
    L2 += [L_2]
    L_2 = input("Digite um valor para sua lista 1 ou digite fim\n")
    
print("\n A uniao e a intersecao respectivamente sao:\n")
      
uniao_de(L1,L2)
inter_de(L1,L2)

        
