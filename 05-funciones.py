import os 

def funcion1():
    num1= int(input("numero1: "))
    num2= int(input("numero2: "))
    res= num1 + num2
    print(f"la suma de {num1} y {num2} es {res}")


def funcion2():
    num1= int(input("numero 1: "))
    num2= int(input("numero 2: "))
    res=num1 - num2
    print(f"la resta de {num1} y {num2} es {res}")

def  funcion3():
    num1= int(input("numero1: "))
    num2= int(input("numero2: "))
    res=num1 * num2
    print(f"la Multiplicacion de {num1} y {num2} es {res}")

def funcion4():
    num1= int(input("numero1: "))
    num2= int(input("numero2: "))
    res=num1 / num2
    print(f"la Division de {num1} y {num2} es {res}")

def run():
    op=0
    while op != 5:
        print("1. suma")
        print("2. Resta")
        print("3. Multiplicacion")
        print("4. Division")
        print("5. Salir")

        op=int(input("ingrese una opcion: "))

        if op==1:
            funcion1()
        elif op==2:
            funcion2()
        elif op==3:
            funcion3()
        elif op==4:
            funcion4()
        elif op==5:
            print("adios")
        else:
            print("opcion invalida")
        
    





if __name__ == "__main__":
    run()