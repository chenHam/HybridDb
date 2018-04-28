# MAIN PROGRAM
import MyProject.Methods.RunQueriesToDB as runQueries
if __name__ == '__main__':
    print("Start to run main function")
    # RUN HTTP QUERIES TO WINE CELLAR
    runQueries.Run()
    # GET ALL QUERIES LOG AS A FILE
    createLogQueriesFile.Run()
    # CLUSTER
    getCluster.Run()
    # GRAPHS
    getGraph.Run()
