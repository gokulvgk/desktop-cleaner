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


													#  GUI code starts here

root = Tk()
root.title('Desktop cleaner')
root.geometry('800x800')
videocount=3
root.configure(bg="#FAEBD7")
def TheButton():
    n = Label(root,text='Let start from the begining.').grid(column=10)
    
option1 = ['Video file 1',
           'Video file 2',
           'Video file 3',
           'Video file 4']
myLabel = Label(root,text='Video files',fg='dark blue',bg='#FFE4C4',font='algerian').grid(row=10, column=10,padx=200)
clicked = StringVar()
clicked.set('4 Files')
drop1 = OptionMenu(root,clicked,*option1).grid(row=10, column=11,pady=0)

option2 = ['Audio file 1',
           'Audio file 2',
           'Audio file 3',
           'Audio file 4']
myLabel2 = Label(root,text='Audio files',fg='dark blue',bg='#FFE4C4',font='algerian').grid(row=20, column=10)
clicked = StringVar()
clicked.set('4 Files')
drop1 = OptionMenu(root,clicked,*option2).grid(row=20, column=11)

option3 = ['Text file 1',
           'Text file 2',
           'Text file 3',
           'Text file 4']
myLabel3 = Label(root,text='Text files',fg='dark blue',bg='#FFE4C4',font='algerian').grid(row=30, column=10)
clicked = StringVar()
clicked.set('4 Files')
drop1 = OptionMenu(root,clicked,*option3).grid(row=30, column=11)

option4 = ['Executable file 1',
           'Executable file 2',
           'Executable file 3',
           'Executable file 4']
myLabel4 = Label(root,text='Executable files',fg='dark blue',bg='#FFE4C4',font='algerian').grid(row=40, column=10)
clicked = StringVar()
clicked.set('4 Files')
drop1 = OptionMenu(root,clicked,*option4).grid(row=40, column=11)

option5 = ['Image file 1',
           'Image file 2',
           'Image file 3',
           'Image file 4']
myLabel5 = Label(root,text='Image files',fg='dark blue',bg='#FFE4C4',font='algerian').grid(row=50, column=10)
clicked = StringVar()
clicked.set('4 Files')
drop1 = OptionMenu(root,clicked,*option5).grid(row=50, column=11)

option6 = ['Document 1',
           'Document 2',
           'Document 3',
           'Document 4']
myLabel6 = Label(root,text='Documents',fg='dark blue',bg='#FFE4C4',font='algerian').grid(row=60, column=10)
clicked = StringVar()
clicked.set('4 Files')
drop1 = OptionMenu(root,clicked,*option6).grid(row=60, column=11)









mylab = Label(root, text='Click the button to reset the folders').grid(row=100,column=10)
mybutton = Button(root, text='Click Me',command=TheButton).grid(row=110,column=10) 





main()
root.mainloop()