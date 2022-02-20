from fileinput import filename
from pdf2image import convert_from_path
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import sys
import os
import os.path
from sys import exit

filename = 'something'

def pdf2img():
    i = 0
    # print(filename)
    try:
        os.chdir(sys._MEIPASS) 
        images = convert_from_path(filename,poppler_path='binary')

        for img in images:
            img.save(os.path.dirname(filename)+'\page'+str(i)+'.jpg', 'JPEG')
            i += 1
    except Exception as e:
        Result = str(e)
        messagebox.showinfo("Result", e)

    else:
        Result = "Success. Check in the same folder."
        messagebox.showinfo("Result", Result)


def browseFiles():
    global filename
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("All files",
                                                      "*.*"),("Text files",
                                                      "*.txt*"),("PDF files",
                                                      "*.pdf*")))
    label_file_explorer.configure(text="File Selected for Conversion: "+filename)


# Create the window
window = Tk()

# Set window title
window.title('File Explorer')

# Set window size
window.geometry("500x500")

# Set window background color
window.config(background="white")

# Create a Converter Label
label_file_explorer = Label(window,
                            text="PDF to Image Converter using Tkinter",
                            width=100, height=4,
                            fg="blue")


button_explore = Button(window,
                        text="Browse Files",
                        command=browseFiles)

button_convert = Button(window,
                        text="Convert PDF",
                        command=pdf2img)


button_exit = Button(window,
                     text="Exit",
                     command=exit)

label_file_explorer.grid(column=1, row=1)

button_explore.grid(column=1, row=3)

button_convert.grid(column=1, row=5)#convert button pos

button_exit.grid(column=1, row=7)



window.mainloop()

