import sys
import os
import re
import time
import datetime
import subprocess

currentTime = time.time()

# CONVERT UNIX DATE INTO NORMAL HUMAN READABLE DATE
humanDate = datetime.datetime.fromtimestamp(currentTime).strftime('%Y_%m_%d_%H_%M_%S')

# DIRECTORY WE GOING TO STORE THE DATABASE BACKUPS IN
directory = 'C:\\Users\\trasb\\Desktop\\DB_BACKUP_FOLDER\\'

# NAME OF THE SOURCE FILE TO USE FOR LOOPING THROUGH
myfile = 'db_list.txt'

# SQL QUERY TO GET THE INITIAL LIST TO MAKE THE BACKUP FROM
getDB = os.popen('C:\\wamp\\bin\\mysql\\mysql5.7.10\\bin\\mysql -u root "information_schema" -e "SELECT SCHEMA_NAME AS \'\' FROM SCHEMATA WHERE SCHEMA_NAME NOT REGEXP \'information|sys|backup|mysql|test|performance_schema\'"').read()

# REMOVE BLANK LINES FROM LIST
getDB = re.sub('^\s*$','\n',getDB.strip())

# CHECK IF THE FOLDER EXISTS IF IT DOES NOT THEN CREATE THE FOLDER
if not os.path.exists(directory):
		os.makedirs(directory)

# WRITE OUR LIST TO THE DIRECTORY CREATED
result = open(directory + myfile, 'w')

result.write(getDB)

# CLOSE THE FILE HERE, IF ITS NOT DONE THEN YOU WONT GET ANY DATA RETURNED
result.close()


# THIS PART BEGINS THE BACKUP PROCESS OF ALL THE DATABASES
with open('C:\\Users\\trasb\\Desktop\\DB_BACKUP_FOLDER\\db_list.txt', 'r') as file:
	for line in file.xreadlines():
		output = ""+directory+""+humanDate+"_"+line+ "_" + humanDate +""
		output = re.sub(r'\n', '.sql', output)
		line =  re.sub(r'\n', '', line)
		shit = "C:\\wamp\\bin\\mysql\\mysql5.7.10\\bin\\mysqldump -u root " + line + " > " + output + ".sql"
		zipit = 'gzip '+output+'.sql'
		with open(output, 'w') as final:
			os.popen(shit)
			os.popen(zipit)


# GET LIST OF ALL FILES IN THE DIRECTORY AND REMOVE POSSIBLE HIDDEN FILES
list_files = [x for x in os.listdir(directory) if x[0]!='.']


# NOW LOOP THROUGH THE FILES AND REMOVE EMPTY ONES
for each_file in list_files:
    file_path = '%s/%s' % (directory, each_file)

    # CHECK SIZE AND DELETE IF 0
    if os.path.getsize(file_path)==0:
        os.remove(file_path)
    else:
    		name, ext = os.path.splitext(file_path)
    		if ext == '.sql':
    			os.remove(file_path)
