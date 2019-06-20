import json

from flask import Flask, request, Response
from src.controllers.orchestrator import purchase_product

app = Flask(__name__)


@app.route("/Hello_World", methods = ["GET"])
def Hello_World():
    return "Hello Jon!"


@app.route("/Vending_Machine/Purchase", methods = ["POST"])
def Vending_Machine_Purchase():
    request_body = request.data
    test = json.loads(request_body)
    response = purchase_product(test['ProductLocation'], test['insertedCoins'])
    test2 = json.dumps(response)
    return Response(response = test2, status = 200)



if __name__ == '__main__':
    app.run(debug=True)