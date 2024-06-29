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
dia_amanha_str = data_atual + timedelta(1)
dia_amanha = dia_amanha_str.date()

schedule = requests.get(API_URL_PERSISTED + '/getSchedule', headers={"x-api-key":API_KEY}, params={"hl":"pt-BR", "leagueId":cblol_id})

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
        if start_time == dia_amanha:
            times_de_hoje = jogo.get("match", {}).get("teams", [])

            for times in times_de_hoje:
                time = times.get("code")
                print(time)
                confronto = confronto + 1

                if confronto == 1:        
                    connect = mysql.connector.connect(user='root', password='',
                                                host='localhost',
                                                database='db_bolaocblol')
                    cursor = connect.cursor()

                    cursor.execute("INSERT INTO confrontos (time1) VALUES {time};")
                if confronto == 2:
                    cursor.execute("INSERT INTO confrontos (time2) VALUES {time};")
                    print("")
                    confronto = 0
                    
lista = list(cursor)

for l in lista:
    var_id               = l[1]
    var_time1            = l[2]
    var_time2            = l[3]

    '''
    id
    time1
    time2
    '''
    
    print(l)
# 120363314368602784@g.us id grupo teste
# https://andydanger.github.io/live-lol-esports/#/
# https://github.com/AndyDanger/live-lol-esports/blob/main/src/utils/LoLEsportsAPI.ts
# https://github.com/vickz84259/lolesports-api-docs/tree/master
# https://vickz84259.github.io/lolesports-api-docs/#tag/leagues
# https://github.com/pedroherpeto/whatsapp-api
# https://github.com/chrishubert/whatsapp-api