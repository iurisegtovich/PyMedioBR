#aula 6

# tem uma coisa chamada "call back" significa, ao pé da letra, "me liga"

# como contexto suponha que queiramos comparar por exemplo os preços de alguns projetos com custo fixo e variável

#queremos pintar uma cerca

#para contratar a empresa A, ela cobra 50 reais de entrada e mais 1 real por metro de cerca
#então 9o custo que teremos com a empresa A é função do perimetro de cerca que queremos da seguinte forma

def custoA(p):
    return 50 + 1*p #50 reais de entrada mais um rela para cada metro de perimetro contrastado
    
#suponha agora uma empresa B que não cobra entrada nenhuma, mas que cobra 1.25 por cada metro de perimetro    

def custoB(p):
    return 1.25*p #50 reais de entrada mais um rela para cada metro de perimetro contrastado    
    
    
#qual é a empresa que vai me prestar o serviço mais barato????
#issoisso vai depender do tamanho do serviço!
    
# vamos escrever uma função que faça essa comparação por nós

# por exemplo a sdeguinte função:

def COMPARA(f,g,x):
            # esse f e esse g são as funções call back, pois veja mais abaixo como a função COMPARA vai "ligar" para as funções f e g usando o valor x em questão como argumento REAL para o argumento DE SUBSTITUIÃO
    if (f(x) == g(x)):
        #pega aqui a função f fornecida
        #o valor x fornecido
        #e calcula o valor que f assume para esse x em questão
        print( "TANTO FAZ", "f e g tem o mesmo valor, igual a", f(x), " em x igual a ", x )
        return "TANTO FAZ"
    elif (f(x) > g(x)): #elif é abriviação para "else if" quer duizer, senão atender o critério acima, veja se atende ao critério aqui à esquerda
        print( "CONTRATE B", "em x igual a ", x, "f tem valor", f(x), "e g", g(x), "logo f maior que g nesse ponto x" )
        return "CONTRATE B"
    else: #e por fim o else, como antes "se não" atender nenhum dos critérios acima
        print( "CONTRATE A"," em x igual a ", x, "f tem valor", f(x), "e g", g(x), "logo f menor que g nesse ponto x"    )
        return "CONTRATE A"    
        
#essa função espera como argumento numeros 1 e 2 duas FUNÇÕES de uma variável "x"
# e como terceiro um valor de variavel x

#suponha que queiramos 10 metros de cerca:

RESPOSTA=COMPARA(f=custoA, g=custoB, x=10)
#assim nós chamamos um função que não fornce um valor de reposta

#VAMOS TESTAR COM OUTRAS METRAGENS

RESPOSTA=COMPARA(f=custoA, g=custoB, x=1)

RESPOSTA=COMPARA(f=custoA, g=custoB, x=50)

RESPOSTA=COMPARA(f=custoA, g=custoB, x=100)

RESPOSTA=COMPARA(f=custoA, g=custoB, x=1000)

RESPOSTA=COMPARA(f=custoA, g=custoB, x=10000)

#OLHANDO OS RESULTADOS É POSSÍVEL concluir que a empresa A é a especializada em serviços grandes, ela fica mais em conta para os trabalhos de 1000 e 10000 metros
#enquyanto q a empresa B é a mais em contan para os serviços pequenso de 1,10, 50 e 100 metros

