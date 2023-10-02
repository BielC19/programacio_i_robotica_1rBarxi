#1- Et demani una lletra minúscula i et retorni la seva lletra majúscula. 2- Et demani una lletra majúscula i et retorni la seva lletra minúscula.
diferencia = ord("a")-ord("A")
minuscula = input("Introdueix el caracter en minuscula: ")
minuscula_a_majuscula = chr(ord(minuscula)-diferencia)
print(f"\n La teva lletra minuscula es en majuscula {minuscula_a_majuscula} i el codi ascii es {ord(minuscula)-diferencia}")

majuscula = input("Introdueix un caracter en majúscula: ")
majuscula_a_minuscula = chr(ord(majuscula)+diferencia)
print(f"\n La teva lletra majuscula en minuscula {majuscula_a_minuscula} i el codi acsii es {ord(majuscula)+diferencia}")
