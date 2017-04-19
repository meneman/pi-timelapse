
from os import system
from time import sleep
import subprocess
import dropbox

dbx = dropbox.Dropbox('3542wvbpli8AAAAAAAAYYbreqkbJFL2yV33yOz39FmSSQbAq_ywp6xVtOvjVtWal')
dbc = dropbox.client.DropboxClient('3542wvbpli8AAAAAAAAYYbreqkbJFL2yV33yOz39FmSSQbAq_ywp6xVtOvjVtWal')

while True:
    for i in range(3):
        pictureName = subprocess.check_output(['./takePic.sh'])
        picturePath = "./pics/{}.jpg".format(pictureName.strip().decode('ascii'))
        print("the answer is {}".format(picturePath))

        sleep(10)
        f = open(picturePath, 'rb')
        response = dbc.put_file(picturePath.strip('\n'), f)
        print('uploaded:', response)

    print('/n creating gif of existing pictures')
    system('convert -delay 10 -loop 0 ./pics/*.jpg animation.gif')
    f = open('animation.gif', 'rb')
    response = dbc.put_file('animation.gif', f)
    print('uploaded:', response)
    
    print('done')
