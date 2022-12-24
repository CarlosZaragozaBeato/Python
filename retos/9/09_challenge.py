"""
  Reto #9
  CÓDIGO MORSE
  Fecha publicación enunciado: 02/03/22
  Fecha publicación resolución: 07/03/22
  Dificultad: MEDIA
 
  Enunciado: Crea un programa que sea capaz de transformar texto natural a código morse y viceversa.
  - Debe detectar automáticamente de qué tipo se trata y realizar la conversión.
  - En morse se soporta raya "—", punto ".", un espacio " " entre letras o símbolos y dos espacios entre palabras "  ".
  - El alfabeto morse soportado será el mostrado en https://es.wikipedia.org/wiki/Código_morse.
 """
 
def to_morse(string):
  print(string.find('ch'))
  valor = ""
  for i in range(len(string)):                               
    if string[i].lower() =='a':
      valor +=(".- ")
    elif string[i].lower() =='b':
      valor += "-... "
    elif string[i].lower() =='c':
      valor +=("-.-. ")
    elif string[i].lower() =='d':
      valor += "-.. " 
    elif string[i].lower() =='e':
      valor += ". "
    elif string[i].lower() =='f':
      valor += "..-. "
    elif string[i].lower() =='g':
      valor += "--. "
    elif string[i].lower() =='h':
      valor += ".... "
    elif string[i].lower() =='i':
      valor += ".. "
    elif string[i].lower() =='j':
      valor += ".--- "
    elif string[i].lower() =='k':
      valor += "-.- "
    elif string[i].lower() =='l':
      valor += ".-.. "
    elif string[i].lower() =='m':
      valor += "-- "
    elif string[i].lower() =='n':
      valor += "-. "
    elif string[i].lower() =='ñ':
      valor += "--.- "
    elif string[i].lower() =='o':
      valor += "--- "
    elif string[i].lower() =='p':
      valor += ".--. "
    elif string[i].lower() =='q':
      valor += "--.- "
    elif string[i].lower() =='r':
      valor += ".-. "
    elif string[i].lower() =='s':
      valor += "... "
    elif string[i].lower() =='t':
      valor += "-"
    elif string[i].lower() =='u':
      valor += "..- "
    elif string[i].lower() =='v':
      valor += "...- "
    elif string[i].lower() =='w':
      valor += ".--..-.-.- "
    elif string[i].lower() =='x':
      valor += "-..---..--"
    elif string[i].lower() =='y':
      valor += "-.--..--.."
    elif string[i].lower() =='z':
      valor += "--.. "
  return valor
      
print(to_morse("carlos"))

