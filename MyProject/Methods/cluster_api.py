from flask import Flask, request, json

#FLASK_APP=cluster_api.py flask run

app = Flask(__name__)

@app.route("/init", methods=['POST'])
def init():
    global cluster
    #cluster = RandromKMeans();
    cluster = 1
    return "1"

@app.route("/predict", methods=['POST'])
def predict():
    print('start predict')
    obj = request.json
    print('obj: ' + json.dumps(request.json))
    response = cluster.predict(obj.runningTime, obj.aCount, obj.bCount)
    print("response: " + str(response))

    return response


if __name__ == '__main__':
    app.debug = True
    app.run(port=3000)