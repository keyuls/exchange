from flask import Flask
import os
from flask import request,render_template,make_response
import dataservice as ds
import json
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/getrates')
def getRates():
    result = ds.ratesList()
    return result

@app.route('/scrap')
def getScrap():
    ds.scrapSite()
    return 'scrap now'

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(debug=False, port=port, host='0.0.0.0')
    #app.run(debug=False, port=port, host='127.0.0.1')
