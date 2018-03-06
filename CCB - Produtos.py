from functools import partial
from tkinter import *
from backup import *
from cadastro import *
from visualizar import *

class janela(object):

    def bt_backup(self):
        backup()

    def janelaPrincipal(self):
        def bt_cadastro():
            cadastroJanela()

        def bt_visualizar():
            visualizarJanela()

        janela = Tk()

        # Botão Cadastrar
        bt1 = Button(janela, width=30, height=2, text='Cadastrar', borderwidth=0, foreground='#fff', command=bt_cadastro)
        # bt1['command'] = partial(bt_cadastro, janela)
        bt1.place(x=55, y=140)
        bt1['bg'] = '#22C234'
        bt1.configure(font=('Verdana', 20))
        # Fim Botão Cadastrar

        # Botão Vizualizar
        bt2 = Button(janela, width=30, height=2, text='Vizualizar', borderwidth=0, foreground='#fff', command=bt_visualizar)
        # bt2['command'] = partial(bt_click, bt2)
        bt2.place(x=55, y=260)
        bt2['bg'] = '#4AB5FB'
        bt2.configure(font=('Verdana', 20))

        # Fim Botão Vizualizar

        # Botão Excluir
        bt3 = Button(janela, width=30, height=2, text='Excluir', borderwidth=0, foreground='#fff')
        bt3.place(x=55, y=380)
        bt3['bg'] = '#EF3C28'
        bt3.configure(font=('Verdana', 20))

        # Fim Botão Excluir

        # Botão Backup
        bt4 = Button(janela, width=30, height=2, text='Backup', borderwidth=0, foreground='#fff', command=self.bt_backup)
        bt4.place(x=55, y=500)
        bt4['bg'] = '#ED9C0F'
        bt4.configure(font=('Verdana', 20))

        # Fim Botão Backup

        top = Label(janela, text='PROGRAMA CODIGO', foreground="#fff", height=2)
        top.place(x=0, y=0)
        top['bg'] = '#F23838'
        top.configure(font=('Arial', 22)) # 'bold'
        top.pack(side=TOP, fill=X)

        # lb = Label(janela, text='Teste')
        # lb.place(x=40, y=50)
        # lb.configure(font=("Courier", 44))

        # Configurações da Janela
        janela.title('Meu Programa')
        janela.geometry('630x650+200+200')
        janela['bg'] = '#fff'
        janela.mainloop()


janela = janela()
janela.janelaPrincipal()
