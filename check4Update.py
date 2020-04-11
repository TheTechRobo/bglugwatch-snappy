import requests
from sys import exit
def download(filename, url): #Source: dzone.com/articles/simple-examples-of-downloading-files-using-python
    myfile = requests.get(url)
    open(filename, 'wb').write(myfile.content)
def view(url):
    changelog = requests.get(url)
    changelog = changelog.content
version = open("version", "r") #source www.guru99.com/reading-and-writing-files-in-python.html
version = version.read()
link = "http://link.to/version" #link to file with version of program
newVer = view(link)
newVer = newVer.read()
print("Latest version: ", newVer)
print("Current version: ", version)
if newVer == version:
    print("You have the latest version.")
else:
    print("There is a new version available!")
    print("Downloading it...")
    #TODO : add progress bar
    download(bglug.py, "https://raw.githubusercontent.com/TheTechRobo/bglugwatch/master/bglug.py")
    download(version, "https://raw.githubusercontent.com/TheTechRobo/bglugwatch/master/version")
    print("Success !")
    print("Please restart BGLUGwatch.")
    exit()
