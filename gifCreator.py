    print('/n creating gif of existing pictures')
    system('convert -delay 10 -loop 0 ./pics/*.jpg animation.gif')
    f = open('animation.gif', 'rb')
    response = dbc.put_file('animation.gif', f)
    print('uploaded:', response)


    folder = '/path/to/folder'
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            #elif os.path.isdir(file_path): shutil.rmtree(file_path)
        except Exception as e:
            print(e)
