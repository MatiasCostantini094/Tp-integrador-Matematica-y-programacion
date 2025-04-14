#Mensaje de bienvenida
numero= print("App De Binario <-> Decimal")
#Con un While true , nos inidica que siempre sera verdader la condicion , significa que el  programa se ejecuta
#Se cortara el While si se  encuentra con un brack o con una salida  
while True:     
    print(" \nMenú:")
    print("1. Decimal a Binario")
    print("2. Binario a Decimal")
    print("3. Salir")
    #Se muestra el menu de opciones para el usuario 
    opcion = input(" \nSelecciona una opción (1/2/3): ") #Se pide al usuario que ingrese una opcion del menu
    #Opcion 1
    if opcion == "1": #Verifica si la opcion seleccionada  es 1
        numero = input("Ingresa un número decimal: ") # Se  solicita u numero decimal

        if numero.isdigit(): # isdigit => es un metodo de cadena que devuelve positivo si son numeros los ingresados de 0 a 9, si no da falso
            numero_decimal = int(numero) #Convierte el valor ingresado a un numero entero
            numero_binario = bin(numero_decimal)[2:] #convierte el numero decimal a binario
            print("El número binario es:", numero_binario)#Muestra elresultado de la conversion
        else:
            print("Entrada inválida. Debes ingresar un número decimal válido.")#Si no es un numero enetero positivo el ingresado => isdigit() , devuelve falso muestra el mensaje
        #Opcion 2
    elif opcion == "2": #Verifica si la opcion seleccionada  es 2
        numero = input("Ingresa un número binario: ")#Se pide que se ingrese un numero binario
        #En esta variable al establecerla como positiva , la utilizamos para verificar si los caracteres ingresados son los validos ( "0" y "1")
        es_binario = True
        for digito in numero:
            if digito != "0" and digito != "1":#Condicion de que sean solo ("0" y "1")
                es_binario = False #Si no se cumple la condicion del if , se da como falso y se genera un corte con break- Volviendo al inicio del menu
                break
                
        if es_binario: #Si los numeros ingresados son los correctos ("0" y "1") , se ejecuta esta seccion del codigo
            numero_decimal = int(numero, 2)#Convierte el numero binario a decimal , el segundo paramtero dice que es en bas (2)
            print("El número decimal es:", numero_decimal)#Muestra el resultado de la conversion
        else:
            print("Entrada inválida. Solo puedes ingresar 0s y 1s.")#Es el mensaje de error si los numeros ingresados no corresponden a a ("0" y "1")
        #Opcion 3
    elif opcion == "3":   #Verifica si la opcion seleccionada  es 3
        print("¡Hasta luego!") # Mensaje de despedida 
        break # Rompe el Bucle 

    else:
        print("Opción no válida. Intenta con 1, 2 o 3.") # Si se ingresa una opcion que no es correcta del menu , se indica el mensaje !
#Es un menu interactivo , para convertir numeros de binarios a decimales y de decimales a binarios , con la limitacion que deben ser enteros positvos !