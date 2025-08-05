"""
Programa: RK4.py
Propósito:
    Programar el método de Runge-Kutta (RK4) y comprobar su funcionamiento
    con alguno de los casos del ejemplo 2.2 de la hoja de Ejemplos 4.

    Ejemplo utilizado: dy/dx = x*y^2 - y/x
Fecha: 03/12/2022
Autor: Adrián Losada Álvarez 
"""


#Definimos la EDO:
def EDO(x,y):
    return (x*y**2 - y/x)   # <- Introducir EDO

#Método Runge-Kutta (RK4):
def RK4(x0, y0, x_aprox, h):
	n = (int)((x_aprox - x0)/h) #Calculamos el número de iteraciones con el tamaño de salto dado
	y = y0  #Valor inicial

    #Calculamos la aproximación con los datos dados:
	for i in range(1, n + 1):
		k1 = h * EDO(x0, y)
		k2 = h * EDO(x0 + 0.5 * h, y + 0.5 * k1)
		k3 = h * EDO(x0 + 0.5 * h, y + 0.5 * k2)
		k4 = h * EDO(x0 + h, y + k3)

		#Actualizamos el siguiente valor de x e y:
		y = y + (1.0 / 6.0)*(k1 + 2 * k2 + 2 * k3 + k4)
		x0 = x0 + h

    #Mostramos el resultado:
	print("h =",h,"; y(%0.1f)=%0.4f"%(x_aprox, y))


#Valores iniciales:
x0 = 1
y0 = 1

#Valor a aproximar
x_aprox = 1.5

#Tamaño de salto
h = 0.1

#Llamamos a la función para obtener la aproximación
RK4(x0, y0, x_aprox, h)