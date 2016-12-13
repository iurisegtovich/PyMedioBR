# PyMédioBR - Aula 1 - parte_1 - CÓDIGO COMENTADO

# Você deve estar lendo esse código comentado no site github
# mas ao mesmo tempo acompanhando o código puro
# no site http://www.pythontutor.com/live.html#mode=edit
# para conseguir ver a tabela "global frame" que ilusrtra graficamente tudo q iremos apredender sobre variáveis, valores e funções

# Cada parte da aula 1 deve se restringir a um limite de linhas/caracteres de acordo com o serviço do site

# === programando em python ===========================================================================================================

# --- cometários ------------------------------------------------------------------------------------------------------------------------------------

# Qualquer coisa escrita depois de um "jogo da velha" (hashtag) é chamado "comentário". Comentários servem para explicar o que cada pedaço de seu programa faz, eles não inlfuenciam na execução do código

# Contexto dessa aula: Resolver um problema de sobre superficie plana com atrito
# Enunciado: # Vamos supor que temos um bloco de massa m = 5 kg sobre uma superfície plana. Suponhamos que o coeficiente de atrito entre o bloco e a superfície plana seja igual a 0,2, determine o valor da força de atrito para uma força que puxa o bloco com intensidade igual a 50 N ( ver desenho no site: http://exercicios.brasilescola.uol.com.br/exercicios-fisica/exercicios-sobre-plano-inclinado-com-atrito.htm )
# Solução: "Primeiramente devemos retirar os dados do problema"
# Segundo o enunciado, "temos um bloco de massa m = 5 kg", podemos traduzir esse dado em linguagem de programação da forma apresentada na linha de código a seguir:

# --- attribuição (assignment) ------------------------------------------------------------------------------------------------------

m = 5 # Leia essa linha da seguinte forma: o valor (value) "5" é atribuído à variável "m"
# # #-> o valor "5"
# #-> é atribuído (assignment) segundo o operador "="
#-> à variável (variable) "m" aqui declarada.
# Note que na tabela 'global frame' à direita aparece uma linha escrito o nome da variável que declaramos - "m" - e ao lado o valor que atribuimos à ela - "5"
# Da mesma forma retiramos os outros dados do problema:
# "...uma força que puxa o bloco com intensidade igual a 50 N"
F = 50 # a força que puxa o bloco
# note uma nova linha na tabela global frame
# "Suponhamos que o coeficiente de atrito entre o bloco e a superfície plana seja igual a 0,2"
# "μ=0,2" podemos usar letras gregas aqui nos comentários, mas na hora do código só valem as letras (a-z), minusculas e maiusculas (aA-zZ) - que geram variáveis DIFERENTES -, números (0-9) - menos usá-los como primeiro caractere -, e o símbolo "sublinhado" (_)
mu = 0.2 # o coeficiente de atrito
# note aqui que o separador de casas decimal é o ponto, como é o caso na lingua inglesa
# note uma nova linha na tabela global frame
# "veja o angulo de 30 grauis no desenho"
theta = 30 # o ângulo (em graus)
# note uma nova linha na tabela global frame
# "Como sabemos que a força faz um ângulo de 30° com a horizontal, devemos decompor a força na direção y (Fy = F.sen30°), pois a força de atrito depende da normal e do coeficiente de atrito, assim temos:"
# Fy = F x sen30
# sabemos q a componente Fy depende da força F e do seno do angulo theta
# como 30 graus é um angulo notável, devemos saber que seno de 30 graus é 1/2

# --- operadores (operators) ---------------------------------------------------------------------------------------------------------------------------------------------

sen30 = 1/2 # em 1/2, / é o operador de divisão, 
# note uma nova linha na tabela global frame
# podemos agora finalmente efetuar o cálcula da componente Fy
Fy = F * sen30
#  # # # #-> o valor atual da a variavel sen30
#  # # #-> é multiplicado ( * é o operador da multiplicação)
#  # #-> pelo valor atual da variável F
#  #-> o resultado é atribuído
#-> à nova variável Fy
# note uma linha nova na tabela
#podemos seguir com o cálculo da força normal pela seguinte fórmula:
#N = P - Fy
#sabemos que ela depende da força peso, que é calculada pela seguinte fórmula
# P = m*g
# log precisamos declarar uma variável para a aceleração da gravidade e atribuir a ela uma valor
g = 10
# note mais uma linha na tabela
# podemos então seguir com as equações anteriores agora que terminamos de entender as dependencias
P = m * g
# note uma nova linha na tabela
# seguimos para o cálculo de N
N = P - Fy
# note uma nova linha na tabela
# finalmente é possível calcular a força de atrito
# fat = μ x N
fat = mu * N
# com isso terminamos de resolver o problem, usando o python como se fosse uma calculadora para realizar as multiplicações e guardar os valores de todas as variáveis envolvidas nos cálculos na tablea "global frame"
# por fim, podemos "imprimir" a reposta final, pois a tabela Global frame só é visível no site http://www.pythontutor.com/live.html#mode=edit
# enquanto que "imprimir" usando o comando "print" vai exibir o resultado num local apropriado da tela, qualquer que seja o computador, site, ou programa de desenvolvimento que você esteja usando para programar.

# --- impressão (print) ----------------------------------------------------------------------------------------------------------------

print("A força de atrito calculada foi de ",fat,"N")  # impressão da resposta completa no campo "Print output" do site
#    ##                                     #  #  ##-> tudo que está entre parenteses será "impresso" na tela
#    ##                                     #  #  #-> tudo que está entre aspas será impresso como texto
#    ##                                     #  #-> as vírgulas separam cada coisa de tipo diferente que será impressa
#    ##                                     #-> aqui fazer a impressão da variável fat significa imprimir o valor atual que ela possuir
#-> o comando print

# === e agora? ===================================================================================================================

#e se quisermos resolver com uma força F diferente?
# e se quisermos resolver com um angulo diferente?
#vejam a parte 2 do curso!
