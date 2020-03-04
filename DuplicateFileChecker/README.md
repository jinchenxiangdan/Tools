# Duplicate File Checker 
the python version is complete version.

the java version can only check two level subdirectories



## Usage 
1. put the python script in the directory that you want to check duplication. 
2. open terminal and type `python3 duplicate_file_checker.py`
3. wait until it end


## Generated Information 
It would generate five folders and two log files. 

Folders:
- duplicate_content_files
- duplicate_name_files
- duplicate_all_files       : two files with same filename and content
- invalid_filename_files    : the files doesn't have prefix that same as current directory
- final                     : valid files*

*valid files: prefix of file name is same as the directory that it is, unique content, unique file name*

