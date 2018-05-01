# MAIN PROGRAM
import MyProject.Methods.RunQueriesToDB as runQueries
import MyProject.Methods.ReadLogsFromDBToDataFrame as logs
import MyProject.Methods.CleanDb as cleanDb
import MyProject.Methods.CsvToMinimizedCsv as mini
import MyProject.Methods.dfToGraphs as getGraphs


if __name__ == '__main__':
    print("Start to run main function")
    # # CLEAN DB
    #cleanDb.clean()
    # # RUN HTTP QUERIES TO WINE CELLAR
    #runQueries.Run("3001")
    # # GET FIRST LOGS
    #logs.Run("../FilesAndInputs/DataFrame_3001_fat_queries.csv")
    #mini.main("../FilesAndInputs/mainCsv-fat.csv","../FilesAndInputs/DataFrame_3001_fat_queries.csv")
    # CLEAN DB
    # cleanDb.clean()
    # # RUN HTTP QUERIES TO WINE CELLAR
    # runQueries.Run("3002")
    # # GET SECOND LOGS
    logs.Run("../FilesAndInputs/DataFrame_3002_thin_queries.csv")
    mini.main("../FilesAndInputs/mainCsv-thin.csv","../FilesAndInputs/DataFrame_3002_thin_queries.csv")
    # SMART
    # logs.Run("../FilesAndInputs/DataFrame_3001_smart_queries.csv")
    # mini.main("../FilesAndInputs/mainCsv-smart.csv","../FilesAndInputs/DataFrame_3001_smart_queries.csv")
    # # CREATE A GRAPH
    # getGraphs.main()
    # # CLUSTER
    #getCluster.Run()
    print("Finish to run all. Exit now")

