import math
from io import open

class cinepolis:
    def __init__(self):
        self.compras = []
    
    def total_compra(self,cantidad_boletos, usar_tarjeta):
        precio = 12000
        total = cantidad_boletos * precio
        if cantidad_boletos > 5:
            total *= 0.85
        elif 3<= cantidad_boletos <= 5:
            total *= 0.90
        if usar_tarjeta:
            total *= 0.90
        return total
    
    def comprar(self):
        print('---Nueva Compra---')
        num_personas = int(input('Ingrese la cantidad de personas: '))
        nombres = []

        for i in range (num_personas):
            nombre = input(f'Ingrese el nombre de la persona {i+1}: ')
            nombres.append(nombre)
        
        while True:
            cantidad_boletos = int(input('Ingrese la cantidad de boletos a comprar (maximo 7 por persona): '))
            if cantidad_boletos > 7 * num_personas:
                print(f'No pueden comprar mas de {7 * num_personas} boletos.')
                cambiar = input('Quieres cambiar algun dato? (s/n): ').strip().lower()
                if cambiar == 's':
                    menu='''\n
                    Que deseas cambiar?
                    1. Cantidad de personas
                    2. Cantidad de boletos
                    3. Cancelar compra  
                    4. Continuar con la compra actual
                    '''
                    print(menu)
                    opcion = input('Que opcion deseas? ').strip().lower()
                    if opcion == '1':
                        num_personas = int(input('Cuantas personas son: '))
                        nombres = []
                        for i in range (num_personas):
                            nombre = input(f'Ingrese el nombre de la persona {i+1}: ')
                            nombres.append(nombre)
                        cantidad_boletos = int(input('Ingrese la cantidad de boletos a comprar (maximo 7 por persona): '))
                    elif opcion == '2':
                        cantidad_boletos = int(input('Ingrese la cantidad de boletos a comprar (maximo 7 por persona): '))
                    elif opcion == '3':
                        print('Compra cancelada')
                        return self.menu()
                    elif opcion == '4':
                        break
                    else:
                        continue
            usa_tarjeta = input('Pagaras con Tarjeta Cineco?' ).strip().lower() == 's'
            total = self.total_compra(cantidad_boletos, usa_tarjeta)
            print(f'El total es: ${total:.2f}')
            self.compras.append((nombres, cantidad_boletos, total))
            break

    def mostrar_compras(self):
        print('\n---Historial---')
        for compra in self.compras:
            nombre, cantidad_boletos, total = compra
            print(f'Nombre: {nombre}, Cantidad de boletos: {cantidad_boletos}, Total: ${total:.2f}')

    
    def guardar_compras(self):
        with open('compras.txt', 'w') as archivo:
            for compra in self.compras:
                nombre, cantidad_boletos, total = compra
                archivo.write(f'Nombre: {nombre}, Cantidad de boletos: {cantidad_boletos} Total: ${total:.2f}\n')
                print('Compras guardadas')




    def menu(self):
        menu= '''
        ---Cinepolis---
        1. Comprar boletos
        2. Mostrar Historial
        3. Salir y guardar compras
        '''
        while True:
            print(menu)

            opcion = int(input('Seleccione una opcion'))

            if opcion == 1:
                self.comprar()
            elif opcion == 2:
                self.mostrar_compras()
            elif opcion == 3:
                self.guardar_compras()
                print('Gracias por usar Cinepolis')
                break
            else:
                print('Opcion no valida')

if __name__ == "__main__":
    cinepolis=cinepolis()
    cinepolis.menu()

    

