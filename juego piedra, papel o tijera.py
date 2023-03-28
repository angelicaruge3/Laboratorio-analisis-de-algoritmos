 #importar libreria
 import random
 #opciones
 op=("piedra", "papel", "tijera")
 #estructura while
 while True:
    #entradas
    usuario=input("digite la opcion piedra, papel o tijera:  ")
    cpu=random.choice(op)
    #imprimir informacion
    print(f"la op que digito el usuario es: {usuario}")
    print(f"la op CPU es: {cpu}")
    #proceso
    if usuario == "piedra" and cpu=="piedra":
        print("empate!!!")
    elif usuario == "tijera" and cpu=="tijera":
        print("empate!!!")
    elif usuario == "papel" and cpu=="papel":
        print("empate!!!")
    elif usuario == "piedra" and cpu=="papel":
        print("gana cpu!!!")
    elif usuario == "piedra" and cpu=="tijera":
        print("gana usuario!!!")
    elif usuario == "papel" and cpu=="piedra":
        print("gana usuario!!!")
    elif usuario == "papel" and cpu=="tijera":
        print("gana cpu!!!")
    elif usuario == "tijera" and cpu=="piedra":
        print("gana cpu!!!")
    elif usuario == "tijera" and cpu=="papel":
        print("gana usuario!!!")
    else:
        print("Error!!!")

    play_again == input("quieres jugar de nuevo (s/n): ")
    if play_again.lower() != "s":
        break

    
    