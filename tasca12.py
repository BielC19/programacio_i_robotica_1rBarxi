#1- Et demani una lletra minúscula i et retorni la seva lletra majúscula. 2- Et demani una lletra majúscula i et retorni la seva lletra minúscula.
diferencia = ord("a")-ord("A")              #mira la diferencia entre un caracter en minuscula i un en majúscula
minuscula = input("Introdueix el caracter en minuscula: ")      #Demana el valor en mnuscula
minuscula_a_majuscula = chr(ord(minuscula)-diferencia)          #canvia de minusucla a majúscula
print(f"\n La teva lletra minuscula es en majuscula {minuscula_a_majuscula} i el codi ascii es {ord(minuscula)-diferencia}")    #retorna el codi

majuscula = input("Introdueix un caracter en majúscula: ")      #Demana el valor en majúscula
majuscula_a_minuscula = chr(ord(majuscula)+diferencia)          #canvia de majúscula a minuscula
print(f"\n La teva lletra majuscula en minuscula {majuscula_a_minuscula} i el codi acsii es {ord(majuscula)+diferencia}")       #retorna el codi


valor = input("introdueix una lletra i te la canviara de majúscula a minuscula o al reves")
if (valor>=65 and valor<=60):
    print(f"La convercio de majúscula a minuscula es {chr(ord(valor)+diferencia)}")
else:
    print(f"La convercio de minusucla a majúscula es {chr(ord(valor)-diferencia)}")
