#Mensaje de bienvenida
print("Aplicación Binario <-> Decimal")
#Esta funcion convierte de decimal a binario. Se puede simplificar con funciones de math en py
def decimal_a_binario(numero):
    binario = ''
    while numero > 0:                       # Para que se cumpla la condicion numero debe ser + / mayor a 0
        binario = str(numero % 2) + binario # Se concatena el residuo (0 o 1) al inicio de la cadena
        numero = numero // 2                # Se divide el numero entre 2 para obtener el siguiente digito
    return binario or '0'                   # Si el numero es 0 , devolvemos el "0"         
#Esta funcion convierte de binario a decimal. Se puede simplificar con funciones de math en py  
def binario_a_decimal(binario):
    decimal = 0
    longitud = len(binario)                  # Se obtiene la longitud del numero para calcular la posicion
    for i in range(longitud):                
        digito = int(binario[i])             # Convierte cada digito binario en entero
        potencia = longitud - 1 - i          # Calcula la potencia correspondiente al digito
        decimal += digito * (2 ** potencia)  # Sumamos el resultado a la variable decimal
    return decimal

while True:             #Esta parte nos crea un ciclo infinito , hasta que el usuario elija salir.Con la opcion 3 sale con un break
    print("\nMenú:")
    print("1. Decimal a Binario")
    print("2. Binario a Decimal")
    print("3. Salir")
    opcion = input("Seleccione una opción (1/2/3): \n ")  #Se muestra el menu de opciones para el usuario para interactuar

    if opcion == "1":                                  #Si el usuario elige la opcion "1" entra en accion este argumento ; 
        numero_decimal = int(input("Ingrese un número decimal: \n")) # se pide que ingrese un numero
        resultado = decimal_a_binario(numero_decimal)              # llama a la funcion "decimal_a_binario"
        print(f"El numero en binario es: {resultado}")                             #Imprime el resultado esperaddo y vuelve al menu 

    elif opcion == "2":                                 # Si el usuario elige la opcion "2" entra en accion este argumento;
        numero_binario = input("Ingrese un número binario: \n")      # Se pide que ingrese un numero
        if all(digito in '01' for digito in numero_binario):       # Se verifica que lo ingresado sea solo "01"
            resultado = binario_a_decimal(numero_binario)          # Se llama a la funcion "binario_a_decimal"
            print(f"El numero en  decimal es: {resultado}")                         # Se imprime el resultado 
        else:
            print("¡Error! Ingrese solo dígitos binarios (0 y 1).") # mensaje de error si se elige una opcion que no es valida

    elif opcion == "3":                                             #Esta seccion el la salida del programa 
        print("Saliendo del programa, gracias por jugar...")        #Mensaje de salida
        break

    else:
        print("Opción inválida. Intente nuevamente.")               #Mensaje si se elige una opcion invalida en el menu de seleccion

        #Resumen del programa : 
        # Convierte los numeros de binario a decimal y viceversa
        #Tiene un menu interactivo , aplicamos bucles While y for , condcionales y validaciones , se puede ejecutar infinitamente.
        