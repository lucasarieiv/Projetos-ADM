from tkinter import *

def janelaDelete():

    def bt_deletar():
        item = nomeProduto.get()
        while item == '':
            msg = Label(janelaDel, text='Erro: Digite o Nome do Produto', foreground='red', width=30, height=2)
            msg.configure(font=('Verdana', 12))
            msg.pack(pady=0)
            janelaDelete.destroy()

        cont = 0
        itemsCont = open('produtos.txt', 'r')
        itemsConteudo = itemsCont.read()
        itemsConteudo = itemsConteudo.split('\n')
        itemsCont.close()

        # Cria Janela
        deleteJanela =  Tk()

        top = Label(deleteJanela, text='Produtos Para Deletar', bg='#EF3C28', foreground='#fff', font=('Arial', 30), height=2)
        top.pack(side=TOP, fill=X)

        texto1 = Listbox(deleteJanela, font=('Arial', 12), height=100)

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
    bt = Button(janelaDel, width=30, height=2, text='Pesquisar', bg='#EF3C28', borderwidth=0, foreground='#fff', font=('Verdana', 20), command=bt_deletar)
    bt.pack(pady=60)

    # Rodapé
    rodape = Label(janelaDel, text='Por Lucas Vieira Copyright \xa9 2018 - Todos os Direitos Reservados', bg='#EF3C28', foreground='#fff', height=3, font=('Verdana', 13))
    rodape.pack(side=BOTTOM, fill=X)

    janelaDel.geometry('630x650+200+200')
    janelaDel.title('Delete')
    janelaDel.mainloop()
