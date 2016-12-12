# tendo visto a parte 1
# o que fazer se:
# quisermos resolver com uma força F diferente?
# quisermos resolver com um angulo diferente?
# para isso existem as "funções" na programação
# vamos pegar cada equação utilizada e em vez de calcular elas coms os dados do problema vamos definir funções que vão funcionar para esse desenho com quaisquer variações nos dados.
# podemos começar pelo objetivo, calcular a força de atrito:
#lembrem:
# fat = μ x N
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

#exemplo de usar a função
#lembrando da resposta na aula1, o valor de mu foi dado como 0,2 e o de N foi calculado como 25 N
#então essa função deve retornar a força de atrito q era a resposta da questão se fornecermos a ela esses valores
#AGORA muita atenção ao que acontece na tabela conforme você apertar o botão Forward e passar pela linha a seguir
#até agora cada clique em forward andava uma linha no codigo
#agora como nós vamos chamar a função, nós vamos ver um pulo no código lá para dentro da função, fazer as contas l, e depois voltar aqui!
resposta_fat = fat(mu=0.2,N=25)
#            # # aqui "chamamos" a função usando como argumentos REAIS (actual arguments em inlgÊs) os valores de 0.2 e 25 no lugar dos argumentos de substituição mu e N respectivamente
#            # atribuimos o resultado
# à variavel resposta_fat
#podemos ver o valor de reposta na tabela global frame (no site) e podemos usar a função de imprimir
print(resposta_fat)
#seguindo o mesmo raciocínio, vamos transformar todas as "equações" envolvidas nesse problema em "funções" de programação

def N(P,Fy):
    return P-Fy
    
def P(m,g):
    return m*g
    
def Fy(F,theta_graus):
         #-> aqui escrevemos que é em grau para não confundirmos!
    import math
    #      #-> esse é o pacote de matemática (math em inglês) básica do python, precisamos dele para fazer contas com seno de qualquer ângulo que não seja notável
    #-> essa é palavra chave para importar pacotes extra para nos auxiliar
    fator_de_conversao_grau_para_rad = ( 2*math.pi / 360 ) #um círculo inteiro tem 360 graus, equivalente a 2pi radianos, então o fator de conversão de graus para radianos é esse aqui
    theta_rad = theta_graus * fator_de_conversao_grau_para_rad
    #-> essa variável guarda o valor dos angulos convertido para radianos
    return F*math.sin(theta_rad)     
             #        #-> essa função trabalha com angulos em radianos!! por isso precisamos fazer a conversão acima
             # a função seno (sin em inglês) está disponível dentro do pacote math,. então usamos math.sin para chamar ela de lá
#agora que já escrevemos todas as funções podemos testá-las resolvendo o mesmo problema de novo, e depois podemos resolver qualquer variação 

F_dado = 50 #escrevemos F_dado para não nos confundirmos sobre qual variável corresponde ao valor dado no caso atual, enquanto o F na função vai receber o valor de qualquer variação de problema apenas na hora em que chamarmos a função
theta_dado=30

Fy_calc = Fy(F=F_dado,theta_graus=theta_dado)
#note aqui a distinção entre F e F_dado
# a leitura do que essa linha faz é mais ou menos assim:
#à variável Fy_calc, atribuímos(=) o valor calculado pela função Fy, na caso em q a variavel F da qual essa função depende assume o valor de F_dado, e a variável theta assum o valor de theta_dado
#CONTINUANDO...
m_dado=5
g_Terra=10
P_calc=P(m=m_dado,g=g_Terra)
N_calc=N(P=P_calc,Fy=Fy_calc)
mu_dado=0.2
#vamos fazer a conta para resposta_fat DE NOVO agora que já seguimos toda a lógica das funções:
resposta_fat=fat(mu=mu_dado,N=N_calc)
#Vamos fazer uma função única para resolver o problema de uma vez?
#vamos lembrar de todas as dependencias e colocar ela na lista de argumentos da função
def RESOLVE(F,theta_graus,m,g,mu):
    Fy_re = Fy(F,theta_graus) #vamos identificar nossa respostas intermediárias com _re para poder dar uma resposta compelta    
    P_re = P(m,g)
    N_re = N(P_re,Fy_re)
    fat_re = fat(mu,N_re)
    return fat_re, N_re, P_re, Fy_re #a respota dessa função vai se rum "lista" com todas as respostas intermediárias
#testar
RESPOSTA=RESOLVE(F=50,theta_graus=30,m=5,g=10,mu=0.2)