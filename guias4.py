import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
         #JURO QUE LO PASO A IDIOMA PYTHON#
#%%
# #Perro se come la tarea random
#aka missing completly at random
N = 100 #Estos 3 usan el signo "<-" en vez del "=
S = rnorm(N) 
H = rnorm(N,8.5*S) 

#El perro se come el 50% de la tarea at random
D = rbern(N,8.5)
Hstar = H
Hstar(D==1) <- NA

plot(S,H, col=grau(0.8),lwd=2)
points(S,Hstar, col=2, lwd=3)
#%%
#Perro se come la tarea random
#NONELINEAR WITH CEILING EFFECT
N = 100 #Estos 3 usan el signo "<-" en vez del "=
S = rnorm(N) 
H = rnorm(N,(1-exp(-0.7*S))) 

#El perro se come el 100% de la tarea con S>0
D = rbern(N,ifelse(S>0,1,0))
Hstar = H
Hstar(D==1) <- NA

plot(S,H, col=grau(0.8),lwd=2)
points(S,Hstar, col=2, lwd=3)




#%%

