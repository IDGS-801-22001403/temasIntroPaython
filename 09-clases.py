class Operadores:
    # Declaración de propiedades
    # pública
    num1 = 0
    # protegida
    _num2 = 0
    # privada
    __res = 0

    # Declaración del constructor
    def __init__(self, num1, num2):  # Doble guion bajo para el constructor
        self.num1 = num1
        self._num2 = num2

    # Declaración de los métodos
    def suma(self):
        self.__res = self.num1 + self._num2  # Suma correctamente
        print("La suma es: {}".format(self.__res))

    def resta(self):
        self.__res = self.num1 - self._num2  # Resta correctamente
        print("La resta es: {}".format(self.__res))


# Función principal
def main():
    obj = Operadores(3, 4)  
    obj.suma()              
    obj.resta()             


if __name__ == "__main__":
    main()
