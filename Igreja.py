import re
lista = {'Lixa de Ferro': '3001'}

while True:
    print('Digite [1] Para Cadastrar Novos Produtos')
    print('Digite [2] Para Consultar')
    print('Digite [3] Para Sair')
    entrada = input()
    if entrada == '1':
        print('Digite o Nome do Produto')
        nome = input()
        print('Digite o Código do Produto')
        prodCode = input()
        lista[nome] = prodCode
    elif entrada == '2':
        print('Digite o Item')
        item = input()
        for chave, valor in lista.items():
            print(chave, ' - ', valor)
            proc = re.search(item, chave)
            if proc.group(0) != None:
                print(proc.group(0))
            else:
                print('Objeto Não Encontrado')
    elif entrada == '3':
        break
