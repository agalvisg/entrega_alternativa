def calculate_discount(num_children):
    if num_children == 2:
        discount = 0.10
    elif num_children == 3:
        discount = 0.15
    elif num_children == 4:
        discount = 0.18
    elif num_children >= 5:
        discount = 0.19 + (num_children - 5) * 0.01
    else:
        discount = 0.0

    return discount

def main():
    cantidad_niños=int(input("Ingrese la cantidad de niños: "))

    if cantidad_niños>=2:
        descuento=calculate_discount(cantidad_niños)
        print(f"El descuento para una familia con {cantidad_niños} niños es de: {descuento*100}%")

    else:
        print("No hay descuento")

if __name__ == "__main__":
    main()