
def cadena_sin_vocales(cadena:str, letter:str):
    for chr in cadena:
        if chr.lower() == letter.lower():
            break
        elif chr.lower() == "a":
            continue
        elif chr.lower() == "e":
            continue
        elif chr.lower() == "i":
            continue
        elif chr.lower() == "o":
            continue
        elif chr.lower() == "":
            continue
    print(chr, end="")
        
        
cadena_sin_vocales("Hola carlao", "z")