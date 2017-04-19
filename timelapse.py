
from os import system
from time import sleep
import subprocess
import dropbox
import os, shutil

#dbx = dropbox.Dropbox('3542wvbpli8AAAAAAAAYYbreqkbJFL2yV33yOz39FmSSQbAq_ywp6xVtOvjVtWal')
dbc = dropbox.client.DropboxClient('3542wvbpli8AAAAAAAAYYbreqkbJFL2yV33yOz39FmSSQbAq_ywp6xVtOvjVtWal')

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
    
