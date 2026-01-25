import random
from data import learning_english, dict_select_lang, dict_select_diff, dict_select_diff_text, dict_select_ctg
import os
import messages
from categories import choosen_category, extract_deep_categories
from stats import score_assignment


def limpiar_consola():
    os.system("cls" if os.name == "nt" else "clear")


print(f"\n{messages.titulo.center(200, '=')} \n{messages.msg1}")
select_language = int(input(messages.msg2))
limpiar_consola()


#=======================================================================================================================================================================
print(f"{messages.titulo.center(200, '=')}")
print(f"Se escogio recibir las palabras en idioma {dict_select_lang[select_language]} \n{messages.msg3}")
select_difficulty = int(input(messages.msg4))
if select_difficulty == 0:
    select_difficulty2 = int(input(messages.msg5))
else:
    select_difficulty2 = random.choice(dict_select_diff[select_difficulty])
limpiar_consola()


#=======================================================================================================================================================================
print(f"{messages.titulo.center(200, '=')}")
print(f"Se escogio recibir las palabras en idioma {dict_select_lang[select_language]} ")
print(f"Se escogio recibir una cantidad de {select_difficulty2} palabras, correspondientes a un nivel {dict_select_diff_text[select_difficulty]} \n")
select_category = choosen_category(learning_english, dict_select_ctg)
extract_dict, extract_irregulars, select_irregulars = extract_deep_categories(learning_english, dict_select_ctg, select_category) 
digit_value = input(f"\n\n{messages.msg7}")
limpiar_consola()


#=======================================================================================================================================================================
puntaje = 0
correctas = 0
errada = 0
ciclos = 0
infinitive = ""
past_simple = ""
past_participle = ""
irregulars_items = []

while digit_value != "Q" and infinitive != "Q" and past_simple != "Q" and past_participle != "Q" and ciclos < select_difficulty2:
    print(f"{messages.titulo.center(200, '=')}")
    print(f"Se escogio recibir las palabras en idioma {dict_select_lang[select_language]} ")
    print(f"Se escogio recibir una cantidad de {select_difficulty2} palabras, correspondientes a un nivel {dict_select_diff_text[select_difficulty]} ")
    if dict_select_ctg[select_category] == "List of Irregular Verbs" and select_irregulars == 0:
        print(f"Las palabras apareceran de la categoria {dict_select_ctg[select_category]} con todos los verbos irregulares\n")
    elif dict_select_ctg[select_category] == "List of Irregular Verbs" and select_irregulars == 1:
        print(f"Las palabras apareceran de la categoria {dict_select_ctg[select_category]} con cada tiempo verbal\n")
    else:
        print(f"Las palabras apareceran de la categoria {dict_select_ctg[select_category]} \n")
    print(f"--->Puntaje: {puntaje}")
    print(f"--->Errores: {errada}")
    print(f"\nDigite la palabra traducida, si sale un numero en Ingles para ponerlo en español solo ponga el numero en decimales y entre comilas "", si quiere salir digite (Q)...")

    if select_language == 1:
        if dict_select_ctg[select_category] == "List of Irregular Verbs" and select_irregulars == 1:
            irregulars_random = random.choice(extract_irregulars)
            irregulars_items = list(irregulars_random.items())
        else:
            palabra = random.choice(list(extract_dict.keys()))

        for intento in range(4):
            if dict_select_ctg[select_category] == "List of Irregular Verbs" and select_irregulars == 1:
                inf = "INFINITIVE"; p_simple = "PAST SIMPLE"; p_participle = "PAST PARTICIPLE"
                print(f"\n||{inf:^50}||{p_simple:^50}||{p_participle:^50}||")
                print(f"||{irregulars_items[0][0]:<10}: {'':<38}||{irregulars_items[1][0]:<10}: {'':<38}||{irregulars_items[2][0]:<10}: {'':<38}||")
                infinitive = input('Ingrese la traduccion del infinitivo: '); 
                infinitive = infinitive.title()
                if infinitive == "Q": break                
                print(f"\n||{irregulars_items[0][0]:<10}: {infinitive:<38}||{irregulars_items[1][0]:<10}: {'':<38}||{irregulars_items[2][0]:<10}: {'':<38}||")
                past_simple = input('Ingrese la traduccion del past simple: '); 
                past_simple = past_simple.title()
                if past_simple == "Q": break
                print(f"\n||{irregulars_items[0][0]:<10}: {infinitive:<38}||{irregulars_items[1][0]:<10}: {past_simple:<38}||{irregulars_items[2][0]:<10}: {'':<38}||")
                past_participle = input('Ingrese la traduccion del past participle: '); 
                past_participle = past_participle.title()
                if past_participle == "Q": break
                print(f"\n||{irregulars_items[0][0]:<10}: {infinitive:<38}||{irregulars_items[1][0]:<10}: {past_simple:<38}||{irregulars_items[2][0]:<10}:   {past_participle:<38}||")
                ok, puntaje, correctas, errada = score_assignment(1, infinitive, past_simple, past_participle, irregulars_items, intento, extract_dict, palabra, "", puntaje, correctas, errada)
                if ok: break
                # if infinitive == irregulars_items[0][1] and past_simple == irregulars_items[1][1] and past_participle == irregulars_items[2][1]:
                #     if intento == 0:
                #         puntaje+=1
                #         correctas+=1
                #     elif intento == 1:
                #         puntaje+=0.5
                #         correctas+=0
                #     elif intento == 2:
                #         puntaje+=0
                #         correctas+=0
                #     break
                # else:
                #     errada+=1
                #     print(f"\nAlguna quedo incorrecta, REPITE¡¡¡......")            
            else:
                digit_value = input(f"{palabra}:\t")
                digit_value = digit_value.title()
                if digit_value == "Q": break
                ok, puntaje, correctas, errada = score_assignment(2, "", "", "", [], intento, extract_dict, palabra, digit_value, puntaje, correctas, errada)
                if ok: break
                # if extract_dict[palabra] == digit_value:
                #     if intento == 0:
                #         puntaje+=1
                #         correctas+=1
                #     elif intento == 1:
                #         puntaje+=0.5
                #         correctas+=0
                #     elif intento == 2:
                #         puntaje+=0
                #         correctas+=0
                #     break
                # else:
                #     errada+=1
        limpiar_consola()

    elif select_language == 2:
        if dict_select_ctg[select_category] == "List of Irregular Verbs" and select_irregulars == 1:
            irregulars_random = random.choice(extract_irregulars)
            irregulars_items = list(irregulars_random.items())
        else:
            palabra = random.choice(list(extract_dict.values()))

        for intento in range(4):
            if digit_value == "Q": break
            if dict_select_ctg[select_category] == "List of Irregular Verbs" and select_irregulars == 1:
                inf = "INFINITIVE"; p_simple = "PAST SIMPLE"; p_participle = "PAST PARTICIPLE"
                print(f"\n||{inf:^50}||{p_simple:^50}||{p_participle:^50}||")
                print(f"||{irregulars_items[0][1]:<10}: {'':<38}||{irregulars_items[1][1]:<10}: {'':<38}||{irregulars_items[2][1]:<10}: {'':<38}||")
                infinitive = input('Ingrese la traduccion del infinitivo: ')
                infinitive = infinitive.title()
                if infinitive == "Q": break                  
                print(f"\n||{irregulars_items[0][1]:<10}: {infinitive:<38}||{irregulars_items[1][1]:<10}: {'':<38}||{irregulars_items[2][1]:<10}: {'':<38}||")
                past_simple = input('Ingrese la traduccion del past simple: ')
                past_simple = past_simple.title()
                if past_simple == "Q": break  
                print(f"\n||{irregulars_items[0][1]:<10}: {infinitive:<38}||{irregulars_items[1][1]:<10}: {past_simple:<38}||{irregulars_items[2][1]:<10}: {'':<38}||")
                past_participle = input('Ingrese la traduccion del past participle: ')
                past_participle = past_participle.title()
                if past_participle == "Q": break  
                print(f"\n||{irregulars_items[0][1]:<10}: {infinitive:<38}||{irregulars_items[1][1]:<10}: {past_simple:<38}||{irregulars_items[2][1]:<10}:   {past_participle:<38}||")
                if infinitive == irregulars_items[0][0] and past_simple == irregulars_items[1][0] and past_participle == irregulars_items[2][0]:
                    if intento == 0:
                        puntaje+=1
                        correctas+=1
                    elif intento == 1:
                        puntaje+=0.5
                        correctas+=0
                    elif intento == 2:
                        puntaje+=0
                        correctas+=0
                    break
                else:
                    errada+=1
                    print(f"\nAlguna quedo incorrecta, REPITE¡¡¡......")            
            else:
                k = [key for (key, value) in extract_dict.items() if value == palabra][0]
                for intento in range(4):
                    digit_value = input(f"{palabra}:\t")
                    digit_value = digit_value.title()
                    if digit_value == "Q": break
                    ok, puntaje, correctas, errada = score_assignment(2, "", "", "", [], intento, k, palabra, digit_value, puntaje, correctas, errada)
                    if ok: break
                    # if k == digit_value:
                    #     if intento == 0:
                    #         puntaje+=1
                    #         correctas+=1
                    #     elif intento == 1:
                    #         puntaje+=0.5
                    #         correctas+=0
                    #     elif intento == 2:
                    #         puntaje+=0
                    #         correctas+=0
                    #     break
                    # else:
                    #     errada+=1
        limpiar_consola()

    else:
        if dict_select_ctg[select_category] == "List of Irregular Verbs" and select_irregulars == 1:
            irregulars_random = random.choice(extract_irregulars)
            irregulars_items = list(irregulars_random.items())
            position_irregulars = random.choice(list(range(0,2)))
            print(position_irregulars)
            tradu_ir = 1 if position_irregulars == 0 else 0
            print(tradu_ir)
        else:
            palabra_tup = random.choice(list(extract_dict.items()))
            palabra = random.choice(palabra_tup)

        for intento in range(4):
            if digit_value == "Q": break
            if dict_select_ctg[select_category] == "List of Irregular Verbs" and select_irregulars == 1:
                inf = "INFINITIVE"; p_simple = "PAST SIMPLE"; p_participle = "PAST PARTICIPLE"
                print(f"\n||{inf:^50}||{p_simple:^50}||{p_participle:^50}||")
                print(f"||{irregulars_items[0][position_irregulars]:<10}: {'':<38}||{irregulars_items[1][position_irregulars]:<10}: {'':<38}||{irregulars_items[2][position_irregulars]:<10}: {'':<38}||")
                infinitive = input('Ingrese la traduccion del infinitivo: ')
                infinitive = infinitive.title()
                if infinitive == "Q": break                  
                print(f"\n||{irregulars_items[0][position_irregulars]:<10}: {infinitive:<38}||{irregulars_items[1][position_irregulars]:<10}: {'':<38}||{irregulars_items[2][position_irregulars]:<10}: {'':<38}||")
                past_simple = input('Ingrese la traduccion del past simple: ')
                past_simple = past_simple.title()
                if past_simple == "Q": break  
                print(f"\n||{irregulars_items[0][position_irregulars]:<10}: {infinitive:<38}||{irregulars_items[1][position_irregulars]:<10}: {past_simple:<38}||{irregulars_items[2][position_irregulars]:<10}: {'':<38}||")
                past_participle = input('Ingrese la traduccion del past participle: ')
                past_participle = past_participle.title()
                if past_participle == "Q": break  
                print(f"\n||{irregulars_items[0][position_irregulars]:<10}: {infinitive:<38}||{irregulars_items[1][position_irregulars]:<10}: {past_simple:<38}||{irregulars_items[2][position_irregulars]:<10}:   {past_participle:<38}||")
                if infinitive == irregulars_items[0][tradu_ir] and past_simple == irregulars_items[1][tradu_ir] and past_participle == irregulars_items[2][tradu_ir]:
                    if intento == 0:
                        puntaje+=1
                        correctas+=1
                    elif intento == 1:
                        puntaje+=0.5
                        correctas+=0
                    elif intento == 2:
                        puntaje+=0
                        correctas+=0
                    break
                else:
                    errada+=1
                    print(f"\nAlguna quedo incorrecta, REPITE¡¡¡......")            
            else:
                digit_value = input(f"{palabra}:\t")
                digit_value = digit_value.title()
                if digit_value == "Q": break
                if palabra == palabra_tup[0]:
                    ok, puntaje, correctas, errada = score_assignment(3, "", "", "", [], intento, digit_value, palabra, palabra_tup[1], puntaje, correctas, errada)
                    if ok: break
                    # if digit_value == palabra_tup[1]:
                    #     if intento == 0:
                    #         puntaje+=1
                    #         correctas+=1
                    #     elif intento == 1:
                    #         puntaje+=0.5
                    #         correctas+=0
                    #     elif intento == 2:
                    #         puntaje+=0
                    #         correctas+=0
                    #     break
                    # else:
                    #     errada+=1
                else:
                    ok, puntaje, correctas, errada = score_assignment(3, "", "", "", [], intento, digit_value, palabra, palabra_tup[0], puntaje, correctas, errada)
                    if ok: break
                    # if digit_value == palabra_tup[0]:
                    #     if intento == 0:
                    #         puntaje+=1
                    #         correctas+=1
                    #     elif intento == 1:
                    #         puntaje+=0.5
                    #         correctas+=0
                    #     elif intento == 2:
                    #         puntaje+=0
                    #         correctas+=0
                    #     break
                    # else:
                    #     errada+=1
    ciclos+=1
    limpiar_consola()

print(f"Puntaje obtenido: {puntaje}")
print(f"Número de aciertos: {correctas}")
print(f"Numero de errores: {errada}")
print(f"Tu puntaje final es de: {(correctas/select_difficulty2)*100}% para el nivel {dict_select_diff_text[select_difficulty]}")



# def choose():
# choose()