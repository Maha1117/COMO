# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 18:24:08 2022

@author: hmahal
"""
from detoxify import Detoxify
from flask import Flask, request, jsonify
predictor = Detoxify('multilingual')
app = Flask(__name__)
@app.route("/")
def home():
    return "Hello, World!"
    
@app.route("/entity_tagging",methods=['POST'])
def entity_tagging():
        data = request.get_json()
        sentence=data['input_text']
        results = predictor.predict(sentence)
        #results1 = Detoxify('original').predict(sentence)
        #results2 = Detoxify('unbiased').predict(sentence)

        #store = results['toxicity']
        del results['toxicity']
        res=max(zip(results.values(), results.keys()))[1]
        return jsonify({"entity_tagging":res.title(),"toxicity":str(results.values())})
    
if __name__ == "__main__":
    port=8090
    app.run(debug=True,port=port)
