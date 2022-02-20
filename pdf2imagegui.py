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
    i = 1
    try:
        os.chdir(sys._MEIPASS) 
        images = convert_from_path(filename,poppler_path='binary')

        for img in images:
            img.save(os.path.dirname(filename)+'\\'+os.path.splitext(os.path.basename(filename))[0]+str(i)+'.jpg', 'JPEG')
            i += 1
    except Exception as e:
        Result = "No PDF selected/Some Error Occured"
        messagebox.showinfo("Result", Result)

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
                            text="PDF to Image Converter using Python <3",
                            width=75, height=10,
                            fg="blue")

#select files button
button_explore = Button(window,
                        text="Browse Files",
                        command=browseFiles)

button_convert = Button(window,
                        text="Convert PDF",
                        command=pdf2img, height=5, width=20, bg="#745ead", fg="white")


button_exit = Button(window,
                     text="Exit",
                     command=exit, width=10, bg="#cc4141")

label_file_explorer.grid(column=1, row=1)

button_explore.grid(column=1, row=3,pady=10)

button_convert.grid(column=1, row=5,pady=10)#convert button pos

button_exit.grid(column=1, row=7)



window.mainloop()

