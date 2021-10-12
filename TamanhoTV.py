def ola():
    print("\nOlá, Vamos descobrir quantas pelegadas tem a sua tv ?\n"
      "Primeiro precisamos saber quantos centimetros tem a sua tv em DIAGONAL, pegue uma fiTa e veja a medida de ponta até a outra\n")
    resultado()

def resultado():
    tv = float(input("Digite quantos centímetros tem a sua tv em diagonal: "))
    polegada = float(2.54)
    print("A Sua tv tem, {:.2f} Polegadas\n".format(tv/polegada))
    sair()

def sair():
    decisao = input("Quer fazer uma nova consulta ?\n"
      "Digite 1 para fazer uma nova conslta\n"
      "digite 2 para sair:" )
    if decisao == "1":
        ola()
        resultado()
    elif decisao == "2":
        ola()
    else:
        sair()
ola()