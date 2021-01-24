from flask import Flask, jsonify, request, url_for

from outputjson import *
import json
app = Flask(__name__)

@app.route('/', methods=['POST'])

def return_result():
    
    thisjson = 0
    try:
        thisjson = request.get_json(0)
        if(thisjson['splat']=="Solar"):
            return SolarRolls(thisjson)
        else:
            return "Not implemented yet"
    except:
        SolarRolls(thisjson)
    

if __name__ == '__main__':

    app.run(host='0.0.0.0',port=80)


def SolarRolls(jsonobj):
    try:
        amount = thisjson['amount']
    except:
        error = "Failed to get amount of dice you wanted to roll."
        amount = 1
    doubles=0
    try:
        doubles = thisjson['doubles']
    except:
        doubles = 10
    try:
        threshold = thisjson['threshold']
    except:
        threshold = 7
    SolarPool = new outputjson.output(amount, doubles, threshold)
    neat=json.dumps(SolarPool.dict)
    SolarPool.result = SolarPool.result[:-2]

    output = ""
    if(error == ""):
        output = jsonify({
            'results': SolarPool.result,
            'dice total': neat,
            'botch': SolarPool.successes != 0,
            'successes': SolarPool.sucs,
            'doubles': doubles
        })
    else:
        output = jsonify({
            'error': error
        })

    return output


