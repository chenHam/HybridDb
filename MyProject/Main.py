# MAIN PROGRAM
import MyProject.Methods.RunQueriesToDB as runQueries
import MyProject.Methods.ReadLogsFromDBToDataFrame as graph
if __name__ == '__main__':
    print("Start to run main function")
    # RUN HTTP QUERIES TO WINE CELLAR
    runQueries.Run()
    # GET ALL QUERIES LOG AS A FILE AND CREATE A GRAPH
    graph.Run()
    # CLUSTER
    getCluster.Run()

