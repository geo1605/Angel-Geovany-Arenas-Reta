import random
import math
puntos = 10000
cuantosS = 0
random.random()
for i in range(puntos):
    x = random.random()
    y = random.random()
    yc = math.sqrt(1-x*x)
    if y > yc:
        None
    else:
        cuantosS +=1
cuarto = float(cuantosS) / float(puntos)
print (cuarto)
pi = cuarto*4
print(pi)
