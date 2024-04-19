from enum import Enum

class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7
 
    #método que devuelve el día siguiente    
    def sucesor(self):
        
        #Primer día es lunes
        first_day=Weekday.MONDAY.value 

        #Calculamos la diferencia entre el día actual y el primer día
        diferencia = (self.value - first_day) %7
        
        #Calculamos el día siguiente
        siguiente = (self.value +(7-diferencia))%7 +1
        
        return Weekday(siguiente)
    
    def __str__(self):
        return self.name

def main():
    #se pide al usuario que introduzca un día de la semana
    day=input("Introduce un día de la semana: ").upper()    
    
    #se transforma el día a un valor numérico
    current_day = Weekday[day]
    print(f"Hoy es {current_day}")

    #se calcula el día siguiente
    next_day = current_day.sucesor()
    print(f"Mañana será {next_day}")

if __name__ == "__main__":
    main()

    