from funciones import cRect, cCir, cCuad

print("hola que quieres calcular?")
print("1. circulo")
print("2. cuadrado")
print("3. rectangulo")
o = int(input("elije: "))
if o == 1:
    r = float(input("coloca el radio:"))
    result = cCir(r)
    print(result)
if o == 2:
    r = float(input("coloca el lado:"))
    result = cCuad(r)
    print(result)
if o == 3:
    b = float(input("coloca base:"))
    a = float(input("coloca altura"))
    result = cRect(a,b)
    print(result)
