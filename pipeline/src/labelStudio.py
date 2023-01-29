import sys
import time

from subprocess import Popen
from label_studio_sdk import Client


        
class LabelStudioProject():
    def __init__(self, projectName, projectDescription, projectId, clientName, clientId, **kwargs):
        self.projectName = projectName
        self.projectDescription = projectDescription
        self.projectId = projectId
        self.clientName = clientName
        self.clientId = clientId
        self.__dict__.update(**kwargs)
        self.kwargs = kwargs
        print("Project initialized...")

    def authenticate(self, URL, API_KEY):
        # Connect to the Label Studio API and check the connection
        print('Authenticating Label Studio')
        ls = Client(url=URL, api_key=API_KEY)
        if (ls.check_connection()['status'] == "UP"):
            print("Connected")
            return ls

    def getName(self):
        return self.projectName

    def createProjectLS(self):
        print("Project being created on label-studio")
        ls = self.auth
        project = ls.start_project(
            title=self.projectName,
                label_config='''
                <View>
                    <Header value="Listen to the audio" />
                    <Audio name="audio" value="$audio" />
                    <Header value="Write the transcription" />
                    <TextArea name="transcription" toName="audio"
                        rows="4" editable="true" maxSubmissions="1" />
                </View>
                '''
            )
        project.import_tasks(
    [
        {'image': 'https://data.heartex.net/open-images/train_0/mini/0045dd96bf73936c.jpg'},
        {'image': 'https://data.heartex.net/open-images/train_0/mini/0083d02f6ad18b38.jpg'}
    ]
)