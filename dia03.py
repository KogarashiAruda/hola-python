nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

if edad < 13:
    print(f"{nombre} Eres un niño")
elif edad <= 17:
    print(f"{nombre} Eres un adolescente")
elif edad <= 64:
    print(f"{nombre} Eres un adulto")
else:
    print(f"{nombre} Eres un adulto mayor")