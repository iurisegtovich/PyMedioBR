#PARTE3

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
    Fy_re = Fy(F,theta_graus) #vamos identificar nossa respostas intermediárias com _re para poder dar uma resposta completa (as respostas intermediáriuas sempre valem pontinhos na prova, não é mesmo ?)
    P_re = P(m,g)
    N_re = N(P_re,Fy_re)
    fat_re = fat(mu,N_re)
    return fat_re, N_re, P_re, Fy_re #a respota dessa função vai se rum "lista" com todas as respostas intermediárias

RESPOSTA=RESOLVE(F=50,theta_graus=30,m=5,g=10,mu=0.2)
