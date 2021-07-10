import requests
import os
os.chdir("blglasses")
response = requests.get("https://api.github.com/repos/TheInventionMaker/blglasses/releases/latest")
version = response.json()["tag_name"]
if(os.path.isfile(version + '.txt')):
        print("Already on current version")
else:
        print("Different version. Updating...")
        os.chdir("/home/pi")
        os.system("sudo rm -rf blglasses")
        print("Deleted old version")
        os.system("git clone https://github.com/TheInventionMaker/blglasses.git")
        print("Created new version")
        os.chdir("blglasses")
        f = open(version + ".txt","w+")
        os.system("ls") 
        print("Updating Complete.")