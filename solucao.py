import requests
import json
import tkinter as tk

# função para atualizar a data e hora de embarque e chegada do voo na tela
def update_flight_info():
    # fazer a consulta à API do Flightradar24
    url = "https://data.flightradar24.com/v1/flight/list.json?query=GLO1373"
    response = requests.get(url)
    
    # converter a resposta em JSON
    data = json.loads(response.content)
    
    # obter as informações de embarque e chegada do voo
    flight_data = data["result"]["response"]["data"][0]
    departure_time = flight_data["departure"]["time"]["scheduled"]
    arrival_time = flight_data["arrival"]["time"]["scheduled"]
    
    # atualizar o texto na tela
    departure_label.config(text="Embarque: " + departure_time)
    arrival_label.config(text="Chegada: " + arrival_time)
    
    # aguardar 1 minuto antes de atualizar novamente
    root.after(60000, update_flight_info)

# criar a janela principal
root = tk.Tk()
root.title("Informações do voo")

# criar as labels para as informações de embarque e chegada
departure_label = tk.Label(root, font=("Arial", 18))
arrival_label = tk.Label(root, font=("Arial", 18))

# posicionar as labels na tela
departure_label.pack(pady=10)
arrival_label.pack()

# chamar a função de atualização pela primeira vez
update_flight_info()

# iniciar o loop principal da interface gráfica
root.mainloop()
