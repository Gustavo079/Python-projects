def madlib():
# # string concatenation (aka how to put strings together)
# # suppose we want to create a string that says "subscribe to _____ "
# youtuber = "Kylie Ying" # some string variable

    name = input("Ingresa tu nombre: ")
    age = int(input("age: "))

    if age < 18:
        hobby = input("hobby: ")
        madlib = f"Hola mi nombre es {name}, tengo {age} años y me gusta {hobby}\
            en mis ratos libres. trabajo como {trabajo} me gustav lo que hago,\
            creo que como todo me estreso algunas veces pero me agrada\
            lo que hago."
    else:
        place = input("place: ")
        Woman = input("woman: ")
        madlib = f"Hola {Woman}, te escribo esta carta desde {place}, la verdad\
            no ha sido facil para los dos esta situacion, aunque es una gran oportunidad\
            espero volver a vernos. Con cariño: {name}"
        
    print(madlib)