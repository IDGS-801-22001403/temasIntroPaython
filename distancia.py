import math

class PuntosDistancia:
    def __init__(self):
        self.punto1_x = 0
        self.punto1_y = 0
        self.punto2_x = 0
        self.punto2_y = 0

    def ingresar_coordenadas(self):
        self.punto1_x = int(input("Inserta la coordenada X del primer punto: "))
        self.punto1_y = int(input("Inserta la coordenada Y del primer punto: "))
        self.punto2_x = int(input("Inserta la coordenada X del segundo punto: "))
        self.punto2_y = int(input("Inserta la coordenada Y del segundo punto: "))

    def calcular_distancia(self):
        distancia = math.sqrt(((self.punto2_x - self.punto1_x) ** 2) + ((self.punto2_y - self.punto1_y) ** 2))
        print(f'La distancia entre los puntos es: {distancia:.2f}')

def main():
    calculador = PuntosDistancia()  
    calculador.ingresar_coordenadas()  
    calculador.calcular_distancia()  

if __name__ == '__main__':
    main()
