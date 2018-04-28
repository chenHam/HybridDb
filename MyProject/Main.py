# MAIN PROGRAM
import MyProject.Methods.RunQueriesToDB as runQueries
import MyProject.Methods.ReadLogsFromDBToDataFrame as logs
import MyProject.Methods.CleanDb as cleanDb
import MyProject.Methods.CsvToMinimizedCsv as getGraph
if __name__ == '__main__':
    print("Start to run main function")
    # CLEAN DB
    cleanDb.clean()
    # RUN HTTP QUERIES TO WINE CELLAR
    runQueries.Run("3001")
    # GET FIRST LOGS
    logs.Run("../FilesAndInputs/DataFrame_3001_smart_queries.csv")
    # CLEAN DB
    # cleanDb.clean()
    # # RUN HTTP QUERIES TO WINE CELLAR
    # runQueries.Run("3002")
    # # GET SECOND LOGS
    # logs.Run("../FilesAndInputs/DataFrame_3002_thin_queries.csv")
    # # CREATE A GRAPH
    # getGraph.main()
    # CLUSTER
    #getCluster.Run()
    print("Finish to run all. Exit now")

