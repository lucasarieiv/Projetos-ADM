from tkinter import *
import re

def janelaDelete():

    def bt_deletar(janela):
        item = nomeProduto.get()
        while item == '':
            janela.destroy()

        cont = 0
        itemsCont = open('produtos.txt', 'r')
        itemsConteudo = itemsCont.read()
        itemsConteudo = itemsConteudo.split('\n')
        itemsCont.close()
        janela.destroy()

        # Cria Janela
        deleteJanela =  Tk()

        def delet(listaEncontrados, listaSemResultado, janela):
            c = cExcluir.get()
            cont = 0
            salvo = []
            for li in listaEncontrados:
                cont += 1
                if cont != int(c):
                    salvo.append(li)
            prod = open('produtos.txt', 'w')
            for i in listaSemResultado:
                prod.write(i + '\n')
            for s in salvo:
                prod.write(s + '\n')
            prod.close()
            janela.destroy()

        top = Label(deleteJanela, text='Produtos Para Deletar', bg='#EF3C28', foreground='#fff', font=('Arial', 30), height=2)
        top.pack(side=TOP, fill=X)

        itemL = itemsConteudo
        itemL.sort()
        cont = 0
        listaSemResultado = []
        listaEncontrados = []

        for i in itemL:
            findItem = re.search(item.upper(), i)
            if findItem == None:
                listaSemResultado.append(i)
            elif findItem != None:
                listaEncontrados.append(i)
            elif i == '':
                continue

        numeroIndice = Label(deleteJanela, text='Escolha o Produto Ex: [1]', font=('Arial', 22))
        numeroIndice.place(x=0, y=0)
        numeroIndice.pack(side=TOP)

        texto1 = Listbox(deleteJanela, font=('Verdana', 12),height=15)

        # Loop Para Visualizar os Produtos
        for li in listaEncontrados:
            if li == '':
                continue
            cont += 1
            findItem1 = re.search(item.upper(), li)
            if findItem1 != None:
                txt = text=str('[' + str(cont) + ']').ljust(30, '.') + str(li)
                texto1.insert(cont, txt)
                texto1.configure(font=('Verdana', 22))
                texto1['bg'] = '#ccc'
                texto1.pack(side=TOP, fill=X, pady=0)

        # Caixa de Input Botão Excluir
        cExcluir = Entry(deleteJanela, width=32, font=('Heveltica', 22))
        cExcluir.pack(pady=20)

        # Botão Excluir
        btExcluir = Button(deleteJanela, text='Excluir', foreground='#fff', borderwidth=0, width=30, height=2, font=('Verdana', 20), bg='#EF3C28', command= lambda: delet(listaEncontrados, listaSemResultado, deleteJanela))
        btExcluir.pack(pady=10)

        # Configurações da Janela
        deleteJanela.title('Deletar Produto')
        deleteJanela.geometry('1900x1000+0+0')
        deleteJanela.mainloop()

    # Cria Janela
    janelaDel = Tk()

    # Topo do Programa
    top = Label(janelaDel, text='Deletar Produtos', bg='#EF3C28', foreground='#fff', height=2, font=('Arial', 30))
    top.pack(side=TOP, fill=X)

    # Texto: Digite o Nome do Produto Ex: Lâmpada
    nomeTexto = Label(janelaDel, text='Digite o Nome do Produto \n Ex: Lâmpada', font=('Courier', 30))
    nomeTexto.pack(pady=50)

    # Caixa de Input do "Digite o Nome do Produto Ex: Lâmpada"
    nomeProduto = Entry(janelaDel, width=30, foreground='#4F4F4F', font=('Heveltica', 22))
    nomeProduto.pack(pady=10)

    # Botão Pesquisar
    bt = Button(janelaDel, width=30, height=2, text='Deletar', bg='#EF3C28', borderwidth=0, foreground='#fff', font=('Verdana', 20), command= lambda: bt_deletar(janelaDel))
    bt.pack(pady=60)

    # Rodapé
    rodape = Label(janelaDel, text='Por Lucas Vieira Copyright \xa9 2018 - Todos os Direitos Reservados', bg='#EF3C28', foreground='#fff', height=3, font=('Verdana', 13))
    rodape.pack(side=BOTTOM, fill=X)

    janelaDel.geometry('630x650+200+200')
    janelaDel.title('Delete')
    janelaDel.mainloop()
