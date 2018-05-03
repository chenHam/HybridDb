from flask import Flask, request, json

#FLASK_APP=cluster_api.py flask run
from MyProject.Methods.random_k_means import RandomKMeans

app = Flask(__name__)

@app.route("/init", methods=['POST'])
def init():
    global cluster
    cluster = RandomKMeans()
    return "ok"

@app.route("/predict", methods=['POST'])
def predict():
    print('start predict')
    obj = request.json
    print('obj: ' + json.dumps(request.json))

    # obj = {
    #     "runningTime":2,
    #     "aCount":6,
    #     "bCount":1
    # }

    response = cluster.getPrediction(obj['runningTime'], obj['aCount'], obj['bCount'])
    print("response: " + str(response))

    return response


if __name__ == '__main__':
    app.debug = True
    init()
    app.run(port=3000)
    # predict()
