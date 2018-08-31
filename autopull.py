from time import sleep
from os import popen
while (True):
    popen("git pull")
    sleep(120)
