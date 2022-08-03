from flask import Flask, jsonify, request
import ShopClues_Scraper as ssc
import Flipkart_Scraper as fsc
import Olx_Scraper as osc

app = Flask(__name__)

def getResult(query) :
    ret, ec = [], [ssc, osc, fsc]
    
    for scraper in ec :
        ret += scraper.processQuery(query)

    ret = sorted(ret, key = lambda i : (int(i['Price'][1 :].replace(',', ''))))
    print(len(ret))

    return ret


@app.route("/scraper")
def getList() :
    res = []

    args = request.args
    query = args.get('q')
    print(query)

    res = getResult(query)

    return jsonify(res)

if __name__ == '__main__':
    app.run(debug = True)
