class Nota():
    
    @staticmethod
    def notas_en_rango(nota_1,nota_2,nota_3,nota_4):
        #Se asegura que las notas estén en el rango de 0 a 20.

        if nota_1 not in range(0,21):
            print("Nota 1 no válida")
            return nota_1
        elif nota_2 not in range(0,21):
            print("Nota 2 no válida")
            return nota_2
        elif nota_3 not in range(0,21):
            print("Nota 3 no válida")
            return nota_3
        elif nota_4 not in range(0,21):
            print("Nota 4 no válida")
            return nota_4
        else:
            return nota_1,nota_2,nota_3,nota_4
        
    @staticmethod
    def media(nota_1,nota_2,nota_3,nota_4):
        nota_media = float (nota_1 + nota_2 + nota_3 + nota_4) / 4
        return nota_media


def evaluacion(nota_media):

    if nota_media in range(0,21): #Se asegura que la nota esté en el rango de 0 a 20
        if nota_media>=15: 
            print(f"Alumno con talento, su nota media es de {nota_media}")
            
        elif 12<=nota_media<15:
            print(f"Con capacidad, su nota media es de {nota_media}")
                    
        elif nota_media<12:
            print(f"Debe reorientarse, su nota media es de {nota_media}")
        
    else: #Si la nota no se encuentra en el rango devuelve 
        print(f"Notas no válidas, la media de {nota_media} no es válida.")
        return main()
    
def main():

    nota_1 = float(input("Introduce la nota 1: "))
    Nota.notas_en_rango(nota_1,0,0,0)
    nota_2 = float(input("Introduce la nota 2: "))
    Nota.notas_en_rango(0,nota_2,0,0)
    nota_3 = float(input("Introduce la nota 3: "))
    Nota.notas_en_rango(0,0,nota_3,0)
    nota_4 = float(input("Introduce la nota 4: "))
    Nota.notas_en_rango(0,0,0,nota_4)

    nota_media = Nota.media(nota_1,nota_2,nota_3,nota_4)
    evaluacion(nota_media)

if __name__ == "__main__":
    main()