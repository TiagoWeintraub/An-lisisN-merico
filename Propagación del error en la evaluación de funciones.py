# La deflexión y de la punta de un mástil en un bote de vela es:
#     y = FL^4/8EI --> (a*b**4)/(8*c*d)
# Donde F = una carga lateral uniforme (lb/ft), L = altura (ft), E = el módulo de elasticidad
# (lb/ft^2), e I = el momento de inercia (ft^4). Estime el error en y, dados los siguientes datos:
# F = 50 lb/ft     ΔF = 2 lb/ft
# L = 30 ft        ΔL = 0.1 ft
# E = 1.5×10^8 lb/ft^2 = 150000000  ΔE = 0.01×10^8 lb/ft^2 = 1000000
# I = 0.06 ft^4    ΔI = 0.0006 ft^4

# Datos de nuestro ejercicio:
#     cant variables = 4
    
#     función:  y = (a*(b**4))/(8*c*d)
    
#     a = 50      Δa = 2 
#     b = 30      Δb = 0.1 
#     c = 150000000   Δc = 1000000 
#     d = 0.06        Δd = 0.0006 

from sympy import *

def Calculos_2_v(funcion):
    
    a, b = symbols(f'a b ', real=True)

    y = eval(funcion)

    dic = {}
    
    dic[a] = float(input('Ingrese el valor de la variable "a": '))
    dic[b] = float(input('Ingrese el valor de la variable "b": '))

    print(dic)
    
    parcial_simbolica_a = diff(y, a) #Derivada parcial respecto de a en formato str
    #print(diff(y, a))
    parcial_numerica_a = parcial_simbolica_a.subs(dic) #Convierte la derivada de str a expresión numérica
    #print(parcial_numerica_a)
    
    parcial_simbolica_b = diff(y, b) #Derivada parcial respecto de b en formato str
    #print(diff(y, b))
    parcial_numerica_b = parcial_simbolica_b.subs(dic) #Convierte la derivada de str a expresión numérica
    #print(parcial_numerica_b)
    
    lista_errores = []
    error_a = float(input('Ingrese el valor del error de la variable "a": '))
    error_b = float(input('Ingrese el valor del error de la variable "b": '))
    lista_errores.append(error_a)
    lista_errores.append(error_b)

    error_y = abs(parcial_numerica_a)*abs(error_a) + abs(parcial_numerica_b)*abs(error_b) 
    
    print(f'\nEl error de la función "y = {y}" cuando "a = {dic[a]}" con un error de "Δa = {round(error_a, 7)}" y \n"b = {dic[b]}" con un error de "Δb = {round(error_b, 7)}" \nes de: "Δy = {round(error_y, 7)}"')
    
    sustituciones_finales(dic,y, error_y, lista_errores)
    
    return error_y

def Calculos_3_v(funcion):
    
    a, b, c = symbols(f'a b c', real=True)

    y = eval(funcion)

    dic = {}
    
    dic[a] = float(input('Ingrese el valor de la variable "a": '))
    dic[b] = float(input('Ingrese el valor de la variable "b": '))
    dic[c] = float(input('Ingrese el valor de la variable "c": '))

    print(dic)
    
    parcial_simbolica_a = diff(y, a) #Derivada parcial respecto de a en formato str
    #print(diff(y, a))
    parcial_numerica_a = parcial_simbolica_a.subs(dic) #Convierte la derivada de str a expresión numérica
    #print(parcial_numerica_a)
    
    parcial_simbolica_b = diff(y, b) #Derivada parcial respecto de b en formato str
    #print(diff(y, b))
    parcial_numerica_b = parcial_simbolica_b.subs(dic) #Convierte la derivada de str a expresión numérica
    #print(parcial_numerica_b)

    parcial_simbolica_c = diff(y, c) #Derivada parcial respecto de c en formato str
    #print(diff(y, c))
    parcial_numerica_c = parcial_simbolica_c.subs(dic) #Convierte la derivada de str a expresión numérica
    #print(parcial_numerica_c)
    
    lista_errores = []
    error_a = float(input('Ingrese el valor del error de la variable "a": '))
    error_b = float(input('Ingrese el valor del error de la variable "b": '))
    error_c = float(input('Ingrese el valor del error de la variable "c": '))
    lista_errores.append(error_a)
    lista_errores.append(error_b)
    lista_errores.append(error_c)

    error_y = abs(parcial_numerica_a)*abs(error_a) + abs(parcial_numerica_b)*abs(error_b) + abs(parcial_numerica_c)*abs(error_c)
    
    print(f'\nEl error de la función "y = {y}" cuando "a = {dic[a]}" con un error de "Δa = {round(error_a, 7)}","b = {dic[b]}" con un error de "Δb = {round(error_b, 7)}" y \n"c = {dic[c]}" con un error de "Δc = {round(error_c, 7)}" es de: "Δy = {round(error_y, 7)}"')
    
    sustituciones_finales(dic,y, error_y, lista_errores)
    
    return error_y


def Calculos_4_v(funcion):
    
    a, b, c, d = symbols(f'a b c d', real=True)

    y = eval(funcion)

    dic = {}
    
    dic[a] = float(input('Ingrese el valor de la variable "a": '))
    dic[b] = float(input('Ingrese el valor de la variable "b": '))
    dic[c] = float(input('Ingrese el valor de la variable "c": '))
    dic[d] = float(input('Ingrese el valor de la variable "d": '))


    print(dic)
    
    parcial_simbolica_a = diff(y, a) #Derivada parcial respecto de a en formato str
    #print(diff(y, a))
    parcial_numerica_a = parcial_simbolica_a.subs(dic) #Convierte la derivada de str a expresión numérica
    #print(parcial_numerica_a)
    
    parcial_simbolica_b = diff(y, b) #Derivada parcial respecto de b en formato str
    #print(diff(y, b))
    parcial_numerica_b = parcial_simbolica_b.subs(dic) #Convierte la derivada de str a expresión numérica
    #print(parcial_numerica_b)

    parcial_simbolica_c = diff(y, c) #Derivada parcial respecto de c en formato str
    #print(diff(y, c))
    parcial_numerica_c = parcial_simbolica_c.subs(dic) #Convierte la derivada de str a expresión numérica
    #print(parcial_numerica_c)
    
    parcial_simbolica_d = diff(y, d) #Derivada parcial respecto de d en formato str
    #print(diff(y, d))
    parcial_numerica_d = parcial_simbolica_d.subs(dic) #Convierte la derivada de str a expresión numérica
    #print(parcial_numerica_d)
    
    lista_errores = []
    error_a = float(input('Ingrese el valor del error de la variable "a": '))
    error_b = float(input('Ingrese el valor del error de la variable "b": '))
    error_c = float(input('Ingrese el valor del error de la variable "c": '))
    error_d = float(input('Ingrese el valor del error de la variable "d": '))
    lista_errores.append(error_a)
    lista_errores.append(error_b)
    lista_errores.append(error_c)
    lista_errores.append(error_d)

    error_y = abs(parcial_numerica_a)*abs(error_a) + abs(parcial_numerica_b)*abs(error_b) + abs(parcial_numerica_c)*abs(error_c) + abs(parcial_numerica_d)*abs(error_d)
    
    print(f'\nEl error de la función "y = {y}" cuando "a = {dic[a]}" con un error de "Δa = {round(error_a, 7)}", "b = {dic[b]}" con un error de "Δb = {round(error_b, 7)}",\n "c = {dic[c]}" con un error de "Δc = {round(error_c, 7)}" y "d = {dic[d]}" con un error de "Δd = {round(error_d, 7)}" es de: "Δy = {round(error_y, 7)}"')
    
    sustituciones_finales(dic,y, error_y, lista_errores)
    
    return error_y

def sustituciones_finales(dic ,funcion, error_y, lista_errores):

    y = funcion

    func_evaluada = y.subs(dic)
    
    print(f'La función al sustituir los valores apropiados nos da como resultado "y = {round(func_evaluada,7)}",\n por lo tanto "y" está entre: {round(func_evaluada,7)} +- {round(error_y,7)} ')

    extremo1 = func_evaluada + error_y
    
    extremo2 = func_evaluada - error_y
    
    print(f'\n"y" se encuentra entre {round(extremo1,7)} y {round(extremo2,7)}\n')
    
    lista_values = list(dic.values())
    lista_keys = list(dic.keys())
    
    lista_extremo1 = []
    lista_extremo2 = []

    for i in range(len(lista_values)):
        lista_extremo1.append(lista_values[i] + lista_errores[i])
        lista_extremo2.append(lista_values[i] - lista_errores[i])
    
    dic_extremo1 = dict(zip(lista_keys, lista_extremo1))
    # print(dic_extremo1)
    dic_extremo2 = dict(zip(lista_keys, lista_extremo2))
    # print(dic_extremo2)
    
    func_evaluada_extremo1 = y.subs(dic_extremo1)
    func_evaluada_extremo2 = y.subs(dic_extremo2)

    print(f'Verificamos la validez de estas etimaciones sustituyendo los valores extremos: \n Obtenemos {func_evaluada_extremo2} y {func_evaluada_extremo1}\n las estimaciones de primer orden están razonablemente cercanas de los valores exactos.')

def validarFunc(y):
    
    tupla_simb = ('a','b','c','d','+','-','*','/','(',')','0','1','2','3','4','5','6','7','8','9',' ')

    for i in y:
        if i in tupla_simb:
            pass
        else:
            print('\nError de notación')
            y = input('\nIngrese nuevamente la función a trabajar (recuerde utilizar la notación correcta): \n')
            validarFunc(y)
        print(f'La función ha sido ingresada correctamente: {y}')
        return y

def main():
    
    cant_variables = int(input('\nIngrese cuántas variables tiene la función a trabajar (2 a 4 variables): \n'))
    while (4 < cant_variables or cant_variables < 2):
        print('\nLa cantidad de variables no es correcta, ingrese un número del 2 al 4\n')
        cant_variables = int(input('\nIngrese cuántas variables tiene la función a trabajar (2 a 4 variables): \n'))
    
    print('Notación:\n Suma: + | Resta: - \n Producto: * | Cociente: / \n Potenciación: ** | Radicación: **(x/n), n y x: números reales')
    print('Las variables que puede utilizar son: a, b, c, d\nEj: En caso de usar 3 variables debe ingresar: a, b y c , en caso de usar 2 variables: a y b')
    funcion = validarFunc(input('\nIngrese la función a trabajar (recuerde utilizar la notación correcta): \n'))
    
    if cant_variables == 2:
        resultado = Calculos_2_v(funcion)

    elif cant_variables == 3:
        resultado = Calculos_3_v(funcion)

    elif cant_variables == 4:
        resultado = Calculos_4_v(funcion)
    
    repetir_programa = input('\n¿Desea volver a ejecutar el programa? (y/n) \n')
    while repetir_programa.lower() != 'y' and repetir_programa.lower() != 'n':
        repetir_programa = input('\n¿Desea volver a ejecutar el programa? (y/n) \n')
    
    if repetir_programa == 'y':
        main()
    else:
        print('El programa ha finalizado')
main()