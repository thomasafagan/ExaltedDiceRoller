from flask import Flask, jsonify, request, url_for
from random import *
import json
app = Flask(__name__)

@app.route('/', methods=['POST'])

def return_result():
    
    amount = request.get_json(0)
    doubles = amount['doubles']
    result=""
    dictionary={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0}
    sucs = 0
    botch=False

    for i in range(0,amount['amount']):
        
        temp=(randint(1,10))
        print(temp)
        result+=str(temp)+", "
        dictionary[temp]=dictionary[temp]+1
        if(temp>=7):
            if(temp==10):
                sucs+=2
            else:
                sucs+=1
    if((sucs==0) and (dictionary[1]>0)):
        botch=True
    neat=json.dumps(dictionary)
    result = result[:-2]



    return jsonify({
        'results': result,
        'dice total': neat,
        'botch': botch,
        'successes': sucs
    })
    

if __name__ == '__main__':

    app.run(host='0.0.0.0',port=80)
