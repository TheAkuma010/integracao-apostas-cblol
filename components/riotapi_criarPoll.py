import requests
import json
import mysql.connector

API_KEY = 'akumabot'
session_id = 'akumabot'
WPP_API_URL = 'http://localhost:3000'

connect = mysql.connector.connect(user='root', password='',
                                                host='localhost',
                                                database='db_bolaocblol')

cursor = connect.cursor()
cursor.execute("SELECT * FROM confrontos WHERE confrontos.EXEC = 'NAO'")

lista = list(cursor)

for l in lista:
    var_id               = l[0]
    var_time1            = l[1]
    var_time2            = l[2]

    '''
    id
    time1
    time2
    '''

    criarPoll = {
    "chatId": "120363314368602784@g.us",
    "contentType": "Poll",
    "content": {
      "pollName": f"{var_time1} vs {var_time2}",
      "pollOptions": [
        f"{var_time1}", 
        f"{var_time2}"
      ],
      "options": {
        "allowMultipleAnswers": False
      }
    }
    }
    mensagem = {
        "chatId": "120363314368602784@g.us",
        "contentType": "Poll",
        "content": {
            "pollName": "TESTE?",
            "pollOptions": [
                "Cats",
                "Dogs"
            ],
            "options": {
                "allowMultipleAnswers": True
            }
        }
    }
    
#     mensagem = {
#   "chatId": "5521996773500@c.us",
#   "contentType": "string",
#   "content": f"{var_time1} vs {var_time2}"
#     }


    
    
    # with open("criarPoll.json", 'w') as file:
    #     json.dump(mensagem, file, indent=4)
        
    with open('criarPoll.json', 'r') as jsonread:
        poll = json.load(jsonread)
    
    print(poll)
    print(var_time1 + " vs " + var_time2)
    enviarPoll = requests.post(WPP_API_URL + '/client/sendMessage/' + session_id, headers={"x-api-key":API_KEY}, data=(poll))
    
    if enviarPoll.status_code == 200:
        print("Poll sent successfully.")
    else:
        print(f"Failed to send poll. Status code: {enviarPoll.status_code}, Error: {enviarPoll.text}")
        
    # with open("criarPoll.json", 'w') as outfile:
    #     pass
    
# 120363314368602784@g.us id grupo teste
# https://andydanger.github.io/live-lol-esports/#/
# https://github.com/AndyDanger/live-lol-esports/blob/main/src/utils/LoLEsportsAPI.ts
# https://github.com/vickz84259/lolesports-api-docs/tree/master
# https://vickz84259.github.io/lolesports-api-docs/#tag/leagues
# https://github.com/pedroherpeto/whatsapp-api
# https://github.com/chrishubert/whatsapp-api