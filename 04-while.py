x=0

while x<10:
    print(x)
    x=x+1
    pass

'''Operaciones de multiplicaciones de a x b utilizando sumas
    a=3
    b=4
    salida: 3+3+3+3=12
'''


a=int (input('ingresa el primer numero: '))
b=int (input('ingresa el segundo numero: '))
i=0
salida=0
while i<b:
    salida=salida+a
    i=i+1

print(f"el numero {a} x el numero {b}= {salida}")