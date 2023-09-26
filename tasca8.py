main.py >

cantidad_de_huevos = int(input("Ingrese la cantidad de huevos:
"))

cajas_llenas = cantidad_de_huevos // 6
huevos_sobrantes = cantidad_de_huevos % 6
if (huevos_sobrantes>0):
  cajas_llenas += 1
print(f"Se pueden llenar {cajas_llenas} cajas de huevos.")
print(f"Sobran {huevos_sobrantes} huevos.")
