sexo = input("introduce tu sexo (H o M), \n")
nombre = input("introduce tu nomnre, \n")

if sexo == "m":
    if nombre[0].lower() < "m":
         print("tu grupo es el A")
    else:
         print("tu grupo es el B")

elif sexo == "h":
    if nombre[0].lower() > "m":
         print("tu grupo es el A")
    else:
         print("tu grupo es el B")
