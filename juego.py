import random
import os
import time

def dibujo_mensajes(linea1="", linea2="", linea3="", linea4="", mensaje=""):
    '''Funcion principal interfaz ascii'''
    print(f'''
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/,,(*/((@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(&%%@@@@@@,.@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@##*,,,****(#@@@@@@{linea1: ^25}@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%/***,*,*(##(@@@@@{linea2: ^25}@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/#*%@@&*%@@&%(/@@@@{linea3: ^25}@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/**,,*,%(**#*/@@@@{linea4: ^25}@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/(/(#&@@%%(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@((###%%@%(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#(/&&&&@%%#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/(*/,,, (&&&(//(//#,/@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@... //*,#%.&@@@&@@@@((%%#//((,...@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@,*,,,*%%%%%%&#%(/..*%%.%&&%%&&&,(*(/&@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@,***,,,%%%%%#%%#*...,,,#&&%%&&&&,//*##,@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@*,****/,%%%%%%%&&/,...,*&&%&%&&&&.*,(%(,/@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@///,,*((,&&&&%&&&&&(....&&&&%&&&&&(#,,,,(%*@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@,.(%%%%#&/&&&&%&%%&&&&,/&&&&&&&&&&&&&,,,,//,*@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@*,*,,*,(#&@@&&&%&&&&&&&%&&&&&&&&&&&&&@@(#****/**@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@,*,*****#%&@@@&&&&%&&&&&&%%%&&&&&&&&&&@@@@*(/*//,./.@@@@@@@@@@@@@
    @@@@@@@@@@@@@@.. .*,*(%/@@@@@&&&&&&&&%%%&&&&&&&@@@@@&@@@@@*(%/(* , ,#@@@@@@@@@@@
    @@@@@@@@@@*..,.....(#,@@@@@@@@%&%%%&&@@@&%&@@@@@@@&@&@@*&%@(#/(., ****,@@@@@@@@@
    @@@@@@@&,,,,/.,*/.%%%#@@@@@@@@##%&@@@@@&&@@@@@@@@@%&&@@@@@@@@#(,**,. *,.*/@@@@@@
    %%%%%(.#*,@#,,%&&@#,%@//@@(#@@*&@,*&@##@@/#@@/(@&*(@(*&@**@&,/@%@&,.&(.*(.,#&&&&
    &&(/.%.*(,@@(.*@@@*&####&&&&#%#&&&&/#@@@(**(&@@&(***@%&&&&&&/&@@%@#.&/(&@.##*.&&
    &@@/@@,&@#&&&/&&*&&&%&%%%%%%%&&&&&&@@@@@@@@@@@@@@@@@@&&&&&%&&%&&&%%&&*&@,*#.&@/%
    {mensaje: ^78}''') 

def verificar_usuario(usuario, contraseña):
    '''Verifica que el usuario a loguear sea correcto y devuelve las fichas del mismo'''
    logged = False
    fichas = 0 # Dejar esto o al haber error de logueo arrojara error.
    try:
        cuentas = open("cuentas.txt","rt")
        linea = cuentas.readline()
        while linea:
            nombre_usuario, password, leer_fichas = linea.split(";")
            if nombre_usuario == usuario and password == contraseña:
                logged = True
                fichas = int(leer_fichas)
            linea = cuentas.readline()
    except:
        pass
    finally:
        try:
            cuentas.close()
        except:
            pass
    
    return logged, fichas

def verificar_existencia_usuario(usuario):
    '''Esta funcion es usada para verificar que el usuario a registrar no sea uno existente y se genere un registro duplicado'''
    correcta = True
    try:
        cuentas = open("cuentas.txt","rt")
        linea = cuentas.readline()
        while linea:
            nombre_usuario, password, leer_fichas = linea.split(";")
            if nombre_usuario == usuario:
                correcta = False
            linea = cuentas.readline()
    except:
        pass
    finally:
        try:
            cuentas.close()
        except:
            print("No se ha detectado archivo de cuentas. Creando...")
    return correcta

def crear_cuenta(usuario, contraseña):
    '''Crear la cuenta en cuentas.txt con append, al ser a+ si el archivo no existe, se crea'''
    fichas_iniciales = 1000
    try:
        entrada = open("cuentas.txt", "a+")
        entrada.write(f"{usuario};{contraseña};{fichas_iniciales}\n")
    except:
        pass
    finally:
        entrada.close()
    return fichas_iniciales



def guardar_datos(jugador):
    '''Funcion para guardar las fichas actuales del jugador, se usa temporal.txt como helper.'''
    try:
        os.rename("temporal.txt", "cuentas.txt") #por si el rename falla en el intento de guardar anterior, esta linea trata de corregirlo.
    except:
        pass
    try:
        entrada = open("cuentas.txt","rt")
        salida = open("temporal.txt","wt")
        linea = entrada.readline()
        while linea:
            aux = linea
            usuario, password, fichas = aux.split(";")
            if usuario == jugador["nombre"]:
                salida.write(f"{usuario};{password};{jugador['fichas']}\n")
            else:
                salida.write(linea)
            linea = entrada.readline()
    except:
        pass
    finally:
        try:
            entrada.close()
            salida.close()
            os.remove("cuentas.txt")
            time.sleep(0.2)
            os.rename("temporal.txt", "cuentas.txt")
        except:
            pass

def evaluar_fichas(jugador):
    '''Funcion para verificar en caso de que el usuario no tiene mas fichas se le hace un challenge para recargar.'''
    if jugador["fichas"] == 0:
        print("Usted no cuenta con fichas.")
        while jugador["fichas"] == 0:
            recarga(jugador)
    guardar_datos(jugador)

def crear_mazo(num_mazos, inicio=0, mazo=[]):
    '''Funcion recursiva para crear el maso, recive la cantidad de mazos que se desea utilizar'''
    cartas = [["♥", "A", 11], ["♥", "K", 10], ["♥", "Q", 10], ["♥", "J", 10], ["♥", "10", 10], ["♥", "9", 9], ["♥", "8", 8], ["♥", "7", 7], ["♥", "6", 6], ["♥", "5", 5], ["♥", "4", 4], ["♥", "3", 3], ["♥", "2", 2], ["♦", "A", 11], ["♦", "K", 10], ["♦", "Q", 10], ["♦", "J", 10], ["♦", "10", 10], ["♦", "9", 9], ["♦", "8", 8], ["♦", "7", 7], ["♦", "6", 6], ["♦", "5", 5], ["♦", "4", 4], ["♦", "3", 3], ["♦", "2", 2], ["♠", "A", 11], ["♠", "K", 10], ["♠", "Q", 10], ["♠", "J", 10], ["♠", "10", 10], ["♠", "9", 9], ["♠", "8", 8], ["♠", "7", 7], ["♠", "6", 6], ["♠", "5", 5], ["♠", "4", 4], ["♠", "3", 3], ["♠", "2", 2], ["♣", "A", 11], ["♣", "K", 10], ["♣", "Q", 10], ["♣", "J", 10], ["♣", "10", 10], ["♣", "9", 9], ["♣", "8", 8], ["♣", "7", 7], ["♣", "6", 6], ["♣", "5", 5], ["♣", "4", 4], ["♣", "3", 3], ["♣", "2", 2]]
    if inicio < num_mazos:
        mazo.extend(cartas)
        crear_mazo(num_mazos, inicio + 1, mazo)
    random.shuffle(mazo)
    return mazo

def apuestas(jugador):
    '''Evalua si el usuario puede apostar la cantidad deseada y si ingresa el valor correcto.'''
    apuestaOk = False
    while True:
        try:
            apuesta = int(input(f"Por favor, ingrese su apuesta: "))
            if apuesta > jugador.get("fichas"):
                print("La apuesta no puede ser mayor a sus fichas disponibles.")
            else:
                jugador["apuesta"] = apuesta
                apuestaOk = True
                print("La apuesta fue hecha correctamente")
            break
        except ValueError:
            print("La apuesta debe ser un numero positivo.")
    return apuestaOk

def entregar_carta(mazo):
    '''Funcion para entregar una carta del mazo.'''
    carta = mazo.pop()
    return carta

def contar(mano):
    '''Funcion para contar la suma de las cartas'''
    cuenta = 0
    for n in mano["cartas"]:
        cuenta += n[2]
    return(cuenta)

def verificar_as(mano):
    '''Verifica si la mano tiene un as en caso de que supere la cuenta para cambiarle el valor a los as'''
    tiene_as = False
    for n in mano["cartas"]:
        if n[2] == 11:
            tiene_as = True
    return tiene_as

def corregir_as(mano):
    '''Cambia el valor del primer As que encuentre.'''
    replaced = False
    cont = 0
    while replaced == False:
        if mano["cartas"][cont][2] == 11:
            mano["cartas"][cont][2] = 1
            replaced = True
        cont += 1

def jugador_acciones(jugador, crupier ,mazo, hide):
    '''Turno completo del jugador, devuelve false si True si el jugador se excede de 21'''
    turno = True
    while turno == True:
        jugador_busted = False
        if contar(jugador) < 21:
            if len(jugador["cartas"]) == 2:
                turno, duplica = duplicar(jugador, crupier, hide, mazo)
                if duplica == True:
                    jugador["cartas"].append(entregar_carta(mazo))
                    if contar(jugador) > 21:
                        jugador_busted = True
            else:
                turno = turno_jugador(jugador, crupier, hide)
            if turno == True:
                jugador["cartas"].append(entregar_carta(mazo))
        elif contar(jugador) == 21:
            mostrar_cartas(crupier, jugador, hide, mensaje=f"Usted suma: {contar(jugador)}.")
            turno = False
        else:
            if verificar_as(jugador) == True:
                corregir_as(jugador)
            else:
                jugador_busted = True
                turno = False
                mostrar_cartas
                mostrar_cartas(crupier, jugador, hide, mensaje=f"Usted se ha pasado de 21, su cuenta fue {contar(jugador)}")
                time.sleep(2)
    return jugador_busted

def duplicar(jugador, crupier, hide, mazo):
    '''Funcion para duplicar la apuesta en la primer ronda'''
    duplicar = False
    mostrar_cartas(crupier, jugador, hide, mensaje=f"Usted suma: {contar(jugador)}, desea una carta mas?")
    eleccion = input("Ingrese 'y' para otra carta, 'd' para duplicar o 'n' para terminar su turno: ")
    while eleccion != "y" and eleccion != "n" and eleccion != "d":
        eleccion = input("Debe elegir 'y' para pedir otra carta, 'd' para duplicar o 'n' para finalizar: ")
    if eleccion.lower() == "y":
        respuesta = True
    elif eleccion.lower() == "d":
        if jugador["fichas"] >= (jugador["apuesta"] * 2):
            duplicar = True
            respuesta = False
            jugador["apuesta"] *= 2
            print(f"La apuesta ha sido duplicada, la apuesta actual es de {jugador['apuesta']}")
        else:
            print("No posee las fichas suficientes para duplicar, se continua normalmente.")
            respuesta = True
    elif eleccion.lower() == "n":
        respuesta = False
    return respuesta, duplicar

def turno_jugador(jugador, crupier, hide):
    '''Usada para eleccion del jugador al pedir cartas'''
    mostrar_cartas(crupier, jugador, hide, mensaje=f"Usted suma: {contar(jugador)}, desea una carta mas?")
    eleccion_turno = input("Ingrese 'y' para recibir otra carta o 'n' para terminar su turno: ")
    return evaluar_respuesta(eleccion_turno)

def evaluar_respuesta(eleccion_turno):
    '''Usada para evaluar la respuesta del jugador, llamada por turno_jugador y al final del turno'''
    respuesta = False
    while eleccion_turno != "y" and eleccion_turno != "n":
        eleccion_turno = input("Debe elegir 'y' para continuar o 'n' para finalizar: ")
    if eleccion_turno.lower() == "y":
        respuesta = True
    elif eleccion_turno.lower() == "n":
        respuesta = False
    return respuesta

def string_cartas(mano):
    '''Genera un string con las cartas del jugador'''
    cartas_mostrar = ""
    for c in mano["cartas"]:
        cartas_mostrar += f" {c[1]}{c[0]} "
    return cartas_mostrar

def mostrar_cartas(crupier, jugador, hide, mensaje=""):
    '''Llamar al dibujo y revelar las cartas dependiendo el valor de hide para saber si el revelado del crupier es parcial o completo'''
    if hide == True:
        dibujo_mensajes(mensaje=mensaje, linea1="CRUPIER", linea2=f"{crupier['cartas'][0][1]}{crupier['cartas'][0][0]}", linea3="TUS CARTAS", linea4=f"{string_cartas(jugador)}")
    else:
        dibujo_mensajes(mensaje=mensaje, linea1="CRUPIER", linea2=f"{string_cartas(crupier)}", linea3="TUS CARTAS", linea4=f"{string_cartas(jugador)}")

def repartir(jugador, crupier, mazo, cantidad=2):
    '''Repartida inicial recursiva de cada mano'''
    if cantidad > 0:
        jugador["cartas"].append(entregar_carta(mazo))
        crupier["cartas"].append(entregar_carta(mazo))
        repartir(jugador, crupier, mazo, cantidad-1)

def finalizar_turno(jugador, crupier, premio, mazo, num_mazos):
    '''Reparte premio y resetea los valores para iniciar otra partida, además llama para guardar datos y verificar el estado del mazo'''
    jugador["fichas"] = jugador["fichas"] + premio
    jugador["cartas"] = []
    jugador["apuesta"] = 0
    crupier["cartas"] = []
    guardar_datos(jugador)
    verificar_mazo(mazo, num_mazos)
    return mazo

def verificar_mazo(mazo, num_mazos):
    '''Verifica que haya cartas en el maso para seguir jugando, si baja a menos de 1/4 del inicial, se genera un nuevo mazo.'''
    if len(mazo) < (48*num_mazos)//4:
        return crear_mazo(num_mazos)

def turno_crupier(crupier, jugador, mazo, hide):
    '''Inicia el turno del crupier'''
    mostrar_cartas(crupier, jugador, hide, mensaje=f"El crupier suma {contar(crupier)}")
    crupier_busted = False
    time.sleep(1.5)
    while contar(crupier) <= 16:
        crupier["cartas"].append(entregar_carta(mazo))
        mostrar_cartas(crupier, jugador, hide, mensaje=f"El crupier suma {contar(crupier)}")
        time.sleep(1.5)
        if contar(crupier) > 21:
            if verificar_as(crupier) == True:
                corregir_as(crupier)
            else:
                crupier_busted = True
    return crupier_busted

def evaluar_resultado(jugador, crupier, crupier_busted, jugador_busted):
    '''Evalua el resultado en base a los datos del jugador y crupier'''
    black_jack = False
    gana_jugador = False 
    if crupier_busted == True and jugador_busted == False:
        if verificar_blackjack(jugador) == True:
            premio = int((jugador["apuesta"] / 2) * 3)
            black_jack = True
        else:
            premio = jugador["apuesta"]
        gana_jugador = True
    elif contar(jugador) > contar(crupier) and crupier_busted == False and jugador_busted == False:
        if verificar_blackjack(jugador) == True:
            premio = int((jugador["apuesta"] / 2) * 3) #verificar esto despues
            black_jack = True
        else:
            premio = jugador["apuesta"]
        gana_jugador = True
    elif contar(jugador) == contar(crupier) and jugador_busted == False:
        premio = 0
        gana_jugador = True
    else:
        premio = -(jugador["apuesta"])
    return gana_jugador, premio, black_jack

def verificar_blackjack(jugador):
    '''Verifica si el jugador tiene blackjack'''
    black_jack = False
    if len(jugador["cartas"]) == 2 and contar(jugador) == 21:
        black_jack = True
    return black_jack

def mostrar_resultado(ganador, premio, black_jack):
    '''Muestra el resultado al usuario'''
    if ganador == True and premio != 0:
        if black_jack == True:
            print("Black Jack! 3:2 para usuario. Ha ganado", premio)
        else:
            print("El usuario ha ganado: ", premio)
    elif ganador == True and premio == 0:
        print("Empate, se devuelven las apuestas")
    elif ganador == False:
        print("Usted ha perdido")

def recarga(jugador):
    '''Recarga fichas al usuario con un challenge matematico'''
    print("Al tener 0 fichas puede completar un desafio matematico para recargar.")
    print("Cual es el resultado de la siguiente operación matematica?")
    valor0 = random.randint(1, 20)
    valor1 = random.randint(1, 10)
    valor2 = random.randint(1, 10)
    valor3 = random.randint(1, 20)
    resultado = int(input(f"{valor0} + {valor1} * {valor2} - {valor3} = "))
    verificador = valor0 + valor1 * valor2 - valor3
    if resultado == verificador:
        jugador["fichas"] = 1000
        print("Ha respondido correctamente, se han cargado 1000 fichas en su cuenta\n")
    else:
        print("Su respuesta es incorrecta.")

num_mazos = 4
dibujo_mensajes(mensaje="Bienvenido a Blackjack UADE", linea2="Programacion 1", linea3="Grupo 4")
time.sleep(2)

#Inicio Loguin
dibujo_mensajes(mensaje="Si ya cuenta con una cuenta presione 'i', para registrarse 'n'")
eleccion = input("Su elección: ")
ingresado = False
while ingresado == False:
    if eleccion.lower() == "i":
        login = False
        intentos = 0
        while login == False and intentos < 3:
            dibujo_mensajes(mensaje="Por favor, ingrese su usuario y contraseña")
            usuario = input("Usuario: ")
            contraseña = input("Ingrese su contraseña: ")
            login, fichas = verificar_usuario(usuario, contraseña)
            intentos += 1
            if login == False:
                dibujo_mensajes(mensaje="Contraseña o usuario incorrecto, intente nuevamente.")
                time.sleep(2)
            else:
                ingresado = True
        if login == False:
            dibujo_mensajes(mensaje="Ha superado el maximo de intentos. Por favor cree una cuenta.")
            time.sleep(2)
            eleccion = input("Si ya cuenta con una cuenta presione 'i', caso contrario 'n': ")
    elif eleccion.lower() == "n":
        cuenta_correcta = False
        dibujo_mensajes(mensaje="Ingrese el usuario y contraseña que desea, minimo 3 caracteres.")
        usuario = input("Nombre de usuario: ")
        password = input("Contraseña: ")
        while cuenta_correcta == False:
            cuenta_correcta = verificar_existencia_usuario(usuario)
            if len(usuario) < 3 or len(password) < 3:
                cuenta_correcta = False
            if cuenta_correcta == False:
                dibujo_mensajes(mensaje="El usuario esta en uso o no cumple con el minimo de 3 caracteres.")
                usuario = input("Ingrese el nombre de usuario con el que se indentificara: ")
                password = input("Ingrese la contraseña que usara para identificarse: ")
            if cuenta_correcta == True:
                dibujo_mensajes(mensaje="Cuenta Creada correctamente.")
                fichas = crear_cuenta(usuario, password)
                ingresado = True
                time.sleep(2)
    else:
        dibujo_mensajes(mensaje="Debe seleccionar una opción.")
        eleccion = input("Si ya cuenta con una cuenta presione 'i', caso contrario 'n': ")
    
    if ingresado == True:
        jugador = {
            "nombre": usuario,
            "fichas": fichas,
            "cartas": [],
            "apuesta": 0,
        }
        crupier = {
            "cartas": [],
        }

    mazo = crear_mazo(num_mazos)

## Inicio Juego
dibujo_mensajes(mensaje=f"Bienvenido {jugador['nombre']}, actualmente tienes {jugador['fichas']} fichas.")
evaluar_fichas(jugador)
gameContinues = True
while gameContinues == True:
    apuesta = False
    while apuesta == False:
        apuesta = apuestas(jugador)
    
    repartir(jugador, crupier, mazo)
    hide = True
    mostrar_cartas(crupier, jugador, hide)
    jugador_busted = jugador_acciones(jugador, crupier, mazo, hide)

    time.sleep(0.3)
    
    hide = False
    mostrar_cartas(crupier, jugador, hide)
    crupier_busted = turno_crupier(crupier, jugador, mazo, hide)
    ganador, premio, black_jack = evaluar_resultado(jugador, crupier, crupier_busted, jugador_busted)
    mostrar_resultado(ganador, premio, black_jack)
    time.sleep(3)
    finalizar_turno(jugador, crupier, premio, mazo, num_mazos)
    evaluar_fichas(jugador)
    
    dibujo_mensajes(mensaje=f"Usted tiene {jugador['fichas']} fichas. Desea continuar jugando?")
    continua = input("Ingrese 'y' para seguir o 'n' para abandonar ahora: ")
    while continua != True and continua != False:
        continua = evaluar_respuesta(continua)
        if continua == False:
            print("Gracias por haber jugado. Vuelva pronto!")
            gameContinues = False



