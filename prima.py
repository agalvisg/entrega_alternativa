def calcular_prima(kilometros, accidentes, años_servicio):
    # Calcular el prima por distancia
    prima_distancia = min(kilometros * 0.01, 400)

    # Calcular la prima por antigüedad
    prima_por_antiguedad = 0
    if años_servicio >= 4:
        prima_por_antiguedad= 200 + (años_servicio - 4) * 20

    # Calcular la prima total
    if accidentes == 0:
        prima_total = prima_distancia + prima_por_antiguedad
    elif accidentes == 1:
        prima_total = (prima_distancia + prima_por_antiguedad) / 2
    elif accidentes == 2:
        prima_total = (prima_distancia + prima_por_antiguedad) / 3
    elif accidentes == 3:
        prima_total = (prima_distancia + prima_por_antiguedad) / 4
    else:
        prima_total = 0

    return prima_total

def main():
    # leer los datos de entrada
    kilometros = float(input("Enter the number of kilometers driven: "))
    accidentes = int(input("Enter the number of accidents: "))
    años_servicio = int(input("Enter the number of years of service: "))

    # Calcular la prima
    prima = calcular_prima(kilometros, accidentes, años_servicio)

    # output del resultado
    print(f"La prima anual para el conductor son: {prima} €")