""" 
 Reto #1
 ¿ES UN ANAGRAMA?
 Dificultad: MEDIA

 Enunciado: Escribe una función que reciba dos palabras (String) y retorne verdadero o falso
 (Boolean) según sean o no anagramas.
 Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
 NO hace falta comprobar que ambas palabras existan.
 Dos palabras exactamente iguales no son anagrama.
"""

def Anagram(first_word, second_word):
    return first_word.lower() == second_word.lower()[::-1]

def AnagramV2(first_word, second_word):
    semi_word = ""
    for i in reversed(first_word):
        semi_word += i
    return semi_word.upper() == second_word.upper()

print(Anagram("Amor", "Roma"))
print(AnagramV2("Amor", "Roma"))