from tkinter import *

def visualizarJanela():

    # Função Qunado o Botão for Clicado
    def bt_visualizar(janela):
        item = nomeProduto.get()
        cont = 0
        itemsCon = open('produtos.txt', 'r')
        itemsConteudo = itemsCon.read()
        itemsList = itemsConteudo.split('\n')
        itemsCon.close()

        janela.destroy()

        janela3 = Tk()

        top = Label(janela3, text='Produtos Encontrados', foreground='#fff', bg='#4AB5FB', font=('Arial', 30), height=2)
        top.pack(side=TOP, fill=X)

        texto1 = Listbox(janela3, font=('', 12), height=100)
        for i in itemsList:
            if i == '':
                continue
            findItem = re.search(item.upper(), i)
            if findItem != None:
                cont += 1
                # texto1 = Label(janela3, text=str(i), foreground='#000', height=2)
                tx = text=str(cont).ljust(40, '.') + str(i)
                texto1.insert(cont, tx)
                texto1.configure(font=('Arial', 22))
                texto1['bg'] = '#fff'
                texto1.pack(side=TOP, fill=X, pady=10)

        # Configurações da Janela
        janela3.title('Visualizar Produtos')
        janela3.state('zoomed') # Janela Full Screen
        janela3.mainloop()
        itemsList.sort()

    # Cria Janela
    janela2 = Tk()

    # Topo do Programa
    top = Label(janela2, text='Visualizar Produtos', foreground='#fff', height=2, bg='#4AB5FB', font=('Arial', 30))
    top.pack(side=TOP, fill=X)

    # Texto: Digite o Nome do Produto \n Ex: Lâmpada
    texto = Label(janela2, text='Digite o Nome do Produto \n Ex: Lâmpada', foreground='#000', font=('Courier', 30))
    texto.pack(pady=50)

    # Caixa de Input do "Digite o Nome do Produto Ex: Lâmpada"
    nomeProduto = Entry(janela2, width=30, foreground='#4F4F4F', font=('Heveltica', 22))
    nomeProduto.pack(pady=10)

    # Botão Pesquisar
    bt = Button(janela2, width=30, height=2, text='Pesquisar', borderwidth=0, foreground='#fff', bg='#4AB5FB', font=('Verdana', 20), command= lambda: bt_visualizar(janela2))
    bt.pack(pady=60)

    # Rodapé
    rodape = Label(janela2, text='Por Lucas Vieira Copyright \xa9 2018 - Todos os Direitos Reservados', bg='#4AB5FB', foreground='#fff', height=3, font=('Verdana', 13))
    rodape.pack(side=BOTTOM, fill=X)

    # Configurações da Janela
    janela2.title('Visualizar')
    janela2.geometry('630x650+200+200')
    janela2.mainloop()
