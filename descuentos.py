nom_cliente = input("Ingrese el nombre del cliente: ")

while True:
    try:
        precio = float(input("Ingrese el precio del producto: "))
        if precio <= 0:
            print("El precio debe ser mayor a cero. Intente nuevamente.")
            continue
        break
    except ValueError:
        print("Por favor, ingrese un número válido.")
        continue
    

while True: 
    try:
        cantidad = int(input("Ingrese la cantidad del producto: "))
        if cantidad <= 0:
            print("La cantidad debe ser mayor a cero. Intente nuevamente.")
            continue
        break
    except ValueError:
        print("Por favor, ingrese un número válido.")
        continue


subtotal = precio * cantidad
if subtotal >= 2000:
    descuento = 0.15
elif subtotal >= 1000:
    descuento = 0.10
elif subtotal >= 500:
    descuento = 0.05
else:
    descuento = 0

cantidad_descuento = subtotal * descuento
total = subtotal - cantidad_descuento

print("\n----- TICKET DE COMPRA -----")
print(f"Cliente: {nom_cliente}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Descuento aplicado: {descuento * 100:.0f}%")
print(f"Cantidad descontada: ${cantidad_descuento:.2f}")
print(f"Total a pagar: ${total:.2f}")
print("----------------------------")