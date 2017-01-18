# PyMédioBR - Aula 1 - parte_1 - CÓDIGO PURO PARA PYTHON-TUTOR-LIVE
# Você deve estar lendo esse código no site http://www.pythontutor.com/live.html#mode=edit para conseguir ver a tabela "global frame" que ilusrtra graficamente tudo q iremos apredender sobre variáveis, valores e funções
# Este código deve se restringir a menos de 80(?) linhas aproximadamente, devido a um limite no serviço do site

# Qualquer coisa escrita depois de um "jogo da velha" (hashtag) é chamado "comentário" - não influencia na execução do código

m = 5 # a massa: o valor (value) "5" é atribuído à variável "m"
F = 50 # a força que puxa o bloco
mu = 0.2 # o coeficiente de atrito
theta = 30 # o ângulo (em graus)
sen30 = 1/2 # seno de 30 gruas

Fy = F * sen30 # o valor atual da a variavel sen30 é multiplicado ( * é o operador da multiplicação) pelo valor atual da variável F e o resultado é atribuído à nova variável Fy

g = 10

P = m * g

N = P - Fy #subtração

fat = mu * N

print("A força de atrito calculada foi de ",fat,"N") # impressão da resposta completa no campo "Print output" do site
