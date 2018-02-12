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
    print('Digite [3] Para Sair')
    print('Digite [4] Para Fazer Backup')
    print('')
    entrada = input('Digite: ')
    if entrada == '1':
        print('')
        print('Digite o Nome do Produto')
        nome = input('Nome Produto: ')
        print('')
        print('Digite o Código do Produto')
        prodCode = input('Código Produto: ')
        if prodCode == '':
            prodCode = 'Sem Código'
        items = open('produtos.txt', 'a')
        items.write(nome.upper() + ' - ' + prodCode + '\n')
        items.close()
        print('Cadastrado com Sucesso!')
        limparTela()
    elif entrada == '2':
        print('Digite o Nome do Item ou Código')
        item = input('Nome do Produto: ')
        cont = 0
        itemsList = visualizarProd()
        for i in itemsList:
            findItem = re.search(item.upper(), i)
            if findItem != None:
                print('')
                cont += 1
                a = str(cont) + '- Item Encontrado '+'[ '+ i + ' ]'
                print(''.ljust(10, '.') + ' ' + a)
        print('')
        if cont == 0:
            print('Nenhum Item Encontrado no Banco de Dados')
        else:
            print('Total de Resultados: ' + str(cont))
        limparTela()
    elif entrada == '3':
        break
    elif entrada == '4':
        user = os.getlogin()
        shutil.copy('produtos.txt', 'C:\\Users\\' + user + '\\OneDrive')
        print('Backup Realizado Com Sucesso', datetime.datetime.now())
        limparTela()
