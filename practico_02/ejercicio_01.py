# Implementar la clase Rectangulo que contiene una base y una altura, y el método area.


class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura


base = int(input("Ingrese la base"))
altura = int(input("Ingrese la altura"))

rectangulo1 = Rectangulo(base, altura)

print("La base es: ", rectangulo1.base)
print("La altura es: ", rectangulo1.altura)
print("El area es: ",rectangulo1.area())