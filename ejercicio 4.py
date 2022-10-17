edad = int(input("Introduce tu edad\n"))
ingresos = float(input("Introduce tus ingresos mensuales\n"))

if edad >= 16 and ingresos >= 1000:
    print(" Deberas tributar ")
else:
    print(" No es necesario tributar ")