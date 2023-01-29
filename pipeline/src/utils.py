import os

def generateProjectDirectory(projectID, projectName, parentDirectory):
    directoryName = "_".join([projectID, projectName])
    directory = os.path.join(parentDirectory,directoryName)
    if (os.path.exists(directory)) == False:
        print("Creating Project Directory...")
        os.mkdir(directory)
        dirList = [
            'ADMIN','ADMIN\CORRESPONDANCE','ADMIN\FINANCIALS','ADMIN\AGREEMENTS', 
            'DELIVERABLES', 'FILE_EXCHANGE', 'FILE_EXCHANGE\FSCORE', 'FILE_EXCHANGE\CLIENT', 
            'MEETINGS'
        ]

        for item in dirList:
            path = os.path.join(directory,item)
            os.mkdir(path)

    else:
        print("Project Directory Already Exists")