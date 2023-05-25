# /*
#  * Crea una función que sea capaz de detectar si existe un viernes 13
#  * en el mes y el año indicados.
#  * - La función recibirá el mes y el año y retornará verdadero o falso.
#  */

import datetime

def exits_friday_13(year: int, month: int):
    """
    Verifica si existe un viernes 13 en el mes y año indicados.

    Args:
        year (int): Año.
        month (int): Mes.

    Returns:
        None
    """
    date = datetime.datetime(year, month, 13) # Crea un objeto datetime para el 13 del mes y año indicados
    
    if date.weekday() == 4:             # Comprueba si el día de la semana es viernes (0: lunes, 1: martes, ..., 4: viernes)
        print('This month has a Friday 13th')   # Imprime el mensaje indicando que hay un viernes 13
    else:
        print('This month does not have a Friday 13th') # Imprime el mensaje indicando que no hay un viernes 13

if __name__ == "__main__":
    print("Please enter the year and month to check if this month has a Friday 13th")  
    year = int(input("Year: ")) # Solicita al usuario que ingrese el año y lo guarda en la variable "year"
    month = int(input("Month: "))# Solicita al usuario que ingrese el mes y lo guarda en la variable "month"
    exits_friday_13(year, month)    # Llama a la función "exits_friday_13" pasando el año y mes ingresados