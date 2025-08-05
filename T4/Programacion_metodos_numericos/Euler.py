"""
Programa: Euler.py
Propósito:
    Programar el método de Euler y comprobar su funcionamiento
    con alguno de los casos del ejemplo 1.1 de la hoja de Ejemplos 4.

    Ejemplo utilizado: dy/dx = x*y^2 - y/x
Fecha: 03/12/2022
Autor: Adrián Losada Álvarez 
"""


#Definimos la EDO:
def EDO(x,y):
    return (x*y**2 - y/x)   # <- Introducir EDO

#Método de Euler:
def Euler(x, y, x_aprox, h):
    #Calculamos la aproximación con los datos dados:
    while (x < x_aprox):
        y = y + h * EDO(x,y)
        x = x + h
 
    #Mostramos el resultado:
    print("h =",h,"; y(%0.1f)=%0.4f"%(x_aprox, y))


#Valores iniciales:
x0 = 1
y0 = 1

#Valor a aproximar
x_aprox = 1.5

#Tamaños de salto:
h1 = 0.1
h2 = 0.05

#Llamamos a la función para obtener las aproximaciones:
Euler(x0, y0, x_aprox, h1)
Euler(x0, y0, x_aprox, h2)