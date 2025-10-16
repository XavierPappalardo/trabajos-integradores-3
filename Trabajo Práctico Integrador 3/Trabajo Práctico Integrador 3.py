#Diccionario alumnos

diccionario_alumnos = {}

#Busca y lee el archivo si lo encuentra

import os

def leer_alumnos():
    global diccionario_alumnos
    if os.path.exists("alumnos.txt") == True:
        with open("alumnos.txt", "r") as archivo:
            archivo.readline()
            for linea in archivo:
                auxiliar_diccionario = linea.strip().split(",")
                nombre = auxiliar_diccionario[0].strip()
                apellido = auxiliar_diccionario[1].strip()
                legajo = auxiliar_diccionario[2].strip()
                nota_promedio = auxiliar_diccionario[3].strip()
                diccionario_alumnos[legajo] = {"nombre": nombre,
                                               "apellido": apellido,
                                               "legajo": legajo,
                                               "notapromedio": nota_promedio,
                                               }
            for i in diccionario_alumnos:
                print(f"Alumno: {diccionario_alumnos[i]['nombre']} {diccionario_alumnos[i]['apellido']} | Legajo: {diccionario_alumnos[i]['legajo']} | Promedio: {diccionario_alumnos[i]['notapromedio']}")
                
                    
    else:
        print("El archivo no existe. Se creará uno a continuación")
        with open("alumnos.txt", "w") as archivo:
            leer_alumnos()

#Comprueba al agregar un nuevo alumno si el legajo está repetido

def validar_existe_alumno(nuevo_legajo):
    if os.path.exists("alumnos.txt") == True:
        with open("alumnos.txt", "r") as archivo:
            archivo.readline()
            for linea in archivo:
                auxiliar_diccionario = linea.strip().split(",")
                nombre = auxiliar_diccionario[0].strip()
                apellido = auxiliar_diccionario[1].strip()
                legajo = auxiliar_diccionario[2].strip()
                nota_promedio = auxiliar_diccionario[3].strip()
                diccionario_alumnos[legajo] = {"nombre": nombre,
                                               "apellido": apellido,
                                               "legajo": legajo,
                                               "notapromedio": nota_promedio,
                                               }
    for i in diccionario_alumnos:
        if i == nuevo_legajo:
            return True
    return False

#Guarda los alumnos aprobados en el archivo aprobados.txt
        
def guardar_aprobados():
    with open("aprobados.txt", "w") as archivo:
        archivo.write("nombre, apellido, legajo, notapromedio\n")
        for i in diccionario_alumnos:
            aprobados = float(diccionario_alumnos[i]["notapromedio"])
            if aprobados >= 6:
                nombre = diccionario_alumnos[i]["nombre"]
                apellido = diccionario_alumnos[i]["apellido"]
                legajo = diccionario_alumnos[i]["legajo"]
                archivo.write(f"{nombre}, {apellido}, {legajo}, {aprobados}\n")

    with open("aprobados.txt", "r") as archivo:
        archivo.readline()
        for linea in archivo:
            auxiliar_aprobados = linea.strip().split(",")
            nombre = auxiliar_aprobados[0].strip()
            apellido = auxiliar_aprobados[1].strip()
            legajo = auxiliar_aprobados[2].strip()
            nota_promedio = auxiliar_aprobados[3].strip()
            print(f"Alumno: {nombre} {apellido} | Legajo: {legajo} | Promedio: {nota_promedio}")
            
#Agregar nuevo alumno

def agregar_alumno():
    global diccionario_alumnos

    #Variable auxiliar para verificar la validez de los nombres y apellidos ingresados
    
    alfabeto = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    while True:
        agregar_nuevo = input("¿Desea agregar un nuevo alumno? Ingrese 'a' si así lo desea, o 'b' si ya no desea agregar más alumnos: ")
        if agregar_nuevo.lower() == "a":
            try:
                while True:
                    caracter_valido = True
                    nuevo_nombre = input("Agregue el nombre del nuevo alumno: ")
                    if nuevo_nombre == "":
                        print("El nombre ingresado no es válido. Por favor ingrese un nombre de alumno válido")
                        continue
                    for caracter in nuevo_nombre:
                        if caracter not in alfabeto:
                           caracter_valido = False
                    if caracter_valido == False:
                        print("El nombre ingresado no es válido. Por favor ingrese un nombre de alumno válido")
                        continue
                    else:
                        break
                while True:
                    caracter_valido = True
                    nuevo_apellido = input("Ingrese el apellido del nuevo alumno: ")
                    if nuevo_apellido == "":
                        print("El apellido ingresado no es válido. Por favor ingrese un apellido de alumno válido")
                        continue
                    for caracter in nuevo_apellido:
                        if caracter not in alfabeto:
                           caracter_valido = False
                    if caracter_valido == False:
                        print("El apellido ingresado no es válido. Por favor ingrese un apellido de alumno válido")
                        continue
                    else:
                        break
                while True:
                    nuevo_legajo = input("Ingrese el legajo del nuevo alumno. Recuerde que debe estar compuesto de 5 números: ")
                    if len(nuevo_legajo) != 5:
                        print("El legajo ingresado es inválido. Por favor ingrese un legajo de 5 números")
                        legajo_valido = False
                    else:
                        legajo_valido = True
                    legajo_comprobacion = validar_existe_alumno(nuevo_legajo)
                    if legajo_comprobacion == True:
                        print(f"El legajo {nuevo_legajo} ya existe en el archivo alumnos.txt, no se permite su escritura")
                    if legajo_comprobacion == False and legajo_valido == True:
                        break
                    else:
                        continue
                while True:
                    nuevo_promedio = float(input("Ingrese el promedio del nuevo alumno: "))
                    if nuevo_promedio > 10 or nuevo_promedio < 1:
                        print("El nuevo promedio ingresado es inválido. Por favor ingrese un promedio entre 1 y 10")
                        continue
                    else:
                        break
                diccionario_alumnos[nuevo_legajo] = {"nombre": nuevo_nombre,
                                                             "apellido": nuevo_apellido,
                                                             "legajo": nuevo_legajo,
                                                             "notapromedio": nuevo_promedio,
                                                            }
                with open("alumnos.txt", "a") as archivo:
                    archivo.write(f"\n{nuevo_nombre}, {nuevo_apellido}, {nuevo_legajo}, {nuevo_promedio}")
                    break
                             
            except ValueError:
                print("Dato inválido. Ingrese datos válidos para cada apartado")
        elif agregar_nuevo.lower() == "b":
            print("No se agregarán más alumnos")
            return

        else:
            print("Ingrese un dato válido por favor")


#Menú

continuar_operando = True
print("Hola, gracias por ingresar al sistema de registro de alumnos.")
while continuar_operando == True:
    continuar_operando = True
    operacion = input("Ingrese la operación que desea realizar.\nIngrese:\n'a'- Para leer el registro de alumnos\n'b'- Para agregar un nuevo alumno al registro\n'c'- Para ver la lista de alumnos aprobados\n'd'- Para salir del sistema: ")
    if operacion.lower() == "a":
        leer_alumnos()
    elif operacion.lower() == "b":
        agregar_alumno()
    elif operacion.lower() == "c":
        guardar_aprobados()
    elif operacion.lower() == "d":
         print("Gracias por usar el sistema de registro de alumnos")
         continuar_operando = False
    else:
        print("El comando ingresado no es válido. Por favor, vuelva a intentarlo")    
