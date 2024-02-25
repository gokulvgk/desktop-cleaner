import os
from tkinter import *
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
root = Tk()
root.title('Desktop cleaner')
root.geometry('800x800')
videocount=3
def TheButton():
    n = Label(root,text='Let start from the begining.').grid(column=10)
    

myLabel = Label(root,text='No of Video files',fg='dark blue',font='algerian').grid(row=10, column=10,padx=200)
clicked = StringVar()
clicked.set('4 Files')
drop1 = OptionMenu(root,clicked,'Video file 1','Video file 2','Video file 3','Video file 4').grid(row=10, column=11,pady=30)

myLabel2 = Label(root,text='Audio files',fg='dark blue',font='algerian').grid(row=20, column=10)
clicked = StringVar()
clicked.set('4 Files')
drop1 = OptionMenu(root,clicked,'Audio file 1','Audio file 2','Audio file 3','Audio file 4').grid(row=20, column=11)

myLabel3 = Label(root,text='Text files',fg='dark blue',font='algerian').grid(row=30, column=10)
clicked = StringVar()
clicked.set('4 Files')
drop1 = OptionMenu(root,clicked,'Text file 1','Text file 2','Text file 3','Text file 4').grid(row=30, column=11)

myLabel4 = Label(root,text='Executable files',fg='dark blue',font='algerian').grid(row=40, column=10)
clicked = StringVar()
clicked.set('4 Files')
drop1 = OptionMenu(root,clicked,'executable file 1','executable file 2','executable file 3','executable file 4').grid(row=40, column=11)

myLabel5 = Label(root,text='Image files %d'%videocount,fg='dark blue',font='algerian').grid(row=50, column=10)
clicked = StringVar()
clicked.set('4 Files')
drop1 = OptionMenu(root,clicked,'Image file 1','Image file 2','Image file 3','Image file 4').grid(row=50, column=11)

myLabel6 = Label(root,text='Documents',fg='dark blue',font='algerian').grid(row=60, column=10)
clicked = StringVar()
clicked.set('4 Files')
drop1 = OptionMenu(root,clicked,'Document 1','Document 2','Document 3','Document 4').grid(row=60, column=11)








mylab = Label(root, text='Click the button to reset the folders').grid(row=100,column=10)
mybutton = Button(root, text='Click Me',command=TheButton).grid(row=110,column=10) 




main()
root.mainloop()