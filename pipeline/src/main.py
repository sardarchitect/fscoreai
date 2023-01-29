from requests.sessions import session
from utils import generateProjectDirectory
from labelStudio import LabelStudioProject
import threading
import sys
import time
from subprocess import Popen
import subprocess

#ADD PROJECT DATA AND SESSION SETTINGS
sessionSettings = {
    'userId' : 9915,
    'role' : 'admin',

    'projectId' : 20220526,
    'projectName' : 'TEST',
    'clientId' : 202202,
    'clientName' : 'Fscore',
    'projectDescription' : 'This is a test project that uses sample images to do bounding box annotations',
    'projectType' : 'img-bb',
    'projectDueDate' : '2022-05-30',
    'parentDirectory' : 'D:\SARDARCHITECTLABS\PROJECTS\FSCORE',
    
    'annotationTool' : 'label-studio',
    "annotationToolURL" : "http://localhost:8080",
    "annotationToolAPIKey" : "7dd53a816f5b20f6f66f0277a4ba76c636727e27", 
    }

if __name__ == "__main__":
    if sessionSettings['role'] == 'admin':
        print('Logged in as admin')
        #GENERATE PROJECT DIRECTORY IF NEEDED
        generateProjectDirectory(str(
            sessionSettings['projectId']),
            sessionSettings['projectName'], 
            sessionSettings['parentDirectory']
        )

        #START ANNOTATION SERVER
        if sessionSettings['annotationTool'] == 'label-studio':
            subprocess.call("D:\SARDARCHITECTLABS\PROJECTS\FSCORE\ADMIN\FSCORE_PROJECT_PIPELINE\src\server.py", shell=True)

        #CREATE PROJECT IN ANNOTATION TOOL
        project = LabelStudioProject(
            projectName = sessionSettings['projectName'],
            projectDescription = sessionSettings['projectDescription'], 
            projectId = sessionSettings['projectId'], 
            clientName = sessionSettings['clientName'], 
            clientId = sessionSettings['clientId'],
            )
        project.authenticate(sessionSettings['annotationToolURL'], sessionSettings['annotationToolAPIKey'])

        #IMPORT DATA IN ANNOTATION TOOL

        #EXPORT DATA FROM ANNOTATION TOOL
    
    if sessionSettings['role'] == 'tasker':
        print('Logged in as a tasker')

        #START ANNOTATION SERVER        
        if sessionSettings['annotationTool'] == 'label-studio':
            server = LabelStudioServer()

        #START AN EXISTING PROJECT
        #ANNOTATE
        #MARK PROJECT STATUS AS 'FOR REVIEW