#PARTE4

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

def RESOLVE(F,theta_graus,m,g,mu):
    Fy_re = Fy(F,theta_graus)
    P_re = P(m,g)
    N_re = N(P_re,Fy_re)

    if (N_re > 0):
        fat_re = fat(mu,N_re)
    else:
        N_re=0
        fat_re = 0
    return fat_re, N_re, P_re, Fy_re

RESPOSTA=RESOLVE(F=50,theta_graus=30,m=5,g=10,mu=0.2)
print("A reposta final é: fat = ",RESPOSTA[0],"Com os seguintes resultados intermediários: N=",RESPOSTA[1],"P=",RESPOSTA[2],"Fy=",RESPOSTA[3])


RESPOSTA=RESOLVE(F=100,theta_graus=30,m=5,g=10,mu=0.2)
print("A reposta final é: fat = ",RESPOSTA[0],"Com os seguintes resultados intermediários: N=",RESPOSTA[1],"P=",RESPOSTA[2],"Fy=",RESPOSTA[3])

RESPOSTA=RESOLVE(F=100,theta_graus=45,m=5,g=10,mu=0.2)
print("A reposta final é: fat = ",RESPOSTA[0],"Com os seguintes resultados intermediários: N=",RESPOSTA[1],"P=",RESPOSTA[2],"Fy=",RESPOSTA[3])

RESPOSTA=RESOLVE(F=150,theta_graus=45,m=5,g=10,mu=0.2)
print("A reposta final é: fat = ",RESPOSTA[0],"Com os seguintes resultados intermediários: N=",RESPOSTA[1],"P=",RESPOSTA[2],"Fy=",RESPOSTA[3])

# OS BLOCOS IF estão filtrando os resultados que fazem o bloco ser levantado e fixando que nesses caso a normal e a fat recebem valor zero pois deixam de existir

# os blocos IF e os blocos FOR são o coralção da programação, veja na aula 5 o que os FOR podem fazer
