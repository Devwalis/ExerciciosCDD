clientes ={
    'Maria': {'saldo': 5000},
    'Renata': {'saldo': 500},
    'Luciana': {'saldo': 1000}

}
clientes['Aline'] = {'saldo': 200}
print(clientes)

nomeClientes ='Maria'
print('Saldo de ', nomeClientes , ':',clientes[nomeClientes])
nomeClientes = 'Luciana'
novoSaldo = 12000
clientes['Luciana']['saldo'] = novoSaldo
print('Saldo de ', nomeClientes , ':',clientes[nomeClientes]['saldo'])
