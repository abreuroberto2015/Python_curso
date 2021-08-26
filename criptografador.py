def cripto(frase):
    tradutor = ""
    for letra in frase:
        if letra in "Aa": tradutor = tradutor + "1"
        elif letra in "Bb": tradutor = tradutor + "2"
        elif letra in "Cc": tradutor = tradutor + "3"
        elif letra in "Dd": tradutor = tradutor + "4"
        elif letra in "Ee": tradutor = tradutor + "5"
        elif letra in "Ff": tradutor = tradutor + "6"
        elif letra in "Gg": tradutor = tradutor + "7"
        elif letra in "Hh": tradutor = tradutor + "8"
        elif letra in "Ii": tradutor = tradutor + "9"
        elif letra in "Jj": tradutor = tradutor + "10"
        elif letra in "Kk": tradutor = tradutor + "11"
        elif letra in "Ll": tradutor = tradutor + "12"
        elif letra in "Mm": tradutor = tradutor + "13"
        elif letra in "Nn": tradutor = tradutor + "14"
        elif letra in "Oo": tradutor = tradutor + "15"
        elif letra in "Pp": tradutor = tradutor + "16"
        elif letra in "Qq": tradutor = tradutor + "17"
        elif letra in "Rr": tradutor = tradutor + "18"
        elif letra in "Ss": tradutor = tradutor + "19"
        elif letra in "Tt": tradutor = tradutor + "20"
        elif letra in "Uu": tradutor = tradutor + "21"
        elif letra in "Vv": tradutor = tradutor + "22"
        elif letra in "Ww": tradutor = tradutor + "23"
        elif letra in "Xx": tradutor = tradutor + "24"
        elif letra in "Yy": tradutor = tradutor + "25"
        elif letra in "Zz": tradutor = tradutor + "26"
        else: tradutor = tradutor + letra
    return tradutor
            
print(cripto(input("Digite sua frase:")))