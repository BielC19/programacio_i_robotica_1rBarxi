#2- Fer amb CodeBlocks (5 punts):
#1 - Fer un programa que donada una dada en aquest format: ABAB et calculi el caràcter
#l’equivalent a la taula d’ASCII del nùmero AA i el BB. Exemple de la posició de les dades.
#A B A B
#Exemple si l'AA fos un 24 i el BB fos un 15 estarien així.
#2 1 4 5
#2- Demana a l’usuari l’inicial del nom i del primer cognom (en majúscules) i codifica’l
#utilitzant la taula ASCII amb el següent mode d’encriptació:
#● Valor numèric ASCII del caracter - 5
#4- Mostrar a l’usuari els caràcters encriptats amb els caràcters d’ASCII nous.

numeros = int(input("Introdueix 4 numeros junts: "))

primer = numeros//1000
segon = (numeros//100)%10
tercer = (numeros//10)%10
quart = numeros%10

numero_nou = (primer*10 + tercer)*100 + (segon*10 + quart)
print(chr(numero_nou))