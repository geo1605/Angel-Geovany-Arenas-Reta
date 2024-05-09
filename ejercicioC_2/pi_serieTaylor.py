acumulador = 0.0
div_act = 1.0
cont = 0
suma = True
while div_act > 0.0000000052:
    cont +=1
    div_act = 1/cont
    if cont % 2 != 0:
        if suma:
            acumulador += div_act
        else:
            acumulador -= div_act
        suma = not suma
    
print(acumulador)
pi = acumulador*4
print(pi)