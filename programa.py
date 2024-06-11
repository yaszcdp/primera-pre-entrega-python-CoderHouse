###PRIMERA PRE-ENTREGA CURSO PYTHON - CODER HOUSE
##Comisión: 57815
##Estudiante: Escobar Tomé Yas'z.

#Objetivo:
#Practicar el concepto de funciones. Preparar la parte lógica para el registro de usuarios. 

#Consigna:
#Crear un programa que permita emular el registro y almacenamiento de usuarios en una base de datos. 
#Crear el programa utilizando el concepto de funciones, diccionarios, bucles y condicionales. 

#Sugerencias:
#Formato de registro: Nombre de usuario y Contraseña. 
#Utilizar una función para almacenar la info y otra para mostrarla. 
#Utilizar un diccionario para almacenar dicha info, con el par user-contraseña. 
#Utilizar otra función para el login de users, comprobando que la contraseña coincida con el user. 


def registro(lista): #Defino la función registro, que recibirá por parámetro la lista de dicts. 
    print("\n-------[ Completa el registro ]-------") 
    nombre = input("♥ Nombre: ")
    apellido = input("♥ Apellido: ")
    val = 0

    while val != 1: 
        user = input("♥ Usuario: ")
        for usuario in lista: #recorro la lista de usuarios
            if user == usuario['user']: #Si el nombre de usuario coincide lanzo mensaje.
                print("**¡Usuario ya existente! D: ")
                break
        else: #si no hay usuario existente con el nombre ingresado corto el bucle. 
            val = 1

    contraseña = input("♥ Contraseña: ")
    confirmar_contraseña = input("♥ Confirmar Contraseña: ")
    while confirmar_contraseña != contraseña: #mientras las contraseñas no coincidan se repetirá la solicitud de entrada. 
        confirmar_contraseña = input("**Las contraseñas no coinciden... Intenta nuevamente\n♥ Confirmar Contraseña: ")
    else:
        print("¡Registro completado!")

    nuevo_usuario = {'nombre': nombre, 'apellido': apellido, 'user': user, 'contraseña': contraseña} #defino un nuevo dict con la información ingresada. 
    return nuevo_usuario #retorno el dict nuevo usuario. 

def login(lista): #Defino la función Log In que recibirá por parámetro la lista de dicts. 
    print("\n--------------[ Log In ]--------------")
    val = 0 
    pos = 0

    while val != 1:
        user = input("♥ Usuario: ")
        for i, usuario in enumerate(lista): #recorro la lista de dicts para encontrar el user. 
            if usuario['user'] == user: #si el usuario coincide
                while val != 1: #paso a validar la contraseña
                    contraseña = input("♥ Contraseña: ")
                    if usuario['contraseña'] == contraseña: #Si las contraseñas coinciden aviso al user. 
                        print("¡Inicio de sesión exitoso! :D")
                        val = 1 #cambio el valor de val para cortar el bucle. 
                        pos = i #guardo la posición del usuario en la lista. Esto me servirá para la función de bienvenida. 
                    else:
                        print("**Ups, contraseña inválida. :/")

        if val == 0: #si se recorrió toda la lista sin encontrar coincidencias aviso al usuario. 
            print("**El usuario no existe... :(")

    return pos         

def bienvenida (pos, lista): #Defino la función de bienvenida que recibe por parámetros la lista y la posición del user loggeado en ella. 
    print("\n--------------------------------------")
    print("     ¡ Buenas,", lista[pos]['nombre'], lista[pos]['apellido'], "! ") #Accedo a la info del user para saludarlo. 
    print("--------------------------------------")

def cabecera():
    print("\n[ Primera pre-entrega curso PYTHON - Coder House ]")
    print("[ Estudiante: Yas'z Escobar Tomé. ]")

def menu(): #Defino la función menú. 
    op = -1
    print("\n---------------[ MENÚ ]---------------\n1- Ingresar.\n2- Registrarse.\n0- Salir.")
    try:
        op = int(input("\nElije una opción: "))
        while op < 0 or op >= 3: #mientras la op ingresada no sea ni 1, ni 2 o 0. 
            op = int(input("**Ingresa una opción válida: ")) #Pido que reingrese la opción. 
    except ValueError: #excepción para controlar que no ingrese un tipo de dato inválido. 
        print("**Tipo de dato inválido! Ingresa un número.")    
    return op

def programa (): #Defino la función programa que se encargará de llamar al resto de las funciones. 
    cabecera()
    usuarios = [] #creo una lista q será usada como lista de dicts. 
    op = -1
    while op != 0: #Usaré 0 como valor para salir del programa. 
        op = menu()
        #Con un if anidado accedo a las distintas opciones del menú. 
        if op == 1:
            i = login(usuarios)
            bienvenida(i, usuarios)
        elif op == 2:
            nuevo = registro(usuarios)
            usuarios.append(nuevo)
        elif op == 0:
            print("\n--------------------------------------")
            print("   ¡Gracias por probar mi programa!\n   Hasta lueguito.. ;)")
            print("--------------------------------------")

programa()



