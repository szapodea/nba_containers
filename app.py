from flask import Flask, request, jsonify
import requests


app = Flask(__name__)


#file where api key is stored
api_file = open('api_key.txt')
api_key = api_file.read()


@app.route('/date')
def getGames():
    date = request.args.get('date')

    url = "https://v2.nba.api-sports.io/games"

    querystring = {"date": date}
    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "api-nba-v1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    games = response.json()
    #print(games, type(games))
    ret = []
    for gm in games['response']:
        away = gm['teams']['visitors']['name']
        home = gm['teams']['home']['name']
        ret.append('{0} Vs {1}'.format(home, away))

    return {'Home Vs Away': ret}



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8082, debug=True)