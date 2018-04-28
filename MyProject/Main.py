# MAIN PROGRAM
import MyProject.Methods.RunQueriesToDB as runQueries
import MyProject.Methods.ReadLogsFromDBToDataFrame as graph
import MyProject.Methods.CleanDb as cleanDb
if __name__ == '__main__':
    print("Start to run main function")
    # CLEAN DB
    cleanDb.clean()
    # RUN HTTP QUERIES TO WINE CELLAR
    runQueries.Run()
    # GET ALL QUERIES LOG AS A FILE AND CREATE A GRAPH
    graph.Run()
    # CLUSTER
    #getCluster.Run()
    print("Finish to run all. Exit now")

