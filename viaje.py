
#Función del coste del trayecto.
def trayecto(alumnos):
    
    if alumnos <=25:#Si hay 25 o menos alumnos.
        precio_trayecto = 67.5*alumnos
        return precio_trayecto
    
    elif alumnos >25:#Si hay más de 25 alumnos.
        precio_trayecto =  61 *alumnos
        return precio_trayecto
    
#Función del coste de la comida.
def comida(alumnos,dias):
    total_comida = alumnos*dias*3.5
    return total_comida 

#Función del coste del alojamiento.
def alojamiento(alumnos,dias):    

    if alumnos <=30:
        total_alojamiento = alumnos*dias*4.75
        return total_alojamiento
    
    elif 31<=alumnos<35:
        total_alojamiento = alumnos*dias*4
        return total_alojamiento
    
    else:
        total_alojamiento = alumnos*dias*3.5
        return total_alojamiento
 #Función del coste total del viaje.
def TotalViaje(alumnos,dias):

    total_trayecto = trayecto(alumnos)
    
    total_comida = comida(alumnos,dias)
    
    total_alojamiento = alojamiento(alumnos,dias)
    #Calculamos el total del viaje.
    total_viaje = total_trayecto + total_comida + total_alojamiento
    
    return total_viaje

def main():
    
    alumnos=int(input("Ingrese la cantidad de alumnos: "))
    dias=int(input("Ingrese la cantidad de dias: "))

    total_viaje = TotalViaje(alumnos,dias)
    print(f"El precio total del viaje son {total_viaje}€")

    viaje_por_alumno = total_viaje/alumnos
    print(f"El precio por alumno es de {viaje_por_alumno}€")

if __name__ == "__main__":
    main()
    