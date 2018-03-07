from tkinter import *

def cadastroJanela():

    # Função Quando o Botão For Clicado
    def bt_click():
        nome = nomeProduto.get()
        while nome == '':
            msg = Label(janela1, text='Erro: Digite o Nome do Produto', foreground='red', width=30, bg='#fff', font=('Verdana', 12))
            msg.pack(pady=5)
            cadastroJanela.destroy()
            cadastroJanela()
        prodCode = codigoProduto.get()
        items = open('produtos.txt', 'a')
        items.write(nome.upper() + ' - ' + prodCode + '\n')
        items.close()
        janela1.destroy()

    # Cria Janela
    janela1 = Tk()

    # Topo do Programa
    top = Label(janela1, text='Cadastro Produtos', foreground='#fff', height=2, bg='#ED9C0F', font=('Arial', 30))
    top.pack(side=TOP, fill=X)

    # Texto: Nome Ex: Lâmpada
    nomeTexto = Label(janela1, text='Nome Ex: Lâmpada', bg='#fff', font=("Courier", 30))
    nomeTexto.pack(pady=30)

    # Caixa de Input do "Nome Ex: Lâmpada"
    nomeProduto = Entry(janela1, width=30, font=('Heveltica', 22))
    nomeProduto.pack(pady=10)

    # Texto: Código Ex: 3014
    codigoTexto = Label(janela1, text='Código Ex: 3014', bg='#fff', font=('Courier', 33))
    codigoTexto.pack(pady=10)

    # Caixa de Input do "Código Ex: 3014"
    codigoProduto = Entry(janela1, width=30, font=('Heveltica', 22))
    codigoProduto.pack(pady=30)

    # Botão Cadastrar
    bt = Button(janela1, width=30, height=2, text='Cadastrar', borderwidth=0, foreground='#fff', bg='#ED9C0F', font=('Verdana', 20), command=bt_click)
    bt.pack(pady=15)

    # Rodapé
    rodape = Label(janela1, text='Por Lucas Vieira Copyright \xa9 2018 - Todos os Direitos Reservados', bg='#ED9C0F', foreground='#fff', height=3, font=('Verdana', 13))
    rodape.pack(side=BOTTOM, fill=X)


    # Configurações da Janela
    janela1.title('Cadastro')
    janela1.geometry('630x650+200+200')
    janela1['bg'] = '#fff'
    janela1.mainloop()
