import tkinter as tk
from tkinter import messagebox
import random
import pygame
from tkinter import ttk

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

# Lista de músicas
musicas = [
    "2much.mp3",
    "asIam.mp3",
    "deserveyou.mp3",
    "swapitout.mp3",
    "trust.mp3",
    "up.mp3"
]

# Função para exibir a mensagem personalizada
def exibir_mensagem():
    nome = campo_nome.get()  # Obtém o nome digitado pelo usuário
    mensagem_personalizada = random.choice(mensagens)
    messagebox.showinfo("Mensagem de Dia dos Namorados", f"{nome}, {mensagem_personalizada}")

# Função para reproduzir a música
def reproduzir_musica():
    pygame.mixer.music.load(musica_selecionada.get())
    pygame.mixer.music.play()

# Função para parar a música
def parar_musica():
    pygame.mixer.music.stop()

# Função para ajustar o volume
def ajustar_volume(event):
    volume = float(barra_volume.get())
    pygame.mixer.music.set_volume(volume)

# Inicializa o módulo pygame
pygame.init()

# Cria uma janela
janela = tk.Tk()
janela.title("Dia dos Namorados")

# Define o estilo dos botões
style = ttk.Style()
style.configure("TButton", font=("Arial", 12), padding=10, width=15)

# Define o estilo para o rótulo do volume
style.configure("TLabel", font=("Arial", 12), padding=10)

# Cria um rótulo e uma entrada de texto para o nome
rotulo_nome = ttk.Label(janela, text="Digite o seu nome:")
rotulo_nome.pack()

campo_nome = ttk.Entry(janela)
campo_nome.pack()

# Cria um botão para exibir a mensagem personalizada
botao_mensagem = ttk.Button(janela, text="Exibir mensagem", command=exibir_mensagem)
botao_mensagem.pack(pady=10)

# Cria um botão para reproduzir a música
botao_reproduzir = ttk.Button(janela, text="Ligar música", command=reproduzir_musica)
botao_reproduzir.pack(pady=10)

# Cria um botão para parar a música
botao_parar = ttk.Button(janela, text="Parar música", command=parar_musica)
botao_parar.pack(pady=10)

# Cria um widget de lista para escolher a música
musica_selecionada = tk.StringVar()
musica_selecionada.set(musicas[0])  # Define a primeira música como a selecionada inicialmente
lista_musicas = ttk.Combobox(janela, textvariable=musica_selecionada, values=musicas)
lista_musicas.pack(pady=10)

# Função para lidar com a seleção da música
def selecionar_musica(event):
    musica_selecionada = lista_musicas.get()
    pygame.mixer.music.load(musica_selecionada)

lista_musicas.bind("<<ComboboxSelected>>", selecionar_musica)

# Cria uma barra de rolagem para ajustar o volume
barra_volume = ttk.Scale(janela, from_=0.0, to=1.0, orient=tk.HORIZONTAL, length=200)
barra_volume.set(1.0)  # Define o volume inicial como máximo
barra_volume.bind("<ButtonRelease-1>", ajustar_volume)  # Ajusta o volume ao soltar o botão do mouse
barra_volume.pack(pady=10)

# Define o estilo para o fundo da janela
style.configure("TFrame", background="pink")

# Cria um frame para estilizar o fundo da janela
frame_fundo = ttk.Frame(janela, style="TFrame")
frame_fundo.pack(fill=tk.BOTH, expand=True)

# Define o estilo para o título da janela
style.configure("TLabel", background="pink", font=("Arial", 16, "bold"))

# Cria um rótulo para o título da janela
rotulo_titulo = ttk.Label(frame_fundo, text="Feliz Dia dos Namorados!", style="TLabel")
rotulo_titulo.pack(pady=20)

# Inicia o loop principal da janela
janela.mainloop()

