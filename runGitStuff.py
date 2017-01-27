import os
import sys
import subprocess

repository = "C:\\development\\GitLabRepository\\"

repositoryFolder = ""
branch = ""

git = "C:\\Program Files\\Git\\bin\\"
command0 = "status"
command1 = "checkout OnlineReg"
command2 = "pull"
command3 = "push origin"
command4 = "commit -a -m "
getRepo = []
mydict = {}
#commitComment = ""+str(sys.argv[3])+" ["+branch+"]"


print("\n Choose Repository: \n")
print [name for name in os.listdir(repository)]

for i, name in enumerate(os.listdir(repository)):
	mydict.update({i:name})

print('\n')

chosenOption = raw_input('Specify Repo: ')

print('\n')
#chosenOption = int(chosenOption)

getRepo.append(mydict[int(chosenOption)])

getRepo.append('OnlineReg')

repositoryFolder = ""+getRepo[0]+"\\"
branch = getRepo[1]

def getStatus():
		os.system('cd '+repository+repositoryFolder+' && "'+git+'git" '+command0+'')

def writeToRepository():
		commitComment = ""+''.join(getRepo[2])+""
		os.system('cd '+repository+repositoryFolder+' && "'+git+'git" '+command4+' '+commitComment+'')

def getLatest():
		os.system('cd '+repository+repositoryFolder+' && "'+git+'git" '+command2+'')

def uploadChanges():
		os.system('cd '+repository+repositoryFolder+' && "'+git+'git" '+command3+' '+branch+'')

if raw_input('Check Status: ') == 'yes':
	print('\n')

	if getRepo[0] == 'msc-online-registration' and getRepo[1] == 'OnlineReg':
		getStatus()

elif raw_input('Write Changes to Repo: ') == 'yes':
	print('\n')
	
	comment = raw_input('Specify Comment: ').split(',')
	print('\n')

	getRepo.append(comment)
	writeToRepository()

elif raw_input('Get Latest: ') == 'yes':
	print('\n')

	if getRepo[0] == 'msc-online-registration' and getRepo[1] == 'OnlineReg':
		getLatest()


elif raw_input('Upload Changes: ') == 'yes':
	print('\n')

	if getRepo[0] == 'msc-online-registration' and getRepo[1] == 'OnlineReg':
		uploadChanges()

else:
	print('Does Not look you want to do anything :)')
	exit()
