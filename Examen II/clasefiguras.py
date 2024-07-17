import os
import math

# Clase Figura

class Figura:
    def area(self):
        radio=float(input("Ingrese el radio de la figura: "))
        area = (2 * 3.14 * radio)
        print("El área del circulo es: ", area)

        area = (4 * 3.14 * (radio * radio))
        print("El área de la esfera es: ", area)

        exit()

    def volumen(self):
        radio=float(input("Ingrese el radio de la figura: "))

        volumen = (4 * 3.14 * (radio * radio * radio)) / 3

        print("El volumen de la esfera es: ", volumen)

        exit()














