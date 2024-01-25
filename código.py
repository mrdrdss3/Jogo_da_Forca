import random

# Escolhendo uma palavra aleatória da lista de animais
def escolher_palavra(lista_de_animais):
  indice = random.randint(0, len(lista_de_animais)-1)
  palavra_escolhida = lista_de_animais[indice]

  return(palavra_escolhida)

# Criando as variáveis necessárias
def identificando_letras(lista_de_animais):
  chances = 6
  certo = 0
  lista_letras_erradas = ""
  tem_a_letra= 0
  palavra = escolher_palavra(lista_de_animais)
  advinha_palavra = []
  
  print("tente adivinhar a palavra!")
  print(" ")

  # Colocando os traços em relação a quantidade de letras da palavra
  for letra in range(0, len(palavra)):
    advinha_palavra.append("_")

  # Imprimindo a string
  for i in range(0, len(advinha_palavra)):
    print(advinha_palavra[i], end = " ")
    
  print(" ")
  print(" ")

  # Lógica do jogo: enquanto houver chances o usuário deve inserir uma letra
  while chances > 0:
    letra_escolhida = input("Escolha uma letra: ")
    print(" ")
    
    ## Passa pela palavra e vê se a letra escolhida está presente; 
    ## Se sim: substituir o traço da string pela letra e adicionar mais um em um contador para quebrar o loop quando completar a palavra
    for i in range(0, len(palavra)):
      if letra_escolhida == palavra[i]:
        advinha_palavra[i] = letra_escolhida
        tem_a_letra += 1
      print(advinha_palavra[i], end = " ")
    print(" ")

    ## Se não: diminuir as chances e adicionar a letra escolhida em uma lista para não haver repetição
    if tem_a_letra == 0:
      chances -= 1
      lista_letras_erradas += letra_escolhida + " "

    # Zerar o contador dentro do loop para a leitura de novas letras
    tem_a_letra = 0

    # Contar a quantidade de letras achadas da palavra
    for i in range(0, len(advinha_palavra)):
      if advinha_palavra[i] != "_":
        certo += 1

    # Se a quantidade for igual a palavra foi completada
    if certo == len(advinha_palavra):
      print("VOCÊ CONSEGUIU, PARABÉNS!!")
      break

    certo = 0

    # Impressão da lista e das chances restantes
    print(" ")
    print(f"Letras erradas: {lista_letras_erradas}")
    print(f"Chances restantes: {chances}")
    print(" ")

  # Se a pessoa perder imprimir a palavra correta
  if chances == 0:
    print("Você perdeu, que triste ;(")
    print(f"A palavra era: {palavra}")


lista_de_animais = ["leao", "baleia", "golfinho", "hipopotamo", "arara", "cachorro", "gato", "lagartixa", "macaco", "abelha", "lesma", "veado", "tartaruga", "aranha", "anta", "rinoceronte", "cabra", "cacatua", "escorpiao", "falcao", "flamingo", "naja", "orangotango", "ornitorrinco", "borboleta", "coruja"]
print("ESSE É O JOGO DA FORCA!")
print(" ")
print(" ")
identificando_letras(lista_de_animais)
