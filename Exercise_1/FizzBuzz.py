"""
/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */
"""

# Definición de una función llamada "fizzbuzz" sin argumentos.
def fizzbuzz():
    
    # Ciclo for que recorre los números del 1 al 100 (incluyendo el 1 y el 100).
    for i in range(0,101):
        
        # Si el número es divisible por 15 (múltiplo de 3 y 5 a la vez),
        # imprime "fizzbuzz".
        if i % 15==0:
            print("fizzbuzz") 
            
        # Si el número es divisible por 3 (pero no por 15),
        # imprime "fizz".
        elif i % 3==0:
            print("fizz")
        
        # Si el número es divisible por 5 (pero no por 15),
        # imprime "buzz".   
        elif i % 5==0:
            print("buzz")
            
        # Si el número no es divisible ni por 3, ni por 5, ni por 15,
        # simplemente imprime el número en sí.   
        else:
            print(i)
            
# Llamada a la función "fizzbuzz" para ejecutarla
fizzbuzz()        
    