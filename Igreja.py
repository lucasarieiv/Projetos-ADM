import re

while True:
    print('Digite [1] Para Cadastrar Novos Produtos')
    print('Digite [2] Para Visualizar')
    print('Digite [3] Para Sair')
    entrada = input()
    if entrada == '1':
        print('Digite o Nome do Produto')
        nome = input()
        print('Digite o Código do Produto')
        prodCode = input()
        items = open('produtos.txt', 'a')
        items.write(nome + ' - ' + prodCode + '\n')
        items.close()
    elif entrada == '2':
        print('Digite o Item')
        item = input()
        itemsCon = open('produtos.txt', 'r')
        itemsConteudo = itemsCon.read()
        itemsList = itemsConteudo.split('\n')
        for i in itemsList:
            findItem = re.search(item, i)
            if findItem != None:
                print(i)

        itemsCon.close()
    elif entrada == '3':
        break
