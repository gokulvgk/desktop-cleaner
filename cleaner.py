import os

#creates the folders
def createFolders(rootdir, filetypes):
	for folder in filetypes.keys():
		newDirectory = rootdir + "\\" + folder
		if not os.path.exists(newDirectory):
			os.mkdir(newDirectory)


#moves the files into thier respective folders
def moveToFolder(file, rootdir, filetypes):
	#gets file format which is after the "."
	if "." in file:
		tempArray = file.split(".")
		fileFormat = tempArray[-1]
	else:
		return

	#finds the correct folder to place the file
	for folder in filetypes:
		if fileFormat in filetypes[folder]:
			scrPath = rootdir + "\\" + file
			dstPath = rootdir + "\\" + folder + "\\" + file

			if not os.path.isfile(dstPath): #makes sure no overwriting occurs
				os.rename(scrPath, dstPath)
			return


def main():
	#Folders will be divided based on the following file types
	filetypes = {"Photos":[], "Videos":[], "Audio":[], "Documents":[], \
					 "Compressed":[],"Executables":[]}

	filetypes["Photos"] = ["jpg", "jpeg", "png", "gif", "tif", "tiff", "bmp", \
	 							  "raw", "svg", "PNG"]
	filetypes["Videos"] = ["m4v", "flv", "mpeg", "mov", "mpg", "mpe", "wmv", \
								  "mp4", "MOV", "avi", "mkv"]
	filetypes["Audio"] = ["mp3", "wav", "aiff", "mid", "flac", "aac", "wma"]
	filetypes["Documents"] = ["doc", "docx", "html", "htm", "pdf", "odt", "ods", \
									  "xls", "xlsx", "ppt", "pptx", "txt", "rtf"]
	filetypes["Compressed"] = ["zip", "zipx", "7z", "rar", "tar"]
	filetypes["Executables"] = ["exe"]

	rootdir = os.getcwd()
	files = os.listdir(rootdir)
	createFolders(rootdir, filetypes)
	for file in files:
		moveToFolder(file, rootdir, filetypes)

main()
