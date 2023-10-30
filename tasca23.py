#Fes un programa que demani dues lletres minúscules i mostri les lletres de l'abecedari que hi ha entre elles, incloent-hi els extrems.

lletra_1 = input("Introdueix una lletra en minuscula: ")
lletra_2 = input("Introdueix una lletra en minuscula: ")

print(f"Les letres que hi ha entre mitg son de '{lletra_1}' i '{lletra_2}' son: ")

lletra_1 = ord(lletra_1)
lletra_2 = ord(lletra_2)

while (lletra_1 <= lletra_2):
    print(chr(lletra_1))
    lletra_1 += 1