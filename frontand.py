import backand as back
from time import sleep
import apuracao_votos as apuracao

w3 = back.conected()



while True:

    print("\n")
    print("eleitor 1")

    sleep(3)
    print("candidato 0: 700")
    print("\n")
    print("candidato 1: 100")
    print("\n")
    print("candidato 2: 135")
    print("\n")
    back.candidato = input("Digite o numero do candidato: ")
    back.os.system("clear || cls")
    back.candidato = int(back.candidato) #converte candidato para inteiro

    if back.candidato in back.candidatos:
        w3, flag_candidato, tx_hash00 = back.transacao(w3, back.candidato, back.eleitor[0])
        back.os.system("clear || cls")
        print("Seu voto foi computado...")
        sleep(2)
        break
    else:
        print("Nenhum candidato tem o numero digitado, for favor digite novamente")
        sleep(2)
        back.os.system("clear || cls")

while True:

    print("\n")
    print("eleitor 2")

    sleep(3)
    print("candidato 0: 700")
    print("\n")
    print("candidato 1: 100")
    print("\n")
    print("candidato 2: 135")
    print("\n")
    back.candidato = input("Digite o numero do candidato: ")
    back.os.system("clear || cls")
    back.candidato = int(back.candidato) #converte candidato para inteiro

    if back.candidato in back.candidatos:
        w3, flag_candidato, tx_hash01 = back.transacao(w3, back.candidato, back.eleitor[1])
        back.os.system("clear || cls")
        print("Seu voto foi computado...")
        sleep(2)
        break
    else:
        print("Nehum candidato tem o numero digitado, for favor digite novamente")
        sleep(2)
        back.os.system("clear || cls")

while True:

    print("\n")
    print("eleitor 3")

    sleep(3)
    print("candidato 0: 700")
    print("\n")
    print("candidato 1: 100")
    print("\n")
    print("candidato 2: 135")
    print("\n")
    back.candidato = input("Digite o numero do candidato: ")
    back.os.system("clear || cls")
    back.candidato = int(back.candidato) #converte candidato para inteiro

    if back.candidato in back.candidatos:
        w3, flag_candidato, tx_hash02 = back.transacao(w3, back.candidato, back.eleitor[2])
        back.os.system("clear || cls")
        print("Seu voto foi computado...")
        sleep(2)
        break
    else:
        print("Nenhum candidato tem o numero digitado, for favor digite novamente")
        sleep(2)
        back.os.system("clear || cls")


eleitores, candidatos =  apuracao.user(w3)

votos = []

votos = apuracao.apuracao(w3, tx_hash00, tx_hash01, tx_hash02)

print("votos: ")
print(votos)

