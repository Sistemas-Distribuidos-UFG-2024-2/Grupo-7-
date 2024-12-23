import tkinter as tk
from tkinter import messagebox
from turtle import get_poly

# Função que será chamada ao clicar no botão
def exibir_mensagem():
    messagebox.showinfo("Mensagem", "Olá! Você clicou no botão.")
    str = botao.getvar()
    messagebox.showinfo("Mensagem", str)


# Criação da janela principal
janela = tk.Tk()
janela.title("Minha Interface")
janela.geometry("300x200")


# Mantendo a janela aberta
janela.mainloop()


class First_View:
    port = 0
    def __init__(self):
            #iniciando os atributos da janela first
            janela = tk.Tk()
            janela.title("Monitoramento de Servidores")
            janela.geometry("400x400")
   
    def get_port(self):
        return self.port
     
    def set_port(self,port):
         self.port = port

    def get_port_to_connect(self): 
        aux = self.entrada.get()
        self.set_port(aux)
        print(self.get_port())

    label = tk.Label(janela, text="Bem-vindo à Interface!", font=("Arial", 14))
    label.pack(pady=10)

    botao = tk.Button(janela, text="Clique aqui", command=get_port_to_connect(self))
    botao.pack(pady=10)

    entrada = tk.Entry(janela, width=25)
    entrada.pack(pady=10)

