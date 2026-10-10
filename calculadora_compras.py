producto = input("¿Que producto compraste? ")
precio = float(input("¿Cual es el precio? "))
cantidad = int(input("¿Que cantidad compraste? "))

total = precio * cantidad
print("----Ticket de compra----")
print(f"Producto: {producto}")
print(f"Precio: {precio}")
print(f"Cantidad: {cantidad}")
print(f"Total a pagar: {total}")
print("------------------------")
