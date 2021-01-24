from flask import Flask, jsonify, request, url_for

import outputjson
import json
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
@app.route('/', methods=['POST'])

def homepage():
    
    thisjson = 0
    try:
        thisjson = request.get_json(0)
        print(thisjson)
        if((thisjson['splat']).lower()=="solar"):
            return SolarRolls(thisjson)
        else:
            return jsonify({
                'Error': "Not implemented yet"
            })
    except:
        return SolarRolls(thisjson)


def SolarRolls(jsonobj):
    error=""
    amount = 0
    try:
        amount = jsonobj['amount']
        if(amount>100):
            return jsonify({
                'Error':"Yeah, fucking right"
            })
    except:
        error = "Failed to get amount of dice you wanted to roll."
        
    doubles=0
    try:
        doubles = jsonobj['doubles']
    except:
        doubles = 10
    try:
        threshold = jsonobj['threshold']
    except:
        threshold = 7
    SolarPool = outputjson.output(amount, doubles, threshold)
    neat=SolarPool.dict
    SolarPool.result = SolarPool.result[:-2]

    output = ""
    if(error == ""):
        output = jsonify({
            'individual_dice': SolarPool.result,
            'count_of_each_result': neat,
            'botch': SolarPool.successes == 0 and SolarPool.dict[1]>0,
            'successes': SolarPool.successes,
            'doubles': doubles
        })
    else:
        output = jsonify({
            'error': error
        })

    return output


@app.route('/help', methods=['POST'])
def helppage():
    return json.load(open('help.json','r'))

    
@app.route('/', methods=['GET'])
def noobpage():
    return "Get out of here, NOOOB."
if __name__ == '__main__':

    app.run(host='0.0.0.0',port=443, debug=True, ssl_context='adhoc')

