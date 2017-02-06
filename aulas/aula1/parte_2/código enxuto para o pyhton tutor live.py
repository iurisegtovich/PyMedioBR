# então vamos definir uma função usando a sintaxe a seguir:
def fat(mu,N):
#   #     ####-> os dois pontos dizem que as intruções dessa função começam a seguir
#   #     ###-> o que está entre parenteses é chamado "lista de argumentos de substituição (dummy arguments em inglÊs)" e são as coisas das quais essa função depende e que devem mudar dependendo dos dados do problema
#   #     ##-> aqui o calculo de fat depende de um mu e de um N dados
#   #     #-> separar as coisas por vírgula
#   #-> esse é o nome da função que calcula fat
#-> essa é a palavra chave para definir funções
    return mu*N
#   #      #-> o resultado dessa conta é o que a função "devolve quando tentarmos usá-la
#   #-> essa é a palavra chave para retornar o valor calculado
#-> tem q ter um espaço aqui antes do return do tamanho de 1 TAB, isso se chama "identação" e diz o que faz parte da função e o que já não faz mais parte
# daqui para baixo não faz mais parte da função
# Note que apareceu na tabela global frame uma célula para a função fat e um setinha dizendo que fat não tem um valor, fat chama uma função que depende de mu e N sendo a princípio desconhecidos...

resposta_fat = fat(mu=0.2,N=25)

print(resposta_fat)

def N(P,Fy):
    return P-Fy
    
def P(m,g):
    return m*g
    
def Fy(F,theta_graus):
    import math
    fator_de_conversao_grau_para_rad = ( 2*math.pi / 360 ) #um círculo inteiro tem 360 graus, equivalente a 2pi radianos, então o fator de conversão de graus para radianos é esse aqui
    theta_rad = theta_graus * fator_de_conversao_grau_para_rad

    return F*math.sin(theta_rad)     

F_dado = 50 #escrevemos F_dado para não nos confundirmos sobre qual variável corresponde ao valor dado no caso atual, enquanto o F na função vai receber o valor de qualquer variação de problema apenas na hora em que chamarmos a função
theta_dado=30

Fy_calc = Fy(F=F_dado,theta_graus=theta_dado)

m_dado=5
g_Terra=10
P_calc=P(m=m_dado,g=g_Terra)
N_calc=N(P=P_calc,Fy=Fy_calc)
mu_dado=0.2

resposta_fat=fat(mu=mu_dado,N=N_calc)

def RESOLVE(F,theta_graus,m,g,mu):
    Fy_re = Fy(F,theta_graus) #vamos identificar nossa respostas intermediárias com _re para poder dar uma resposta compelta    
    P_re = P(m,g)
    N_re = N(P_re,Fy_re)
    fat_re = fat(mu,N_re)
    return fat_re, N_re, P_re, Fy_re #a respota dessa função vai se rum "lista" com todas as respostas intermediárias

RESPOSTA=RESOLVE(F=50,theta_graus=30,m=5,g=10,mu=0.2)