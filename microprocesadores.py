def calcular_descuento(cantidad, cliente):
    descuento = 0
    #definir el descuento por cantidad
    if cantidad >= 10000 and cantidad <= 20000:
        descuento = 0.10
    elif cantidad > 20000 and cantidad <= 40000:
        descuento = 0.15
    elif cantidad > 40000:
        descuento = 0.20
    #Ajustar el descuento por tipo de cliente    
    if cliente == "COMMAQ":
        descuento -= 0.02
    elif cliente == "BEL":
        descuento += 0.01
    
    return descuento

def main():

    cantidad_pedida = int(input("Ingrese la cantidad pedida(pedido mínimo 10.000 piezas.): ")) #Pedido del cliente
    
    cliente = input("Ingrese el tipo de cliente (BEL O COMMAQ): ").upper() #Tipo de cliente
    
    descuento_final = calcular_descuento(cantidad_pedida, cliente)
    
    print(f"El descuento final es de {descuento_final * 100}%")

if __name__ == "__main__":
    main()
