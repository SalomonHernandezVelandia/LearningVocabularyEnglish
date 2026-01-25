import messages


def choosen_category(learning_english, dict_select_ctg):
    cont = 1
    print(f"{0}. {'Aleatorio'}")

    for l in learning_english:
        dict_select_ctg[cont] = l
        print(f'{cont}. {l}')
        cont+=1
    select_category = int(input(f"{messages.msg6}"))

    return select_category



def extract_deep_categories(learning_english, dict_select_ctg, select_category):
    extract_dict = {}
    extract_irregulars = []
    select_irregulars = 0

    tipo = 0 if dict_select_ctg[select_category] == "Aleatorio" else learning_english[dict_select_ctg[select_category]] 

    if dict_select_ctg[select_category] == "Aleatorio":
        for unpacking in learning_english:
            if isinstance(learning_english[unpacking], list):
                for unpacking_list_lv2 in learning_english[unpacking]:
                    for unpacking_list_lv3 in unpacking_list_lv2:
                        if isinstance(unpacking_list_lv2[unpacking_list_lv3], dict):
                            for unpacking_list_lv4 in unpacking_list_lv2[unpacking_list_lv3]:
                                extract_dict = extract_dict | unpacking_list_lv2[unpacking_list_lv3][unpacking_list_lv4]
                        else:
                            extract_dict = extract_dict | unpacking_list_lv2
            else:
                extract_dict = extract_dict | learning_english[unpacking]
            print(extract_dict)

    elif dict_select_ctg[select_category] == "List of Irregular Verbs": 
        print(f"\n\n{messages.msg8} \n{messages.msg9} \n")
        select_irregulars = int(input(messages.msg10))
        if select_irregulars == 0:
            for irr in learning_english['List of Irregular Verbs']:
                extract_dict = extract_dict | irr
                # print(extract_dict)
        else:
            extract_irregulars = learning_english[dict_select_ctg[select_category]]

    else:
        # Nivel 2
        if isinstance(tipo, dict):
            extract_dict = learning_english[dict_select_ctg[select_category]]
        else:
            # Nivel3
            for des in learning_english[dict_select_ctg[select_category]]:
                type_search_deep = list(des.items())
                if isinstance(type_search_deep[0][1], dict):
                    # Nivel4
                    for des_lv3 in type_search_deep[0][1]:
                        extract_dict = extract_dict | type_search_deep[0][1][des_lv3]
                else:
                    #Nivel3
                    extract_dict = extract_dict | des 

    return extract_dict, extract_irregulars, select_irregulars

