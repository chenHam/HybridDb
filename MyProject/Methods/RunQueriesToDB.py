# import random
# import sys
# from multiprocessing import Pool
# from pip._vendor import requests
# import time
# import json
# import MyProject.Methods.GetLearningModifyTime as tfm
# import datetime
# from datetime import datetime
# import MyProject.FilesAndInputs.winesArrayAsJson as wines
# #from test import ScheduledTask
#
# def insertQuery(wine,port):
#     r = requests.post("http://193.106.55.134:"+port+"/wines", data=wine)
#     print("insert return: ",r.status_code, r.reason," port: ",port)
#
# def getQuery(wine,port):# small 3002. big 3001
#     r = requests.post("http://193.106.55.134:"+port+"/getwines/",data=wine, timeout = 999999)
#     print("get return: ",r.status_code, r.reason," port: ",port)
#
# def updateQuery(wine1,wine2,port):
#     headers = {'Content-Type': 'application/json'}
#     data = [wine1, wine2]
#     r = requests.put(url="http://193.106.55.134:"+port+"/wines",  json=data, headers = headers)
#     print("update return: ",r.status_code, r.reason," port: ",port)
#
#
# def runUpdateQuery(distribution,windowTime,port):
#     timeInSec=windowTime*60
#     queryInterval=timeInSec/distribution
#     for i in range(0, distribution):
#         time.sleep(queryInterval)
#         numOfWine1 = random.randint(0, 23)
#         numOfWine2 = random.randint(0, 23)
#         print("Run update query number  " + str(i)+"...")
#         updateQuery(wines.wines[numOfWine1],wines.wines[numOfWine2],port)
#
# def runGetQuery(distribution,windowTime,queryWineSize,port):
#   timeInSec = windowTime * 60
#   queryInterval = timeInSec / distribution
#
#   sc = ScheduledTask(distribution)
#
#   sc.runTask(getQuery, queryInterval, args = [wines.wines2[queryWineSize],port])
#
#   while sc.isDone() == False:
#       time.sleep(1)
#
#   # for i in range(0, distribution):
#   #   time.sleep(queryInterval)
#   #   print("Run get-big query number  "+str(i)+"...")
#   #   getQuery(wines.wines2[queryWineSize],port)
#
#
#
#
#
# def runInsertQuery(distribution,windowTime,port):
#   timeInSec = windowTime * 60
#   queryInterval = timeInSec / distribution
#   for i in range(0, distribution):
#     time.sleep(queryInterval)
#     numOfWine1 = random.randint(0, 23)
#     print("Run insert query number  "+str(i)+"...")
#     insertQuery(wines.wines[numOfWine1],port)
#
# def runFunc(params):
#     startTime = datetime.now()
#     if(len(sys.argv)<2):
#         print("Insert arguments !!!!")
#         exit(1)
#     dists=json.loads(sys.argv[1])
#     actionIterations=len(dists)
#     windowTime = int(sys.argv[2])
#     numOfIterations=int(sys.argv[3])
#     for i in range(0,numOfIterations):
#         print(params[0]," iteration: ",i)
#         for i in range(0, actionIterations):
#           nowtime=datetime.now()
#           if(sys.argv[4]=="1"):
#             port=initialPort((nowtime-startTime).total_seconds())
#           else:
#               port=params[1]
#           if (params[0] == "getBig"):
#             runGetQuery(dists[i][0],windowTime,1,port)
#           elif (params[0] == "getSmall"):
#             runGetQuery(dists[i][1], windowTime,0,port)
#           elif (params[0] == "insert"):
#             runInsertQuery(dists[i][2],windowTime,port)
#           elif (params[0] == "update"):
#             runUpdateQuery(dists[i][3],windowTime,port)
#           else:
#             print("Unknown command !!")
#
# def initialPort(time):
#     res=tfm.getPrediction(time)
#     if(res=="fat"):
#       print("initial port: 3002")
#       return "3002"
#     else:
#         print("initial port: 3001")
#         return "3001"
#
# def Run(thePort):
#     print("----------Start to Run all the queries----------")
#     p = Pool(2)
#     p.map(runFunc, [["getBig",thePort],["getSmall",thePort]]) # OPTIONAL TO ADD :: ,"insert","update"
#     print("----------Finish to Run all the queries----------")
