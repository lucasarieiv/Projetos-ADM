#! python3
# Igreja.py - Realiza Cadastro e Exclusão de Dados!

import re, os, shutil, datetime

def visualizarProd():
    itemsCon = open('produtos.txt', 'r')
    itemsConteudo = itemsCon.read()
    itemsList = itemsConteudo.split('\n')
    itemsCon.close()
    return itemsList

def limparTela():
    cls = input()
    if cls == '' or cls != '':
        os.system('cls')

while True:
    print('Digite [1] Para Cadastrar Novos Produtos')
    print('Digite [2] Para Visualizar Existentes')
    print('Digite [3] Para Excluir Item')
    print('Digite [4] Para Sair')
    print('Digite [5] Para Fazer Backup')
    print('')
    entrada = input('Digite: ')
    if entrada == '':
        os.system('cls')


    #SE A ENTRADA == 1
    if entrada == '1':
        print('')
        print('Digite o Nome do Produto [Ex: Luvas]')
        nome = input('Nome Produto: ')
        print('')
        print('Digite o Código do Produto [Ex: 3014]')
        prodCode = input('Código Produto: ')
        if nome == '':
            continue
        items = open('produtos.txt', 'a')
        items.write(nome.upper() + ' - ' + prodCode + '\n')
        items.close()
        print('')
        print('CADASTRADO COM SUCESSO!')
        limparTela()


    #SE A ENTRADA == 2
    elif entrada == '2':
        print('Digite o Nome [Ex: Luvas] ou Código [Ex: 3014]')
        item = input('Nome do Produto: ')
        print('')
        cont = 0
        itemsList = visualizarProd()
        itemsList.sort()
        for i in itemsList:
            if i == '':
                continue
            findItem = re.search(item.upper(), i)
            if findItem != None:
                print('')
                cont += 1
                prod = str(cont) + '- Item Encontrado '+'[ '+ i + ' ]'
                print(''.ljust(10, '.') + ' ' + prod)
        print('')
        if cont == 0:
            print('NENHUM ITEM ENCONTRADO NO BANCO DE DADOS')
        else:
            print('Total de Resultados [' + str(cont) + ']')
        limparTela()


    #SE A ENTRADA == 3
    elif entrada == '3':
        print('')
        print('Digite o Nome [Ex: Luvas] ou Código [Ex: 3014]')
        ndP = input('Digite: ') #Nome do Produto
        while ndP == '':
            print('Digite o Nome [Ex: Luvas] ou Código [Ex: 3014]')
            ndP = input('Digite: ')
        itemL = visualizarProd()
        itemL.sort()
        cont = 0
        lista = []
        lista2 = []

        for i in itemL:
            findItem = re.search(ndP.upper(), i)
            if findItem == None:
                lista.append(i)
            elif findItem != None:
                lista2.append(i)
            elif i == '':
                continue

        #LOOP PARA VIZUALIZAR OS PRODUTOS
        for li in lista2:
            if li == '':
                continue
            cont += 1
            print('.......... ['+ str(cont) +'] Número do Item ' + li)
        print('')
        print('Digite o Número do Item Para Excluir [Ex: 1]')
        exI = input('Digite: ')
        if exI == '':
            limparTela()
            continue
        cont = 0
        salvo = []

        #LOOP PARA PEGAR O NÚMERO DO PRODUTO ESCOLHIDO E JOGAR EM UMA LISTA DE EXCLUSÃO
        for li in lista2:
            cont += 1
            if cont != int(exI):
                salvo.append(li)
        prod = open('produtos.txt', 'w')
        for i in lista:
            prod.write(i + '\n')
        for s in salvo:
            prod.write(s + '\n')
        prod.close()
        print('')
        print('DELETADO COM SUCESSO!')
        limparTela()

    #SE A ENTRADA == 4
    elif entrada == '4':
        break

    #SE A ENTRADA == 5
    elif entrada == '5':
        user = os.getlogin()
        shutil.copy('produtos.txt', 'C:\\Users\\' + user + '\\OneDrive')
        print('Backup Realizado Com Sucesso', datetime.datetime.now())
        limparTela()
