#aula 6

def custoA(p):
    return 50 + 1*p #50 reais de entrada mais um rela para cada metro de perimetro contrastado

def custoB(p):
    return 1.25*p #50 reais de entrada mais um rela para cada metro de perimetro contrastado    

def COMPARA(f,g,x):
    if (f(x) == g(x)):
        print( "TANTO FAZ", "f e g tem o mesmo valor, igual a", f(x), " em x igual a ", x )
        return "TANTO FAZ"
    elif (f(x) > g(x)): #elif é abriviação para "else if" quer duizer, senão atender o critério acima, veja se atende ao critério aqui à esquerda
        print( "CONTRATE B", "em x igual a ", x, "f tem valor", f(x), "e g", g(x), "logo f maior que g nesse ponto x" )
        return "CONTRATE B"
    else: #e por fim o else, como antes "se não" atender nenhum dos critérios acima
        print( "CONTRATE A"," em x igual a ", x, "f tem valor", f(x), "e g", g(x), "logo f menor que g nesse ponto x"    )
        return "CONTRATE A"    

RESPOSTA=COMPARA(f=custoA, g=custoB, x=10)

RESPOSTA=COMPARA(f=custoA, g=custoB, x=1)

RESPOSTA=COMPARA(f=custoA, g=custoB, x=50)

RESPOSTA=COMPARA(f=custoA, g=custoB, x=100)

RESPOSTA=COMPARA(f=custoA, g=custoB, x=1000)

RESPOSTA=COMPARA(f=custoA, g=custoB, x=10000)