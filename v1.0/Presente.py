import tkinter as tk
from tkinter import messagebox
import random

# Lista de mensagens românticas
mensagens = [
    "Você é a pessoa mais especial da minha vida. Feliz Dia dos Namorados!",
    "Meu amor por você é infinito. Tenha um Dia dos Namorados maravilhoso!",
    "Você ilumina a minha vida. Feliz Dia dos Namorados, meu amor!",
    "Você é a razão do meu sorriso. Tenha um dia cheio de amor!",
    "Ao seu lado, todos os dias são Dia dos Namorados. Te amo!",
    "Você é o meu presente mais precioso. Feliz Dia dos Namorados!",
    "Não há distância que nos separe. Feliz Dia dos Namorados, meu amor!",
    "Meu coração bate mais forte por você. Tenha um dia repleto de amor e carinho!"
]

# Função para exibir a mensagem personalizada
def exibir_mensagem():
    nome = campo_nome.get()  # Obtém o nome digitado pelo usuário
    mensagem_personalizada = random.choice(mensagens)
    messagebox.showinfo("Mensagem de Dia dos Namorados", f"{nome}, {mensagem_personalizada}")

# Cria uma janela
janela = tk.Tk()
janela.title("Dia dos Namorados")

# Cria um rótulo e uma entrada de texto para o nome
rotulo_nome = tk.Label(janela, text="Digite o seu nome:")
rotulo_nome.pack()

campo_nome = tk.Entry(janela)
campo_nome.pack()

# Cria um botão para exibir a mensagem personalizada
botao = tk.Button(janela, text="Exibir mensagem", command=exibir_mensagem)
botao.pack(pady=20)

# Inicia o loop principal da janela
janela.mainloop()
