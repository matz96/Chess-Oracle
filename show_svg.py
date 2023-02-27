from email.mime import image
from re import S
import tkinter as tk
import io
import glob
from PIL import Image, ImageTk
import os

import cairosvg
from attr import s
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM, renderPDF
from model_run import model_run
 
def insertfiles():
    file_number = 1
    "loads the list of files in the directory"
    for filename in glob.glob("./images/*"):
        file = ('./images/render' + f'{file_number:03}' + '.svg')
        lst.insert(file_number, file)
        file_number = file_number+1
 
 
def delete_item(event):
    "Deletes a file in the list: called by lst.bind('<Control-d>', delete_item)"
    n = lst.curselection()
    os.remove(lst.get(n))
    lst.delete(n)
 
 
def get_window_size():
    "Returns the width and height of the screen to set images and canvas alike it: called by root.bind <Configure>"
    if root.winfo_width() > 200 and root.winfo_height() >30:
        w = 800
        h = 800
    else:
        w = 200
        h = 30
    return w, h
 
 
def showimg(event):
    
    "takes the selected image to show it, called by root.bind <Configure> and lst.bind <<ListboxSelect>>"
    n = lst.curselection()
    filename = lst.get(n)
    txt1,txt2 = model_run(n[0])
    txt1=str(txt1)
    txt2=str(txt2)
    txt.set(txt1 + "\n"+txt2)
   
    cairosvg.svg2png(url=filename, write_to= "temp.png")
    
    im =Image.open("temp.png")
    im = im.resize((get_window_size()), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(im)
    w, h = img.width(), img.height()
    canvas.image = img
    canvas.config(width=w, height=h)
    canvas.create_image(0, 0, image=img, anchor=tk.NW)
    root.bind("<Configure>", lambda x: showimg(x))
  

    
    

root = tk.Tk()
root.title('Das Schachorakel')
root.geometry("800x600+300+50")
lst = tk.Listbox(root)
lst.pack(side="left", fill=tk.BOTH, expand=0)
txt = tk.StringVar() 
#lst.grid(row=0,rowspan=2,column=0,columnspan=1, sticky=tk.NW )
label = tk.Label(root, textvariable = txt, anchor=tk.SW,font=("Arial", 25))
label.pack(side="bottom")


lst.bind("<<ListboxSelect>>", showimg)
lst.bind("<Control-d>", delete_item)
#insertfiles()
canvas = tk.Canvas(root, width= 600, height=600)

canvas.pack(anchor=tk.NW)
  
#root.mainloop()