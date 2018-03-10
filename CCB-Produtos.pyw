from tkinter import *
from backup import *
from cadastro import *
from visualizar import *
from delete import *

class janela(object):

    def bt_backup(self):
        backup()

    def janelaPrincipal(self):

        # Função Para Chamar a Tela de Cadastro
        def bt_cadastro():
            cadastroJanela()

        # Função Para Chamar a Tela de Visualização
        def bt_visualizar():
            visualizarJanela()

        def bt_delete():
            janelaDelete()

        janela = Tk()

        # Topo do Programa
        top = Label(janela, text='CCB - CAMARAGIBE V 2.1', foreground="#fff", height=2, bg='#787878')
        top.configure(font=('Arial', 30, 'bold')) # 'bold'
        top.pack(side=TOP, fill=X)

        # Botão Cadastrar
        bt1 = Button(janela, width=30, height=2, text='Cadastrar', borderwidth=0, foreground='#fff', command=bt_cadastro, bg='#22C234')
        bt1.configure(font=('Verdana', 20))
        bt1.pack(pady=25)
        # Fim Botão Cadastrar

        # Botão Vizualizar
        bt2 = Button(janela, width=30, height=2, text='Vizualizar', borderwidth=0, foreground='#fff', command=bt_visualizar, bg='#4AB5FB')
        bt2.configure(font=('Verdana', 20))
        bt2.pack(pady=25)

        # Fim Botão Vizualizar

        # Botão Excluir
        bt3 = Button(janela, width=30, height=2, text='Excluir', borderwidth=0, foreground='#fff', bg='#EF3C28', command=bt_delete)
        bt3.configure(font=('Verdana', 20))
        bt3.pack(pady=25)

        # Fim Botão Excluir

        # Botão Backup
        bt4 = Button(janela, width=30, height=2, text='Backup', borderwidth=0, foreground='#fff', command=self.bt_backup, bg='#ED9C0F')
        bt4.configure(font=('Verdana', 20))
        bt4.pack(pady=25)
        # Fim Botão Backup

        # Configurações da Janela
        janela.title('CCB - CODIGOS V 2.1')
        janela.geometry('630x650+200+20')
        janela.mainloop()


janela = janela()
janela.janelaPrincipal()
