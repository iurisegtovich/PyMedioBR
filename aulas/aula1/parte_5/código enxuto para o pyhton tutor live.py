#PARTE5

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

    if (N_re > 1e-9 ): #vamos trocar aquele zero aqui por uma valor de tolerancia: qualquer coisa menor que 1e-9 vai ser zero para a gente 
        fat_re = fat(mu,N_re)
    else:
    
        N_re=0
        fat_re = 0
    return fat_re, N_re, P_re, Fy_re


# o FOR permite fazer uma coisa "análoga" várias vezes variando um detalhe ou outro

for theta_tentativa in [0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90]:
    RESPOSTA=RESOLVE(F=100,theta_graus=theta_tentativa,m=5,g=10,mu=0.2)
    print("para o angulo",theta_tentativa,"a Normal dá",RESPOSTA[1])
    
for theta_tentativa in [25,25.5,26,26.5,27,27.5,28,28.5,29,29.5,30]:
    RESPOSTA=RESOLVE(F=100,theta_graus=theta_tentativa,m=5,g=10,mu=0.2)
    print("para o angulo",theta_tentativa,"a Normal dá",RESPOSTA[1])