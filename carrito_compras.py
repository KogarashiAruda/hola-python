
productos = []
total_compra = 0

while True:
    nombre = input("Nombre del producto (o 'fin' para terminar): ")

    if nombre.lower() == "fin":
        break


    while True:
        try:
            precio = float(input("Precio unitario: "))
            if precio <= 0:
                print("El precio debe ser un número válido y mayor a cero.")
                continue
            break
        except ValueError:
            print("Por favor, ingrese un número válido para el precio.")

    while True:
        try:
            cantidad = int(input("Cantidad: "))
            if cantidad <= 0:
                print("La cantidad debe ser un número válido y mayor a cero.")
                continue
            break
        except ValueError:
            print("Por favor, ingrese un número válido para la cantidad.")

    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    productos.append(producto)

if not productos:
    print("No se registraron productos.")
else:

    print("\n--- PRODUCTOS REGISTRADOS ---")

    for producto in productos:
        subtotal = producto["precio"] * producto["cantidad"]
        total_compra += subtotal
        print(
            f'{producto["nombre"]}: '
            f'{producto["cantidad"]} x '
            f'${producto["precio"]:.2f} = '
            f'${subtotal:.2f}'
        )

    if total_compra >= 2000:
        descuento = 0.15
    elif total_compra >= 1000:
        descuento = 0.10
    elif total_compra >= 500:
        descuento = 0.05
    else:
        descuento = 0

    cantidad_descuento = total_compra * descuento
    print(f"\nSubtotal: ${total_compra:.2f}")
    print(f"Descuento aplicado: {descuento * 100:.0f}%")
    print(f"Cantidad descontada: ${cantidad_descuento:.2f}")
    print(f"Total a pagar: ${total_compra - cantidad_descuento:.2f}")
