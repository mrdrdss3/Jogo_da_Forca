import random

def escolher_palavra(lista_de_animais):
  indice = random.randint(0, len(lista_de_animais)-1)
  palavra_escolhida = lista_de_animais[indice]

  return(palavra_escolhida)

def identificando_letras(lista_de_animais):
  chances = 6
  certo = 0
  lista_letras_erradas = ""
  tem_a_letra= 0
  palavra = escolher_palavra(lista_de_animais)
  advinha_palavra = []
  
  print("tente adivinhar a palavra!")
  print(" ")

  for letra in range(0, len(palavra)):
    advinha_palavra.append("_")
  
  for i in range(0, len(advinha_palavra)):
    print(advinha_palavra[i], end = " ")
    
  print(" ")
  print(" ")

  while chances > 0:
    letra_escolhida = input("Escolha uma letra: ")
    print(" ")
    
    for i in range(0, len(palavra)):
      if letra_escolhida == palavra[i]:
        advinha_palavra[i] = letra_escolhida
        tem_a_letra += 1
      print(advinha_palavra[i], end = " ")
    print(" ")

    if tem_a_letra == 0:
      chances -= 1
      lista_letras_erradas += letra_escolhida + " "

    tem_a_letra = 0

    for i in range(0, len(advinha_palavra)):
      if advinha_palavra[i] != "_":
        certo += 1
      
    if certo == len(advinha_palavra):
      print("VOCÊ CONSEGUIU, PARABÉNS!!")
      break

    certo = 0

    print(" ")
    print(f"Letras erradas: {lista_letras_erradas}")
    print(f"Chances restantes: {chances}")
    print(" ")
  
  if chances == 0:
    print("Você perdeu, que triste ;(")
    print(f"A palavra era: {palavra}")


lista_de_animais = ["leao", "baleia", "golfinho", "hipopotamo", "arara", "cachorro", "gato", "lagartixa", "macaco", "abelha", "lesma", "veado", "tartaruga", "aranha", "anta", "rinoceronte", "cabra", "cacatua", "escorpiao", "falcao", "flamingo", "naja", "orangotango", "ornitorrinco", "borboleta", "coruja"]
print("ESSE É O JOGO DA FORCA!")
print(" ")
print(" ")
identificando_letras(lista_de_animais)
