def Descuento(precio):
    #Para el precio entre 0 y 100 no hay descuento.
    for precio in range(0,100):
        descuento=0
    #Para el precio entre 100 y 500 hay un descuento del 5%.
    for precio in range(100,500):
        descuento=precio*0.05
    #Para el precio a partir de 500 hay un descuento del 8%.
    else:
        descuento=precio*0.08

    return descuento
#Calcula el precio final del producto.
def PrecioFinal(precio,descuento):
    preciofinal=precio-descuento
    return preciofinal
#Función principal.
def main():
    precio=float(input("Introduce el precio del producto: ")) #Pide el precio del producto.
    #Devuelve el precio final del producto.
    print(f"El precio final del producto es: {PrecioFinal(precio,Descuento(precio))}") 

if __name__ == "__main__":
    main() 