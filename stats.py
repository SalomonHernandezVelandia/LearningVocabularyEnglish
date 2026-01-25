def score_assignment(d, infinitive, past_simple, past_participle, irregulars_items, intento, extract_dict, palabra, digit_value, puntaje, correctas, errada):
    if d == 1:
        if infinitive == irregulars_items[0][1] and past_simple == irregulars_items[1][1] and past_participle == irregulars_items[2][1]:
            if intento == 0:
                puntaje+=1
                correctas+=1
            elif intento == 1:
                puntaje+=0.5
                correctas+=0
            elif intento == 2:
                puntaje+=0
                correctas+=0
            return True, puntaje, correctas, errada
        else:
            errada+=1
            print(f"\nAlguna quedo incorrecta, REPITE¡¡¡......")    
            return False, puntaje, correctas, errada
    elif d == 2:
        if extract_dict[palabra] == digit_value:
            if intento == 0:
                puntaje+=1
                correctas+=1
            elif intento == 1:
                puntaje+=0.5
                correctas+=0
            elif intento == 2:
                puntaje+=0
                correctas+=0
            return True, puntaje, correctas, errada
        else:
            errada+=1
            return False, puntaje, correctas, errada
    else:
        if extract_dict == digit_value:
            if intento == 0:
                puntaje+=1
                correctas+=1
            elif intento == 1:
                puntaje+=0.5
                correctas+=0
            elif intento == 2:
                puntaje+=0
                correctas+=0
            return True, puntaje, correctas, errada
        else:
            errada+=1
            return False, puntaje, correctas, errada