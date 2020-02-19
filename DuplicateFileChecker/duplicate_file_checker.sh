#!/bin/bash

# Author: Shawn Jin

#
# functions 
#
function print_my_hashtable {
    for KEY in ${!MY_HASHTABLE[@]}; do 
        echo "$KEY - ${MY_HASHTABLE[$KEY]}"
        # echo "key is $KEY."
    done
}





#
# check and initial log file 
#
log_file="duplicate_log.out"
initial_directory=$(pwd)
log_file="$initial_directory"/"$log_file"

if [[ -e $log_file ]]; then
    echo "" > "$log_file"
fi 

#
# read input parameters 
#
target_file="."
if [[ $# -eq 0 ]]; then
    echo "Target file is current directory." >> "$log_file"
elif [[ $# -eq 1 ]]; then
    # check if it is directory
    if [[ ! -d $1 ]]; then 
        echo "Error: target folder is NOT a directory!"
        echo "Usage: bash duplicate_file_checker [target directory]"
        exit
    fi
    # target_file=$(basename $1)
    # check and remove the directory mark "/"
    # if [[ $target_file == */ ]]; then 
    #     target_file="${target_file::-1}"
    # fi
    target_file=$1
    echo "Target file is "$target_file"." >> "$log_file"
else
    echo "Usage: bash duplicate_file_checker [target directory]"
    exit
fi

#
# ssh information
#
hostname=""


#
# create a hash table 
#
declare -A MY_HASHTABLE



# 
# check the names of directory
#   - The prefix of file names are same as the folder's name
#   - Store in a hash if the filename is valid  
#

# move to target directory
cd $target_file
# get current diretory name 
current_directory_name=$(basename $(pwd))
echo "moved to $current_directory_name" >> "$log_file"
# create a folder to store 
invalid_name_folder="invalid_name_files"
if [[ ! -e $invalid_name_folder ]]; then 
    mkdir $invalid_name_folder
fi
invalid_name_folder="$(pwd)"/"$invalid_name_folder"
echo "created invalid_name_folder: $invalid_name_folder"
# check prefix of file name
for FILE in $(find * -maxdepth 1 -type f); do 
    # check if the name is invalid or not 
    if [[ $(cut -d'_' -f1 <<< $FILE) != $current_directory_name ]]; then 
    # if the name is invalid, mv the file to the invalid_name_folder
        # mv $FILE $invalid_name_folder
            # echo "cut is $(cut -d'_' -f1 <<< $FILE)"
        echo "Found invalid file: $FILE, moving to $invalid_name_folder/..." >> "$log_file"
    else 
    # else add files with valid name into hash
        checksum=($(md5sum $FILE))
        echo "going to add $FILE to hashtable ($checksum)" >> $log_file

        if [[ ${MY_HASHTABLE[$checksum]} == "" ]]; then 
            echo "Found a same file!"
        else 
            MY_HASHTABLE[$checksum]=$FILE
            echo "added $FILE to hashtable" >> $log_file
        fi

        
    fi

done

# list the hashtable 
print_my_hashtable

#
# check & compare the files checksum
#


#
# put it into a hashtable 
# 


close
echo "Done."


