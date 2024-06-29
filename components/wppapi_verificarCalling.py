import requests
import json
import pyodbc
import mysql.connector
from datetime import datetime, timedelta

API_KEY = 'akumabot'
session_id = 'akumabot'
WPP_API_URL = 'http://localhost:3000'
data_atual = datetime.today()
dia_amanha_str = data_atual + timedelta(1)
dia_amanha = dia_amanha_str.date()

with open('comandos.json', 'r') as jsonread:
    comando = json.load(jsonread)

vermensagens = requests.post(WPP_API_URL + '/client/searchMessages/' + session_id, headers={"x-api-key":API_KEY}, data=comando.get("search", {}))

vermensagensJSON = vermensagens.json()
vermensagensDUMP = json.dumps(vermensagensJSON, indent=4)

with open("IdsMensagens.json", "w") as outfile:
    outfile.write(vermensagensDUMP)

with open('IdsMensagens.json', 'r') as file:
    IdMensagem = json.load(file)


# id_mensagem = IdMensagem.get('messages')[0].get('_data').get('id').get("id")
id_chat = IdMensagem.get('messages')[0].get('_data').get('id').get("remote")

# print(id_mensagem)
print(id_chat)

if vermensagensJSON.get("messages"):
    enviarmensagem = requests.post(WPP_API_URL + '/client/sendMessage/' + session_id, headers={"x-api-key":API_KEY}, data=comando.get("retorno", {}))

    visualizarmensagem = requests.post(WPP_API_URL + '/client/sendSeen/' + session_id, headers={"x-api-key":API_KEY}, data=(id_chat))
    print(visualizarmensagem)

# enviarmensagemJSON = enviarmensagem.json()

# scheduleJSON = schedule.json()
# scheduleFINALJSON = json.dumps(scheduleJSON, indent=4)

# with open("schedule.json", "w") as outfile:
#     outfile.write(scheduleFINALJSON)

# with open('schedule.json', 'r') as file:
#     data = json.load(file)

# Navegar pela estrutura aninhada
# jogos = data.get("data", {}).get("schedule", {}).get("events", [])

# # Filtrar e retornar valores de startTime
# for jogo in jogos:
#     start_time_str = jogo.get("startTime")

#     if start_time_str:
#         start_time = datetime.fromisoformat(start_time_str.rstrip('Z')).date()
#         print(start_time)
#         if start_time == dia_amanha:
#             times_de_hoje = jogo.get("match", {}).get("teams", [])

#             for times in times_de_hoje:
#                 time = times.get("code")
#                 vitoria = times.get("result")
#                 print(time)
#                 confronto = confronto + 1

#                 if times.get("result", {}).get("outcome") == "win":
#                     time_venceu = time
                
#                 if confronto == 2:
#                     print(f"Vitória: {time_venceu}")
#                     print("")
#                     confronto = 0
#                     time_venceu = ""

# cnc = mysql.connector.connect(user='root', password='',
#                               host='localhost',
#                               database='db_bolaocblol')
# cursor = cnc.cursor()

# cursor.execute("SELECT * FROM db_bolaocblol.users")

# lista = list(cursor)

# for l in lista:
#     var_id               = l[1]
#     var_first_name       = l[2]
#     var_phone_number     = l[3]

#     '''
#     Codigo_Nota_Debito
#     Codigo_Cliente
#     Contrato
#     '''
    
#     print(l)
# 120363314368602784@g.us id grupo teste
# https://andydanger.github.io/live-lol-esports/#/
# https://github.com/AndyDanger/live-lol-esports/blob/main/src/utils/LoLEsportsAPI.ts
# https://github.com/vickz84259/lolesports-api-docs/tree/master
# https://vickz84259.github.io/lolesports-api-docs/#tag/leagues
# https://github.com/pedroherpeto/whatsapp-api
# https://github.com/chrishubert/whatsapp-api