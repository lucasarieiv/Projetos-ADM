from tkinter import *

def cadastroJanela():
    def bt_click():
        nome = nomeProduto.get()
        while nome == '':
            msg = Label(janela1, text='Erro: Digite o Nome do Produto', foreground='red', width=30)
            msg.place(x=70, y=260)
            msg['bg'] = '#fff'
            msg.configure(font=('Verdana', 12))
            cadastroJanela.destroy()
            cadastroJanela()
        prodCode = codigoProduto.get()
        items = open('produtos.txt', 'a')
        items.write(nome.upper() + ' - ' + prodCode + '\n')
        items.close()
        janela1.destroy()

    janela1 = Tk()

    top = Label(janela1, text='Cadastro Produtos', foreground='#fff', height=2)
    top.place(x=0, y=0)
    top['bg'] = '#ED9C0F'
    top.configure(font=('Arial', 22))
    top.pack(side=TOP, fill=X)

    nomeTexto = Label(janela1, text='Nome Ex: Lâmpada')
    nomeTexto['bg'] = '#fff'
    nomeTexto.place(x=100, y=130)
    nomeTexto.configure(font=("Courier", 33))

    nomeProduto = Entry(janela1, width=25, font=('Verdana', 20))
    nomeProduto.place(x=100, y=200)

    codigoTexto = Label(janela1, text='Código Ex: 3014')
    codigoTexto['bg'] = '#fff'
    codigoTexto.place(x=100, y=290)
    codigoTexto.configure(font=('Courier', 33))

    codigoProduto = Entry(janela1, width=25, font=('Verdana', 20))
    codigoProduto.place(x=100, y=350)

    bt = Button(janela1, width=30, height=2, text='Cadastrar', borderwidth=0, foreground='#fff', command=bt_click)
    bt.place(x=55, y=450)
    bt['bg'] = '#ED9C0F'
    bt.configure(font=('Verdana', 20))


    janela1.title('Cadastro')
    janela1.geometry('630x650+200+200')
    janela1['bg'] = '#fff'
    janela1.mainloop()
