#aula 6

# tem uma coisa chamada "call back" significa, ao p� da letra, "me liga"

# como contexto suponha que queiramos comparar por exemplo os pre�os de alguns projetos com custo fixo e vari�vel

#queremos pintar uma cerca

#para contratar a empresa A, ela cobra 50 reais de entrada e mais 1 real por metro de cerca
#ent�o 9o custo que teremos com a empresa A � fun��o do perimetro de cerca que queremos da seguinte forma

def custoA(p):
    return 50 + 1*p #50 reais de entrada mais um rela para cada metro de perimetro contrastado
    
#suponha agora uma empresa B que n�o cobra entrada nenhuma, mas que cobra 1.25 por cada metro de perimetro    

def custoB(p):
    return 1.25*p #50 reais de entrada mais um rela para cada metro de perimetro contrastado    
    
    
#qual � a empresa que vai me prestar o servi�o mais barato????
#issoisso vai depender do tamanho do servi�o!
    
# vamos escrever uma fun��o que fa�a essa compara��o por n�s

# por exemplo a sdeguinte fun��o:

def COMPARA(f,g,x):
            # esse f e esse g s�o as fun��es call back, pois veja mais abaixo como a fun��o COMPARA vai "ligar" para as fun��es f e g usando o valor x em quest�o como argumento REAL para o argumento DE SUBSTITUI�O
    if (f(x) == g(x)):
        #pega aqui a fun��o f fornecida
        #o valor x fornecido
        #e calcula o valor que f assume para esse x em quest�o
        print( "TANTO FAZ", "f e g tem o mesmo valor, igual a", f(x), " em x igual a ", x )
        return "TANTO FAZ"
    elif (f(x) > g(x)): #elif � abrivia��o para "else if" quer duizer, sen�o atender o crit�rio acima, veja se atende ao crit�rio aqui � esquerda
        print( "CONTRATE B", "em x igual a ", x, "f tem valor", f(x), "e g", g(x), "logo f maior que g nesse ponto x" )
        return "CONTRATE B"
    else: #e por fim o else, como antes "se n�o" atender nenhum dos crit�rios acima
        print( "CONTRATE A"," em x igual a ", x, "f tem valor", f(x), "e g", g(x), "logo f menor que g nesse ponto x"    )
        return "CONTRATE A"    
        
#essa fun��o espera como argumento numeros 1 e 2 duas FUN��ES de uma vari�vel "x"
# e como terceiro um valor de variavel x

#suponha que queiramos 10 metros de cerca:

RESPOSTA=COMPARA(f=custoA, g=custoB, x=10)
#assim n�s chamamos um fun��o que n�o fornce um valor de reposta

#VAMOS TESTAR COM OUTRAS METRAGENS

RESPOSTA=COMPARA(f=custoA, g=custoB, x=1)

RESPOSTA=COMPARA(f=custoA, g=custoB, x=50)

RESPOSTA=COMPARA(f=custoA, g=custoB, x=100)

RESPOSTA=COMPARA(f=custoA, g=custoB, x=1000)

RESPOSTA=COMPARA(f=custoA, g=custoB, x=10000)

#OLHANDO OS RESULTADOS � POSS�VEL concluir que a empresa A � a especializada em servi�os grandes, ela fica mais em conta para os trabalhos de 1000 e 10000 metros
#enquyanto q a empresa B � a mais em contan para os servi�os pequenso de 1,10, 50 e 100 metros

