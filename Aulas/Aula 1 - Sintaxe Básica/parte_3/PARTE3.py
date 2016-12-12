#PARTE3

#repetindo aqui as funções porque vamos usar elas mas as aulas não podem ficar grandes demais senão não roda no site : (
def fat(mu,N):
    return mu*N
def N(P,Fy):
    return P-Fy
def P(m,g):
    return m*g
def Fy(F,theta_graus):
    import math
    theta_rad = theta_graus * ( 2*math.pi / 360 )
    return F*math.sin(theta_rad)     

#Agora Vamos fazer uma função única para resolver o problema de uma vez?
#vamos lembrar de todas as dependencias e colocar ela na lista de argumentos da função
def RESOLVE(F,theta_graus,m,g,mu):
    Fy_re = Fy(F,theta_graus) #vamos identificar nossa respostas intermediárias com _re para poder dar uma resposta completa (as respostas intermediáriuas sempre valem pontinhos na prova, não é mesmo ?)
    P_re = P(m,g)
    N_re = N(P_re,Fy_re)
    fat_re = fat(mu,N_re)
    return fat_re, N_re, P_re, Fy_re #a respota dessa função vai se rum "lista" com todas as respostas intermediárias
#testar
RESPOSTA=RESOLVE(F=50,theta_graus=30,m=5,g=10,mu=0.2)
#notem que a variável RESPOSTA tem uma setinha para uma lista amarela com vários valores
# esses são os valores das respostas intermediárias na ordem em que colocamos elas no "return"
#para imprimir cada um deles temos que usar colchetes e o indice que representa a ordem dele na lista, começcando do zero

print("A reposta final é: fat = ",RESPOSTA[0],"Com os seguintes resultados intermediários: N=",RESPOSTA[1],"P=",RESPOSTA[2],"Fy=",RESPOSTA[3])

#VAMOS MUDAR UM POUQINHO?

# É SÓ COPIAR A LINHA resposta=resolve... e mudar alguns valores
# e depois copiar a linha print("A resposta ..." Nessa não precisa mudar nada

#aí vai:
RESPOSTA=RESOLVE(F=100,theta_graus=30,m=5,g=10,mu=0.2)

#note aqui que os valores na lista mudam, a resposta é "sobre-escrita" "na memória" quando atribuuimos novos valores à ela, perdendo os valores antigos
#enquanto q na "tela de impressão" os valores que forem impressos não mudam mais

print("A reposta final é: fat = ",RESPOSTA[0],"Com os seguintes resultados intermediários: N=",RESPOSTA[1],"P=",RESPOSTA[2],"Fy=",RESPOSTA[3])

#note que aqui fat deu 1.4e-15, quer dizer 1,4 x 10^(-15)
#isso significa zero (experimente arredondar para 9 casas decimais: 0.000000000000014 vire 0.000000000), com erro de arredondamento dos cálculos no computador

# Pergunta1: O que houve?
RESPOSTA=RESOLVE(F=100,theta_graus=45,m=5,g=10,mu=0.2)
print("A reposta final é: fat = ",RESPOSTA[0],"Com os seguintes resultados intermediários: N=",RESPOSTA[1],"P=",RESPOSTA[2],"Fy=",RESPOSTA[3])

#note que aqui fat deu negativo

# Pergunta 2: o que houve?


RESPOSTA=RESOLVE(F=100,theta_graus=45,m=15,g=10,mu=0.2)
print("A reposta final é: fat = ",RESPOSTA[0],"Com os seguintes resultados intermediários: N=",RESPOSTA[1],"P=",RESPOSTA[2],"Fy=",RESPOSTA[3])

# aqui já temos uma resposta coerente de novo

# pergunta 3, por que?


#
#
#
#
#
#
#
#
#
#
#
#
#


# Resposta 1 : a componente Fy ficou igual ao peso, o objeto está em equilíbrio sem exercer pressão sobre o plano do plano, e não apenas arrastado

# Resposta 2 : a componente Fy está maior que o peso, o objeto está sendo levantado, não há mais contato então não há mais força normal
#Vamos ensinar o código a entende isso na aula 4 para que ele não escreve uma força normal negativa e perca pontos na prova.

# resposta 3, aumentando a massa do objeto, ele não está mais sendo levantado