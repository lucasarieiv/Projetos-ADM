from tkinter import *

def visualizarJanela():

    def bt_visualizar():
        item = nomeProduto.get()
        print(item)
        cont = 0
        itemsCon = open('produtos.txt', 'r')
        itemsConteudo = itemsCon.read()
        itemsList = itemsConteudo.split('\n')
        itemsCon.close()

        janela3 = Tk()

        top = Label(janela3, text='Itens Encontrados', foreground='#fff', height=2)
        top['bg'] = '#4AB5FB'
        top.configure(font=('Arial', 30))
        top.pack(side=TOP, fill=X)

        texto1 = Listbox(janela3, font=('', 12), height=100)
        for i in itemsList:
            if i == '':
                continue
            findItem = re.search(item.upper(), i)
            if findItem != None:
                cont += 1
                # texto1 = Label(janela3, text=str(i), foreground='#000', height=2)
                tx = text=str(cont).ljust(50, '.') + str(i)
                texto1.insert(cont, tx)
                texto1.configure(font=('Arial', 22))
                texto1['bg'] = '#fff'
                texto1.pack(side=TOP, fill=X, pady=10)

        janela3.title('Visualizando Produtos')
        janela3.geometry('1900x1000+0+0')
        janela3.mainloop()
        itemsList.sort()

    janela2 = Tk()

    top = Label(janela2, text='Visualizar Produtos', foreground='#fff', height=2)
    top['bg'] = '#4AB5FB'
    top.place(x=0, y=0)
    top.configure(font=('Arial', 22))
    top.pack(side=TOP, fill=X)

    texto = Label(janela2, text='Digite o Nome do Produto \n Ex: Lampada', foreground='#000', height=2)
    texto.configure(font=('Courier', 33))
    texto.pack(pady=50)

    nomeProduto = Entry(janela2, width=30, foreground='#4F4F4F')
    nomeProduto.configure(font=('Heveltica', 22))
    nomeProduto.pack(pady=10)

    bt = Button(janela2, width=30, height=2, text='Pesquisar', borderwidth=0, foreground='#fff', command=bt_visualizar)
    bt['bg'] = '#4AB5FB'
    bt.configure(font=('Verdana', 20))
    bt.pack(pady=80)


    janela2.title('Visualizar')
    janela2.geometry('650x650+200+200')
    janela2.mainloop()
