import hashlib
import os
from os import listdir
from os.path import isfile, isdir, join

#
# Author: Shawn Jin
#
#



# get the check sum of files 
def get_check_sum(input_path):
    # default is md5, could be changed to sha256 as need
    return hashlib.md5(open(input_path, "rb").read()).hexdigest()


# list files under input path 
def list_files(input_path):
    return [f for f in listdir(input_path) if isfile(join(input_path, f))]


# list folders under input path, it will show invisiable files as well
def list_folders(input_path):
    return [f for f in listdir(input_path) if isdir(join(input_path, f))]


def check_duplicate(directory):

    files = list_files(directory)
    print("Working directory is ", directory)
    prefix = directory.strip().split("/")[-1]
    # print("prefix is ", prefix)
    for file in files:
        # print("file is ", file)
        file_path = os.getcwd() + "/" + directory + "/" +file
        # check if the file name is valid or not 
        if file.startswith(prefix):
            checksum = get_check_sum(file_path)

            if checksum in MY_HASH_TABLE:
                if file in FILE_NAME_TABLE:
                    # move to same content and same name folder
                    f =open(LOG_FILE_PATH, 'a')
                    f.write("Complete duplicate file: move " + file_path + "\nto                            " +
                        DUPLICATE_ALL_FOLDER_PATH + file_path.replace(CURRENT_WORK_SPACE, "") + "\n")
                    f.close()
                else:
                    # move to folder : same contant but different name folder 
                    f =open(LOG_FILE_PATH, 'a')
                    f.write("Same content: (with " + MY_HASH_TABLE[checksum] +")\n move " + file_path + "\n to   " +
                        DUPLICATE_CONTENT_FOLDER_PATH + file_path.replace(CURRENT_WORK_SPACE, "") + "\n")
                    f.close()
            else:
                if file in FILE_NAME_TABLE:
                    f =open(LOG_FILE_PATH, 'a')
                    f.write("Same filename: move " + file_path + "\nto                  " +
                        DUPLICATE_FILENAME_FOLDER_PATH + file_path.replace(CURRENT_WORK_SPACE, "") + "\n")
                    f.close()
                else:
                    # add to hash map and move to a folder : final 
                    MY_HASH_TABLE[checksum] = file
                    FILE_NAME_TABLE[file]   = 1
                    f =open(LOG_FILE_PATH, 'a')
                    f.write("Valid File: move " + file_path + "\n to              " +
                        TARGET_FOLDER_PATH + file_path.replace(CURRENT_WORK_SPACE, "") + "\n")
                    f.close()
        else:
            # move to invlaid name folder 
            f =open(LOG_FILE_PATH, 'a')
            f.write("Invalid file name: move " + file_path + "\nto                      " +
                INVALID_NAME_FOLDER_PATH + file_path.replace(CURRENT_WORK_SPACE, "") + "\n")
            f.close()

    for folders in list_folders(directory):
        check_duplicate(directory + "/" + folders)


# create 4 folders that would be store all files. 
def create_invalid_folders():


    # build directory
    try:
        os.mkdir(INVALID_NAME_FOLDER_PATH)
    except FileExistsError:
        print("Directory ", INVALID_NAME_FOLDER_PATH, "already exists.")

    try:
        os.mkdir(DUPLICATE_FILENAME_FOLDER_PATH)
    except FileExistsError:
        print("Directory ", DUPLICATE_FILENAME_FOLDER_PATH,  "already exists.")

    try:
        os.mkdir(DUPLICATE_CONTENT_FOLDER_PATH)
    except FileExistsError:
        print("Directory ", DUPLICATE_CONTENT_FOLDER_PATH,  "already exists.")
    
    try:
        os.mkdir(DUPLICATE_ALL_FOLDER_PATH)
    except FileExistsError:
        print("Directory ", DUPLICATE_ALL_FOLDER_PATH,  "already exists.")

    try:
        os.mkdir(TARGET_FOLDER_PATH)
    except FileExistsError:
        print("Directory ", TARGET_FOLDER_PATH,  "already exists.")


# global variables 
MY_HASH_TABLE                   = {}
FILE_NAME_TABLE                 = {}
CURRENT_WORK_SPACE              = os.getcwd()
INVALID_NAME_FOLDER_PATH        = CURRENT_WORK_SPACE + "/" + "invalid_filename_files"
DUPLICATE_FILENAME_FOLDER_PATH  = CURRENT_WORK_SPACE + "/" + "duplicate_name_files"
DUPLICATE_CONTENT_FOLDER_PATH   = CURRENT_WORK_SPACE + "/" + "duplicate_content_files"
DUPLICATE_ALL_FOLDER_PATH       = CURRENT_WORK_SPACE + "/" + "duplicate_all_files"
TARGET_FOLDER_PATH              = CURRENT_WORK_SPACE + "/" + "final"
LOG_FILE_PATH                   = CURRENT_WORK_SPACE + "/" + "duplicate_checker_log"


def main():


    # get current work directory 
    current_path = os.getcwd()
    # create invlaid forlders to store invalid files 
    create_invalid_folders()
    # clear the log file
    open(LOG_FILE_PATH, "w").close()


    # test area 
    # print("start...")
    # print("path folders: ", list_folders(current_path))
    # print("path files: ", list_files(current_path))
    # end test area 
    folders = list_folders(current_path)
    for folder in folders:
        check_duplicate(folder)


    # list all dict 
    f = open(LOG_FILE_PATH, "a")
    for key, value in MY_HASH_TABLE.items():
        # print(key, " --> ", value)
        f.write("\n" + key + " -- > " + value)
    f.write("\n")
    # list name
    for key, value in FILE_NAME_TABLE.items():
        # print(key, " ==> ", value)
        f.write("\n" + key + " ==> " + str(value))
    f.close()

if __name__ == "__main__":
    main()