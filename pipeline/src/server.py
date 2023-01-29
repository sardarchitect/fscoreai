import sys
import time
from subprocess import Popen

class LabelStudioServer():
    def __init__(self):
        processes = Popen("cmd.exe /c start" + " label-studio")
        processes.wait()
        time.sleep(10)

if __name__ == 'server':
    print('hi')

if __name__ == '__main__':
    print('testing')