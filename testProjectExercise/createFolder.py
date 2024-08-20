import os
from time import sleep

def main():

     file = "./test_createFoler"
     mkdir(file)


def mkdir(folder_PATH):

     folder_exsiting_status = os.path.exists(folder_PATH)  # detecting whether the folder already exsit or not

     if not folder_exsiting_status:
        os.makedirs(folder_PATH)  # create the folder
        print('Folder has been created successfully.')
        sleep(0.5)
        print("PATH:", folder_PATH)
     else:
        print('Folder already existed.')
        sleep(0.5)
        print("PATH:", folder_PATH)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit()
