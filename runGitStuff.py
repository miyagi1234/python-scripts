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
command5 = "clone"
command6 = "branch"
command7 = "branch -d"
command8 = "merge"
projUrl = ""
getRepo = []
getProjectUrl = []
myprojdict = {}
mydict = {}

# Possible next command to add will be - Add to be tracked

try:


	print("\n Choose Repository: \n")
	print [name for name in os.listdir(repository)]
	
	for i, name in enumerate(os.listdir(repository)):
		mydict.update({i:name})
	
	print('\n')
	
	chosenOption = raw_input('Specify Repo: ')
	
	print('\n')
	
	choseBranch = raw_input('Specify Branch: ')
	
	getRepo.append(mydict[int(chosenOption)])
	
	getRepo.append(choseBranch)
	
	repositoryFolder = ""+getRepo[0]+"\\"
	branch = getRepo[1]
	
	if branch == "master":
		branch = "master"
	
	def clone():
		os.system('cd '+repository+repositoryFolder+' && "'+git+'git" '+command5+' '+projUrl+'')
	
	def getStatus():
			os.system('cd '+repository+repositoryFolder+' && "'+git+'git" '+command0+'')
	
	def getStatusAlternate():
			os.system('cd '+repository+repositoryFolder+' && "'+git+'git" '+command0+' '+branch+'')
	
	def writeToRepository():
			commitComment = ""+''.join(getRepo[2])+""
			os.system('cd '+repository+repositoryFolder+' && "'+git+'git" '+command4+' '+commitComment+'')
	
	def getLatest():
			os.system('cd '+repository+repositoryFolder+' && "'+git+'git" '+command2+'')
	
	def uploadChanges():
			os.system('cd '+repository+repositoryFolder+' && "'+git+'git" '+command3+' '+choseBranch+'')
	
	def makeBranch():
		os.system('cd '+repository+repositoryFolder+' && "'+git+'git" '+command6+' '+branch+'')
	
	def deleteBranch():
		os.system('cd '+repository+repositoryFolder+' && "'+git+'git" '+command7+' '+branch+'')
	
	def merge():
		os.system('cd '+repository+repositoryFolder+' && "'+git+'git" '+command8+' '+branch+'')
	
	if raw_input("\n Clone Project: ") == "yes":
		getProjectUrl = raw_input("\n Url Please: \n")
		if getProjectUrl[0] != "":
			projUrl = getProjectUrl[0]
			clone()
	
			print('\n')
	
	elif raw_input('Check Status: ') == 'yes':
		print('\n')
	
		if getRepo[0] == 'msc-online-registration' and getRepo[1] == 'OnlineReg':
			getStatus()
		else:
			getStatusAlternate()
	
	elif raw_input('Create Branch ?: ') == 'yes':
		print('\n')
		makeBranch()
	
	elif raw_input('Delete Branch ?: ') == 'yes':
		print('\n')
		deleteBranch()
	
	elif raw_input('Merge Master or Branch: ') == 'yes':
		print('\n')
		merge()
	
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
		else:
			getLatest()
	
	
	elif raw_input('Upload Changes: ') == 'yes':
		print('\n')
	
		if getRepo[0] == 'msc-online-registration' and getRepo[1] == 'OnlineReg':
			uploadChanges()
	
			print('\n')
		else:
			uploadChanges()
	
	else:
		print('Does Not look you want to do anything :)')
		exit()
except:
	fallback()
