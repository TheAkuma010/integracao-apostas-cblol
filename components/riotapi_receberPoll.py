import requests
import json
import pyodbc
import mysql.connector
from datetime import datetime, timedelta

API_KEY = '0TvQnueqKa5mxJntVWt0w4LpLfEkrV1Ta8rQBb9Z'
API_URL_PERSISTED = 'https://esports-api.lolesports.com/persisted/gw'
API_URL_LIVE = "https://feed.lolesports.com/livestats/v1"
cblol_id = '98767991332355509'
cblol_split_2_2024_id = '112452930844731446'
confronto = 0
data_atual = datetime.today()
dia_amanha = data_atual + timedelta(1)

# standings = requests.get(API_URL + '/getTournamentsForLeague', headers={"x-api-key":API_KEY}, params={"hl":"pt-BR", "leagueId":cblol_id})

standings = requests.get(API_URL_PERSISTED + '/getStandings', headers={"x-api-key":API_KEY}, params={"hl":"pt-BR", "tournamentId":cblol_split_2_2024_id})

schedule = requests.get(API_URL_PERSISTED + '/getSchedule', headers={"x-api-key":API_KEY}, params={"hl":"pt-BR", "leagueId":cblol_id})

standingsJSON = standings.json()
standingFINALJSON = json.dumps(standingsJSON, indent=4)

with open("standing.json", "w") as outfile:
    outfile.write(standingFINALJSON)

scheduleJSON = schedule.json()
scheduleFINALJSON = json.dumps(scheduleJSON, indent=4)

with open("schedule.json", "w") as outfile:
    outfile.write(scheduleFINALJSON)

with open('schedule.json', 'r') as file:
    data = json.load(file)

# Navegar pela estrutura aninhada
jogos = data.get("data", {}).get("schedule", {}).get("events", [])

# Filtrar e retornar valores de startTime
for jogo in jogos:
    start_time_str = jogo.get("startTime")

    if start_time_str:
        start_time = datetime.fromisoformat(start_time_str.rstrip('Z')).date()

        if start_time == data_atual:
            times_de_hoje = jogo.get("match", {}).get("teams", [])

            for times in times_de_hoje:
                time = times.get("code")
                vitoria = times.get("result")
                print(time)
                confronto = confronto + 1

                if times.get("result", {}).get("outcome") == "win":
                    time_venceu = time
                
                if confronto == 2:
                    print(f"Vitória: {time_venceu}")
                    print("")
                    confronto = 0
                    time_venceu = ""

cnc = mysql.connector.connect(user='akuma', password='03072005',
                              host='localhost',
                              database='db_bolaocblol')
cursor = cnc.cursor()

cursor.execute("SELECT * FROM db_bolaocblol.users")

lista = list(cursor)

for l in lista:
    var_id               = l[1]
    var_first_name       = l[2]
    var_phone_number     = l[3]

    '''
    Codigo_Nota_Debito
    Codigo_Cliente
    Contrato
    '''
    
    print(l)
# 120363314368602784@g.us id grupo teste
# https://andydanger.github.io/live-lol-esports/#/
# https://github.com/AndyDanger/live-lol-esports/blob/main/src/utils/LoLEsportsAPI.ts
# https://github.com/vickz84259/lolesports-api-docs/tree/master
# https://vickz84259.github.io/lolesports-api-docs/#tag/leagues
# https://github.com/pedroherpeto/whatsapp-api
# https://github.com/chrishubert/whatsapp-api