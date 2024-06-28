import requests
import tkinter as tk
from tkinter import ttk

nomeinvocador = ''

# Criação da Interface Gráfica
def collectsummoner():

    def submit_form(event=None):
        global nomeinvocador
        nomeinvocador = nomeinvocador_entry.get()
        window.destroy()

    # Criação da janela principal
    window = tk.Tk()
    window.title("LOL STATS")

    # Estilo e tema para widgets
    style = ttk.Style()
    style.configure("TLabel", font=("Helvetica", 12))
    style.configure("TEntry", font=("Helvetica", 12))
    style.configure("TButton", font=("Helvetica", 12))

    # Rótulo e campo de entrada para o Login
    nomeinvocador_label = ttk.Label(window, text="Nome de Invocador:")
    nomeinvocador_label.grid(row=0, column=0, padx=10, pady=10)
    nomeinvocador_entry = ttk.Entry(window)
    nomeinvocador_entry.grid(row=0, column=1, padx=10, pady=10)

    # Botão de envio do formulário
    submit_button = ttk.Button(window, text="Enviar", command=submit_form)
    submit_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
    window.bind('<Return>', submit_form)

    # Execução da janela principal
    window.mainloop()

collectsummoner()

activesummoner = requests.get("https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + (nomeinvocador) + "?api_key=RGAPI-82f0756c-a360-467b-89d7-cfed8f3870b9")
summonerid = activesummoner.json()
# specdata = requests.get("https://br1.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/" + (summonerid['id']) + "?api_key=RGAPI-82f0756c-a360-467b-89d7-cfed8f3870b9")
# (activesummoner.json())
print(activesummoner)