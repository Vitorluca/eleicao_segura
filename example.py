#projeto eleição segura
from web3 import Web3 #web3


#conecta ao nó simulado da rede etheriun
w3 = Web3(Web3.EthereumTesterProvider())

#verifica se o sistema está conectado a rede
print("status: ")
print(w3.is_connected()) 

print("\n")

#Listar as contas cadastradas
print("contas: ")
print(w3.eth.accounts)

print("\n")

#verifica o valor armazenado em cada conta
print("valor em ether: ")
print( w3.eth.get_balance(w3.eth.accounts[0]))

print("\n")

#mudando a base do valor pora base 10
print("valor decimal: ")
print(w3.from_wei(1000000000000000000000000, 'ether'))

print("\n")

#status do blockchain simulado(status do ultimo bloco)
print("blockchain: ")
print(w3.eth.get_block('latest'))

#fazendo uma transação(estrutura de uma transação na rede ethereun)
tx_hash = w3.eth.send_transaction({

   'from': w3.eth.accounts[0],

   'to': w3.eth.accounts[1],

   'value': w3.to_wei(3, 'ether'),

   'gas': 21000

})

print("\n")

#status do novo bloco minerado
print("status do novo bloco: ")
print( w3.eth.get_transaction(tx_hash))

print("\n")

#soldo da conta 0 após a transação
print("saldo da conta 0: ")
print(w3.eth.get_balance(w3.eth.accounts[0]))

print("\n")

#soldo da conta 1 após a transação
print("saldo da conta 1: ")
print(w3.eth.get_balance(w3.eth.accounts[1]))

