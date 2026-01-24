import random
import data
import os

def limpiar_consola():
    os.system("cls" if os.name == "nt" else "clear")

titulo = 'APRENDIENDO INGLES USANDO PYTHON'        

msg1 = """Para comenzar la practica digita el número de en que idioma quieres que las palabras sean dispuestas, es decir, si se escoge Ingles las palabras apareceran en Ingles y deberas digitarlas en Español y viceversa, 
si se escoge aleatorio se entregaran en ambos idiomas y deberas digitar la traduccion del idioma entregado:
0. Aleatorio
1. Ingles
2. Español
"""
msg2 = "\nEscoja el número si desea que las palabras que aparezcan sean de una categoria en especial, en caso de que quiera que sean de cualquier categoria escoja aleatorio: "

msg3 = "Para comenzar el reto oprima enter o cualquier tecla..."


print(f"{titulo.center(200, '=')}")
print(msg1)

select_language = int(input("Digite el número del idioma escogido: " ))
dict_select_lang = {0: "Aleatorio", 1:"Ingles", 2:"Español"}
limpiar_consola()

print(f"{titulo.center(200, '=')}")
print(f"Se escogio recibir las palabras en {dict_select_lang[select_language]} \n")

dict_select_ctg = {0: 'Aleatorio'}
cont = 1
print(f"{0}. {'Aleatorio'}")
for l in data.learning_english:
    dict_select_ctg[cont] = l
    print(f'{cont}. {l}')
    cont+=1

select_category = int(input(f"{msg2}"))
digit_value = input(f"\n\n{msg3}")
limpiar_consola()


extract_dict = data.learning_english[dict_select_ctg[select_category]]


puntaje = 0
errada = 0

while digit_value != "Q":
    print(f"{titulo.center(200, '=')}")
    print(f"Las palabras apareceran de la categoria {dict_select_ctg[select_category]} \n")
    print(f"--->Puntaje = {puntaje}")
    print(f"--->Errores: {errada}")
    print(f"\nDigite la palabra traducida, si quiere salir digite (Q)...")

    if select_language == 1:
        palabra = random.choice(list(extract_dict.keys()))
        for intento in range(4):
            digit_value = input(f"{palabra}:\t")
            digit_value = digit_value.title()
            if digit_value == "Q": break
            if extract_dict[palabra] == digit_value:
                if intento == 0:
                    puntaje+=1
                elif intento == 1:
                    puntaje+=0.5
                elif intento == 2:
                    puntaje+=0
                break
            else:
                errada+=1
        limpiar_consola()

    elif select_language == 2:
        palabra = random.choice(list(extract_dict.values()))
        k = [key for (key, value) in extract_dict.items() if value == palabra][0]
        for intento in range(4):
            digit_value = input(f"{palabra}:\t")
            digit_value = digit_value.title()
            if digit_value == "Q": break
            if k == digit_value:
                if intento == 0:
                    puntaje+=1
                elif intento == 1:
                    puntaje+=0.5
                elif intento == 2:
                    puntaje+=0
                break
            else:
                errada+=1
        limpiar_consola()

    else:
        palabra_tup = random.choice(list(extract_dict.items()))
        palabra = random.choice(palabra_tup)
        digit_value = input(f"{palabra}:\t")
        digit_value = digit_value.title()
        for intento in range(4):
            digit_value = input(f"{palabra}:\t")
            digit_value = digit_value.title()
            if digit_value == "Q": break
            if palabra == palabra_tup[0]:
                if digit_value == palabra_tup[1]:
                    if intento == 0:
                        puntaje+=1
                    elif intento == 1:
                        puntaje+=0.5
                    elif intento == 2:
                        puntaje+=0
                    break
                else:
                    errada+=1
            else:
                if digit_value == palabra_tup[0]:
                    if intento == 0:
                        puntaje+=1
                    elif intento == 1:
                        puntaje+=0.5
                    elif intento == 2:
                        puntaje+=0
                    break
                else:
                    errada+=1
        limpiar_consola()







# def choose():
# choose()