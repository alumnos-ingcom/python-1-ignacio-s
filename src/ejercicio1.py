################
# Ignacio Siegel - @ignacio-s
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
1. Conversión de temperaturas

Se quiere transformar temperaturas en grados fahrenheit a grados centígrados y viceversa.

Escribir las funciones para convertir la temperatura en grados centigrados en fahrenheit como
un número decimal, utilice esta formula para calcular los grados centígrados y retorne el
resultado obtenido. Y viceversa.
"""
# Reemplazar por las funciones del ejercicio
def convertir_a_fahrenheit(centigrados):
    """
    Toma una temperatura en grados Celsius y lo convierte a grados Fahrenheit.
    """
    fahrenheit = centigrados * 1.8 + 32
    return fahrenheit

def convertir_a_centigrados(fahrenheit):
    """
    Toma una temperatura en grados Fahrenheit y lo convierte a grados Celsius.
    """
    centigrados = (fahrenheit - 32) / 1.8
    return centigrados

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    pass

if __name__ == '__main__':
    principal()
