import time

print("¡Bienvenido al Sombrero Seleccionador de Hogwarts!")
name = input("Por favor, ingresa tu nombre: ")

def sorting_hat():
    slytherin = 0
    gryffindor = 0
    hufflepuff = 0
    ravenclaw = 0
    
    print("===================================================================================")
    print("\nResponde las siguientes preguntas para saber a qué casa perteneces en Hogwarts:\n")
    print("===================================================================================")
    
    create_questions = [
        {
            "pregunta": "\n 1-¿Cuáles de los siguientes adjetivos odiarías más que te digan los otros?:\n",
            "opciones": {
                'a': 'Ordinario',    # a) Slytherin
                'b': 'Ignorante',    # b) Ravenclaw
                'c': 'Cobarde',      # c) Gryffindor
                'd': 'Egoísta'       # d) Hufflepuff
            }
        },
        {
            "pregunta": "\n 2-¿Dada la elección, preferirías inventar una poción que garantizara?:\n",
            "opciones": {
                'a': 'Gloria',      # a) Gryffindor
                'b': 'Sabiduria',   # b) Ravenclaw
                'c': 'Amor',        # c) Hufflepuff
                'd': 'Poder'        # d) Slytherin
            }
        },
        {
            "pregunta": "\n 3-Es tarde y llega la noche. Caminas solo por la calle y de repente escuchas un peculiar grito que crees tiene una fuente mágica. ¿Qué harías?:\n",
            "opciones": {
                'a': 'Procedes con precaución manteniendo en mano tu varita oculta y completamente atento ante cualquier movimiento',  # a) Hufflepuff
                'b': 'Sacas tu varita y tratas de descubrir el origen del sonido',                                              # b) Gryffindor
                'c': 'Sacas tu varita y te mantienes firme',                                                                   # c) Slytherin
                'd': 'Te retiras a las sombras mientras repasas mentalmente los hechizos de ataque y defensa más apropiados'   # d) Ravenclaw
            }
        },
        {
            "pregunta": "\n 4-Usted entra en un jardín encantado. ¿Qué sería más curioso examinar primero?:\n",
            "opciones": {
                'a': 'Los árboles de hoja plateada que llevan manzanas de oro',                                      # a) Ravenclaw
                'b': 'Los hongos rojos gordos que parecen estar hablando el uno al otro',                            # b) Hufflepuff
                'c': 'La piscina burbujeante, en la cual algo luminoso en el fondo está haciendo un remolino',       # c) Slytherin
                'd': 'La estatua de un viejo mago con un extraño ojo centellante'                                    # d) Gryffindor
            }
        },
        {
            "pregunta": "\n 5-Un muggle se enfrenta a usted y dice que está seguro de que es una bruja o mago. ¿Qué haría en esa situación?:\n",
            "opciones": {
                'a': 'Preguntas: "¿Qué le hace pensar eso?"',                                             # a) Ravenclaw
                'b': 'Afirmas y preguntas si le gustaría una muestra gratuita de un maleficio',            # b) Slytherin
                'c': 'Afirmas y caminas lejos, dejando que se pregunte si usted está presumiendo',         # c) Gryffindor
                'd': 'Le dices que estás preocupado por su salud mental y te ofreces llevarlo a un médico'  # d) Hufflepuff
            }
        }
    ]

    

    for question in create_questions:
        print(question["pregunta"])
        for key, value in question["opciones"].items():
            print(f"{key}) {value}")
        respuesta = input("Ingresa tu opción: ")
        respuesta = respuesta.lower()

        while respuesta not in question["opciones"].keys():
            print("Opción inválida. Ingresa nuevamente.")
            respuesta = input("Ingresa tu opción: ")
            respuesta = respuesta.lower()

        if respuesta == "a":
            slytherin += 1
        elif respuesta == "b":
            ravenclaw += 1
        elif respuesta == "c":
            gryffindor += 1
        elif respuesta == "d":
            hufflepuff += 1

    print("\n Hmmmmm...")
    time.sleep(1)
    print("\n Creo...")
    time.sleep(1)
    print("\n Que podrías encajar en...")
    time.sleep(1)

    if slytherin > gryffindor and slytherin > hufflepuff and slytherin > ravenclaw:
        casa = "Slytherin"
    elif gryffindor > slytherin and gryffindor > hufflepuff and gryffindor > ravenclaw:
        casa = "Gryffindor"
    elif hufflepuff > slytherin and hufflepuff > gryffindor and hufflepuff > ravenclaw:
        casa = "Hufflepuff"
    else:
        casa = "Ravenclaw"

    print("¡El Sombrero Seleccionador ha decidido que " + name + " pertenece a la casa " + casa + "!")

sorting_hat()
