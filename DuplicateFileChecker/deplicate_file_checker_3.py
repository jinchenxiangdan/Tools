import hashlib
import os
import shutil
import sys

from os import listdir
from os.path import isfile, isdir, join, exists

#
# Author: Shawn Jin
# Purpose: 
#


# get the check sum of files 
def get_check_sum(input_path):
    # default is sha256, could be changed to md5 as need
    return hashlib.sha256(open(input_path, "rb").read()).hexdigest()


# list files under input path 
def list_files(input_path):
    return [f for f in listdir(input_path) if isfile(join(input_path, f))]


# list folders under input path, it will show invisiable files as well
def list_folders(input_path):
    return [f for f in listdir(input_path) if isdir(join(input_path, f))]


def build_hashtable(directory):

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
            # write all data to total file list 
            f = open(TOTAL_FILE_LIST_PATH, 'a')
            f.write(checksum + "\t" + file_path + "\n")
            f.close()

            if checksum in MY_HASH_TABLE:
                if file in FILE_NAME_TABLE:
                    # move to same content and same name folder
                    target = DUPLICATE_ALL_FOLDER_PATH + file_path.replace(CURRENT_WORK_SPACE, "")
                    # target_dir  = get_dir_path(target)

                    # if exists(target_dir):
                    #     # remove 
                    #     # shutil.move(file_path, target)

                    # else:
                    #     print("Folder ", target_dir ," doesn't exist, creating...")
                    #     # os.makedirs(target_dir)
                    #     # shutil.move(file_path, target)                    
                    # write to log file 
                    f = open(DUPLICATE_ALL_FILE_LIST_PATH, 'a')
                    f.write("Complete duplicate file: (with:" + FILE_NAME_TABLE[file] + ")\n move     " + file_path + "\nto      " +
                        target + "\n")
                    f.close()
     
                else:
                    # move to folder : same contant but different name folder 
                    target = DUPLICATE_CONTENT_FOLDER_PATH + file_path.replace(CURRENT_WORK_SPACE, "")
                    # target_dir  = get_dir_path(target)

                    # if exists(target_dir):
                    #     # shutil.move(file_path, target)
                    # else:
                    #     print("Folder ", target_dir ," doesn't exist, creating...")
                    #     # os.makedirs(target_dir)
                    #     # shutil.move(file_path, target)
                    # write to log file 
                    f = open(DUPLICATE_CONTENT_LIST_PATH, 'a')
                    f.write("Ignore - Duplicate content:" + target + " with(" + FILE_NAME_TABLE[MY_HASH_TABLE[checksum]] + ")\n")
                    f.close()

            else:
                if file in FILE_NAME_TABLE:

                    target = DUPLICATE_FILENAME_FOLDER_PATH + file_path.replace(CURRENT_WORK_SPACE, "")
                    # target_dir  = get_dir_path(target)

                    # if exists(target_dir):
                    #     # shutil.move(file_path, target)
                    # else:
                    #     print("Folder ", target_dir ," doesn't exist, creating...")
                    #     # os.makedirs(target_dir)
                    #     # shutil.move(file_path, target)
                    # # write to log file 
                    f =open(DUPLICATE_FILENAME_LIST_PATH, 'a')
                    f.write("Ignore - Duplicate file name: " + target + " with (" + FILE_NAME_TABLE[file] + ")\n")
                    f.close()

                else:
                    # add to hash map and move to a folder : final 
                    MY_HASH_TABLE[checksum] = file
                    FILE_NAME_TABLE[file]   = file_path
                    target = TARGET_FOLDER_PATH + "/" + file_path.split("/")[-2] + "/" + file_path.split("/")[-1]
                    # target_dir  = get_dir_path(target)

                    # if exists(target_dir):
                    #     # shutil.move(file_path, target)
                    # else:
                    #     print("Folder ", target_dir ," doesn't exist, creating...")
                    #     # os.makedirs(target_dir)
                    #     # shutil.move(file_path, target)
                    # write to log file 
                    f = open(UNIQUE_FILE_LIST_PATH, 'a')
                    f.write("Added  - Valid file: " + target + "\n")
                    f.close()

        else:
            # move to invlaid name folder 
            target      = INVALID_NAME_FOLDER_PATH + file_path.replace(CURRENT_WORK_SPACE, "")
            # target_dir  = get_dir_path(target)
            
            # if exists(target_dir):
            #     # shutil.move(file_path, target)
            # else:
            #     print("Folder ", target_dir ," doesn't exist, creating...")
            #     # os.makedirs(target_dir)
            #     # shutil.move(file_path, target)
            # write to log file 
            f = open(INVALID_FILE_LIST_PATH, 'a')            
            f.write("Ignore - Invalid name file: " + target + "\n")
            f.close()

    for folders in list_folders(directory):
        build_hashtable(directory + "/" + folders)

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
            # write all data to total file list 
            f = open(TOTAL_FILE_LIST_PATH, 'a')
            f.write(checksum + "\t" + file_path + "\n")
            f.close()

            if (checksum not in MY_HASH_TABLE and file not in FILE_NAME_TABLE):
                    print("test")
                    # move the files to a folder 
                    MY_HASH_TABLE[checksum] = file
                    FILE_NAME_TABLE[file]   = file_path
                    target = TARGET_FOLDER_PATH + "/" + file_path # + file_path.split("/")[-2] + "/" + file_path.split("/")[-1]
                    target_dir  = get_dir_path(target)

                    # if exists(target_dir):
                    #     shutil.move(file_path, target)
                    # else:
                    #     print("Folder ", target_dir ," doesn't exist, creating...")
                    #     os.makedirs(target_dir)
                    #     shutil.move(file_path, target)
                    # write to log file 
                    f = open(SOURCE_2_UNIQUE_FILE_LIST_PATH, 'a')
                    f.write("Different file found: move " + file_path + "\n to              " +
                        target + "\n")
                    f.close()
            else:
                print("duplicate file: ", file ," confirm")

        else:
            # move to invlaid name folder 
            target      = INVALID_NAME_FOLDER_PATH + file_path.replace(CURRENT_WORK_SPACE, "")
            target_dir  = get_dir_path(target)
            
            if exists(target_dir):
                shutil.move(file_path, target)
            else:
                print("Folder ", target_dir ," doesn't exist, creating...")
                os.makedirs(target_dir)
                shutil.move(file_path, target)
            # write to log file 
            f = open(INVALID_FILE_LIST_PATH, 'a')            
            f.write("Invalid file name: move " + file_path + "\nto                      " +
                target + "\n")
            f.close()

    for folders in list_folders(directory):
        check_duplicate(directory + "/" + folders)


def get_dir_path(path_to_file):
    # assert len(path_to_file) >= 2
    info_array = path_to_file.split("/")
    # print("Alert", info_array)
    info_array = info_array[0:len(info_array)-1]
    return "/".join(info_array)


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

    try:
        os.mkdir(SOURCE_2_UNIQUE_FILE_PATH)
    except FileExistsError:
        print("Directory ", SOURCE_2_UNIQUE_FILE_PATH,  "already exists.")


# global variables 
MY_HASH_TABLE                   = {}
FILE_NAME_TABLE                 = {}
CURRENT_WORK_SPACE              = os.getcwd()
OUT_DIRECTORY                   = "/mnt/d/Projects/Tools/DuplicateFileChecker/duplicate_test_folder_backup_test"
INVALID_NAME_FOLDER_PATH        = OUT_DIRECTORY + "/" + "invalid_filename_files"
DUPLICATE_FILENAME_FOLDER_PATH  = OUT_DIRECTORY + "/" + "duplicate_name_files"
DUPLICATE_CONTENT_FOLDER_PATH   = OUT_DIRECTORY + "/" + "duplicate_content_files"
DUPLICATE_ALL_FOLDER_PATH       = OUT_DIRECTORY + "/" + "duplicate_all_files"
TARGET_FOLDER_PATH              = OUT_DIRECTORY + "/" + "final"
LOG_FILE_PATH                   = OUT_DIRECTORY + "/" + "hashtable_info.out"
TOTAL_FILE_LIST_PATH            = OUT_DIRECTORY + "/" + "total_file_list.out"
DUPLICATE_CONTENT_LIST_PATH     = OUT_DIRECTORY + "/" + "duplicate_content_file_list.out"
DUPLICATE_FILENAME_LIST_PATH    = OUT_DIRECTORY + "/" + "duplicate_name_file_list.out"
DUPLICATE_ALL_FILE_LIST_PATH    = OUT_DIRECTORY + "/" + "duplicate_all_file_list.out"
INVALID_FILE_LIST_PATH          = OUT_DIRECTORY + "/" + "invalid_filename_list.out"
UNIQUE_FILE_LIST_PATH           = OUT_DIRECTORY + "/" + "unique_file_list.out"

SOURCE_2                        = ""
SOURCE_2_UNIQUE_FILE_PATH       = OUT_DIRECTORY + "/" + "source2_unique_files"
SOURCE_2_UNIQUE_FILE_LIST_PATH  = OUT_DIRECTORY + "/" + "source2_unique_files_list.out"


def main():
    # 
    # In this version, the all output is going to be OUT_DIRECTORY
    #  
    # The unique files in source 2 would be putted in "unique_file_list.out" and 

    # source1 is current working directory, source2 should be input
    # source1 = ""
    if (len(sys.argv) > 1):
        SOURCE_2 = sys.argv[1]
    else:
        SOURCE_2 = input("Input source 2: ")

    # test 
    SOURCE_2 = "/mnt/d/Projects/Tools/DuplicateFileChecker/duplicate_test_folder_backup"
    #   
    
    # get current work directory 
    current_path    = os.getcwd()
    # list all folders we need to check 
    folders         = list_folders(current_path)
    # create invlaid forlders to store invalid files 
    create_invalid_folders()
    # clear the log file & list file 
    open(LOG_FILE_PATH,                 "w").close()
    open(TOTAL_FILE_LIST_PATH,          "w").close()
    open(DUPLICATE_CONTENT_LIST_PATH,   "w").close()
    open(DUPLICATE_FILENAME_LIST_PATH,  "w").close()
    open(DUPLICATE_ALL_FILE_LIST_PATH,  "w").close()
    open(INVALID_FILE_LIST_PATH,        "w").close()
    open(UNIQUE_FILE_LIST_PATH,         "w").close()
    open(SOURCE_2_UNIQUE_FILE_LIST_PATH,"w").close()
    # recursively loop folders to build hashmap
    for folder in folders:
        build_hashtable(folder)
    # recursively loop folder to check duplicate 
    folders = list_folders(SOURCE_2)
    for folder in folders:
        check_duplicate(folder)

    # list all dict 
    f = open(LOG_FILE_PATH, "a")
    for key, value in MY_HASH_TABLE.items():
        f.write("\n" + key + " -- > " + value)
    f.write("\n")
    # list name
    for key, value in FILE_NAME_TABLE.items():
        f.write("\n" + key + " ==> " + str(value))
    f.close()

if __name__ == "__main__":
    main()
