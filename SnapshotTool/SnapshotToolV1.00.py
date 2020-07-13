# Start of script

''' Imports '''
import random # This is an extra module
import os # This module is required to be able to delete files, or even access/scan them
# End of import list
''' Integers '''
snaSelCount = int(0) # The total snapshot selection
quitX = int(0) # Variable 1 for quitting
quitY = int(0) # Variable 2 for quitting, force-quits the terminal with a divide-by-zero error
delLock1 = int(1) # The lock for file deletion, 1 means locked, 0 means unlocked
# End of integer list
''' Functions '''
def executiveInstallOp1():
	print("Performing installer action: snapshotTool - V1.00")
	# This is the auto-execute for the SNU lite installer
# End of exectuvie install tool mode1 function
def aboutSnapshotTool():
	print("About snapshot tool\n")
	print("The SNU snapshot tool removes snapshots, and recovers them. It makes SNU a lot lighter, and removes snapshots")
	print("Snapshot tool version: 1.00 (Python 3.7.1) - April 21st 2020")
	versionHistoryConfirm1 = str(input("Do you want to see version history? (y/n)"))
	versionHistoryConfirm1 = versionHistoryConfirm1.upper()
	if (versionHistoryConfirm1 == "Y"):
		print("Snapshot tool version history")
		print("Version 1.00 - April 21st 2020")
		print("Other versions coming soon")
	else:
		noMore = input("Press [ENTER] key to go back")
# End of aboutSnapshotTool function
def confirmDelete():
	print("You are about to delete " + str(snaSelCount) + " files. You need confirmation to do this")
	delKey1 = str(input("Enter the following code to confirm the deletion: d1010d0000 : "))
	if (delKey1 == "d1010d0000"):
		delLock1 == 0
# End of confirmDelete function
def dirSelect_Root():
	print("Root directory")
	print("Modes")
	print("0D")
	print("1D")
	print("2D")
# End of dirSelect-Root function
''' Console '''
print("Welcome to the SNU Snapshot tool command line utility.")
print("Options\nRestore snapshots [ID: 1]\nDelete snapsots [ID: 2]\nAbout [ID: 3]\nCreate snapshot(s) [ID: 4]\nExit [ID: 5]")
quitO = int(0)
while (quitO == 0):
	consoleOptions1 = str(input("Enter an ID: "))
	if (consoleOptions1 == "1"):
		print("Cannot find snapshots to restore, feature coming soon")
	if (consoleOptions1 == "2"):
		print("Select a directory")
		print("Root [1]")
		print("Delete all snapshots of type Snapshot [2]")
		print("Delete all snapshots of type snapshot [3]")
		print("Delete all snapshots of type SNAPSHOT [4]")
		print("Delete all snapshots of type V# [5]")
		dirSearch1 = str(input("Enter the ID to continue"))
		if (dirSearch1 == "1"):
			print (dirSelect_Root())
		if (dirSearch1 == "2"):
			print(confirmDelete())
			#os.remove()
		if (dirSearch1 == "3"):
			print(confirmDelete())
			#os.remove()
		if (dirSearch1 == "4"):
			print(confirmDelete())
			#os.remove()
		if (dirSearch1 == "5"):
			print(confirmDelete())
			#os.remove()
		print("Delete snapshots of [type]")
	if (consoleOptions1 == "3"):
		print(aboutSnapshotTool())
	if (consoleOptions1 == "4"):
		print("Create snapshots of unarchived pages")
		print("This feature is currently unavailable")
		noMore = input("Press [ENTER] key to go back")
	if (consoleOptions1 == "5"):
		quitO + 1
		quit1 = input("Press [ENTER] key to exit")
		print(quitX / quitY)
	if not (consoleOptions1 == "1" or consoleOptions1 == "2" or consoleOptions1 == "3" or consoleOptions1 == "4"):
		print("Please enter a valid ID and try again")
		noMore = input("Press [ENTER] key to continue")
""" Notes """
# Developer notes section
'''
Update the PYTHON version counter file 
■ SnapshotTool.py
▪ Start the macro script to remove snapshot files (the first version will be written in Python and will rely on the upper() function. It will be part of the [()()()] Lite toolkit. Future versions, such as a Java, C, or other language versions are coming soon)
▪ The macro should have some CLI dialogue, such as directory selection, a range of snapshots to delete (ex: 1-75) and an option to strip the snapshot section from the page, a log viewer/creator, a restore function, a function to create snapshots of all files (files that don't have matching dates between last snapshot, and current version) and an exit function)
▪ The option to create snapshots can be removed from the lite version upon installation
▪ The option to add snapshot dates to the snapshot section, and fix snapshot file name links
▪  EVERYTHING MUST HAVE A CONFIRMATION CODE (Not just "y")
Delete file types html css py
Snapshot snapshot SNAPSHOT V all
'''
# End of script