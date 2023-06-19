#responsavel por apurar os votos dos usuarios
candidatos = [] #armazena a lista de candidatos
eleitores = [] # armazena a lista de eleitores
votos = [0,0,0] #armazena os votos de cada candidato


def user(w3):

    candidatos.append(w3.eth.accounts[0])
    candidatos.append(w3.eth.accounts[1])
    candidatos.append(w3.eth.accounts[2])

    eleitores.append(w3.eth.accounts[4])
    eleitores.append(w3.eth.accounts[5])
    eleitores.append(w3.eth.accounts[6])

    return eleitores, candidatos

def apuracao(w3, tx_hash00, tx_hash01, tx_hash02):

    if w3.eth.get_transaction_count(w3.eth.accounts[4]) < 2:
        #conte um voto
        print("eleitor 4 correto")

    
    if w3.eth.get_transaction_count(w3.eth.accounts[5]) < 2:
        #conte um voto
        print("eleitor 5 correto")    

    if w3.eth.get_transaction_count(w3.eth.accounts[6]) < 2:
        #conte um voto
        print("eleitor 6 correto")
    
    bloco02 = w3.eth.get_transaction(tx_hash02)
    bloco01 = w3.eth.get_transaction(tx_hash01)
    bloco00 = w3.eth.get_transaction(tx_hash00)

    flag_apuracao = 0

    while flag_apuracao < 3:
        if candidatos[flag_apuracao] in bloco00['to']:
            votos[flag_apuracao] += 1
        if candidatos[flag_apuracao] in bloco01['to']:
            votos[flag_apuracao] += 1
        if candidatos[flag_apuracao] in bloco02['to']:
            votos[flag_apuracao] += 1
        flag_apuracao += 1
         
    return votos




