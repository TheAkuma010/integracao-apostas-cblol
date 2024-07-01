import requests
import json
import mysql.connector
from datetime import datetime, timedelta

API_KEY = '0TvQnueqKa5mxJntVWt0w4LpLfEkrV1Ta8rQBb9Z'
API_URL_PERSISTED = 'https://esports-api.lolesports.com/persisted/gw'
API_URL_LIVE = "https://feed.lolesports.com/livestats/v1"
cblol_id = '98767991332355509'
cblol_split_2_2024_id = '112452930844731446'
confronto = 0
data_atual_str = datetime.today()
data_atual = data_atual_str.date()
dia_amanha_str = data_atual_str + timedelta(1)
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

connect = mysql.connector.connect(user='root', password='',
                                                host='localhost',
                                                database='db_bolaocblol')

cursor = connect.cursor()

# Filtrar e retornar valores de startTime
for jogo in jogos:
    start_time_str = jogo.get("startTime")

    if start_time_str:
        start_time = datetime.fromisoformat(start_time_str.rstrip('Z')).date()
        if start_time == dia_amanha:
            times_de_hoje = jogo.get("match", {}).get("teams", [])

            for times in times_de_hoje:
                time = times.get("code")
                confronto = confronto + 1
                record = (time + "\n")
                if confronto == 1:
                    with open("jogos_do_dia.txt", 'a') as file:
                        file.write(record)
                if confronto == 2:
                    with open("jogos_do_dia.txt", 'a') as file:
                        file.write(record)
                    with open("jogos_do_dia.txt", 'r') as linhas:
                        linha = linhas.readlines()
                    time1 = linha[0].strip()
                    time2 = linha[1].strip()
                    print(time1)
                    print(time2)
                    cursor.execute("INSERT INTO confrontos (time1, time2, data_jogo) VALUES (%s, %s, %s);", (time1, time2, dia_amanha))
                    connect.commit() 
                    with open("jogos_do_dia.txt", 'w') as arquivo:
                        pass
                    confronto = 0

# 120363314368602784@g.us id grupo teste
# https://andydanger.github.io/live-lol-esports/#/
# https://github.com/AndyDanger/live-lol-esports/blob/main/src/utils/LoLEsportsAPI.ts
# https://github.com/vickz84259/lolesports-api-docs/tree/master
# https://vickz84259.github.io/lolesports-api-docs/#tag/leagues
# https://github.com/pedroherpeto/whatsapp-api
# https://github.com/chrishubert/whatsapp-api