import tkinter as tk
from tkinter import messagebox
import random
import pygame

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

# Função para reproduzir a música
def reproduzir_musica():
    pygame.mixer.music.load("loveme.mp3")  # Insira o caminho para o arquivo de música
    pygame.mixer.music.play()

# Função para parar a música
def parar_musica():
    pygame.mixer.music.stop()

# Função para ajustar o volume
def ajustar_volume(valor):
    volume = float(valor)
    pygame.mixer.music.set_volume(volume)

# Inicializa o módulo pygame
pygame.init()

# Cria uma janela
janela = tk.Tk()
janela.title("Dia dos Namorados")

# Cria um rótulo e uma entrada de texto para o nome
rotulo_nome = tk.Label(janela, text="Digite o seu nome:")
rotulo_nome.pack()

campo_nome = tk.Entry(janela)
campo_nome.pack()

# Cria um botão para exibir a mensagem personalizada
botao_mensagem = tk.Button(janela, text="Exibir mensagem", command=exibir_mensagem)
botao_mensagem.pack(pady=10)

# Cria um botão para reproduzir a música
botao_reproduzir = tk.Button(janela, text="Ligar música", command=reproduzir_musica)
botao_reproduzir.pack(pady=10)

# Cria um botão para parar a música
botao_parar = tk.Button(janela, text="Parar música", command=parar_musica)
botao_parar.pack(pady=10)

# Cria uma barra de rolagem para ajustar o volume
barra_volume = tk.Scale(janela, from_=0.0, to=1.0, resolution=0.1, orient=tk.HORIZONTAL, label="Volume", command=ajustar_volume)
barra_volume.pack(pady=10)

# Inicia o loop principal da janela
janela.mainloop()
