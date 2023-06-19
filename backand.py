from web3 import Web3
import os

#variaveis utilizadas pelo frontand
candidatos = [700,100, 135]
candidato = 0
eleitor = [4, 5, 6] #três eleitores

#função para verificar a conexão com a rede ethereun
def conected():
    os.system("clear || cls")
    w3 = Web3(Web3.EthereumTesterProvider())
    if True == w3.is_connected():
        print("Você está conectado a rede ethereun...")
        print("\n\n")
    else:
        print("error na conexão, pedimos desculpas tente mais tarde")
    return w3

def transacao(w3, candidato, eleitor):
    
    flag_candidato = 0
    if candidato == candidatos[0]:
        flag_candidato = 0
    if candidato == candidatos[1]:
        flag_candidato = 1
    if candidato == candidatos[2]:
        flag_candidato = 2

    tx_hash = w3.eth.send_transaction({

   'from': w3.eth.accounts[eleitor], #eleitor que quer votar

   'to': w3.eth.accounts[flag_candidato], # candidato

   'value': w3.to_wei(3, 'ether'),

   'gas': 21000

    })

    return w3, flag_candidato, tx_hash





    


