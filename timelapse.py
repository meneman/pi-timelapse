
from os import system
from time import sleep
import subprocess
import dropbox
import json
import os, shutil

f = open("timelapse.json", "r")
config = json.loads(f.read())
f.close()



dbc = dropbox.client.DropboxClient(config["accessKey"])

while True:
	for i in range(3):
		pictureName = subprocess.check_output(['./takePic.sh'])
		picturePath = "./pics/{}.jpg".format(pictureName.strip().decode('ascii'))
		print("A Picture was taken and saved at {}".format(picturePath))

		sleep(61)
		f = open(picturePath, 'rb')
		response = dbc.put_file(picturePath.strip('\n'), f)
		print('The Picture was uploaded:', response)


		os.remove(picturePath)
		print("The Picture was removed localy")
