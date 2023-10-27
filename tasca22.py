#Crea una calculadora bàsica que pugui efectuar operacions de suma, resta, multiplicació i divisió.
#El programa ha de demanar a l'usuari que ingressi dos números i després li preguntarà quina operació desitja realitzar.
#No pot dividir entre 0. Depenent de l'operació seleccionada, el programa farà el càlcul i mostrarà el resultat.
#Importo la biblioteca para crear el menu interactivo

print("\n")
print("Calculator")
print("1 - Suma")
print("2 - Resta")
print("3 - Multiplicación")
print("4 - División")
print("5 - Salir del programa")
opcion = input("\n\nSelect an option (number): ")
if int(opcion) == 1:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result_suma = num1 + num2
    print("%.2f" %result_suma)
elif int(opcion) == 2:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result_resta = num1 - num2
    print("%.2f" %result_resta)
elif int(opcion) == 3:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result_multiplicacion = num1 * num2
    print("%.2f" %result_multiplicacion)
elif int(opcion) == 4:
    num1 = float(input("Enter the dividend: "))
    num2 = float(input("Enter the divisor: "))
    try:
        result_division = num1 / num2
        print("%.2f" %result_division)
    except ZeroDivisionError:
        print ("No se puede dividir entre cero.")

