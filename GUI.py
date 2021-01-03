import cv2 as cv
import tkinter as tk
from PIL import ImageTk, Image
import tkinter.font as font

jmb = 5
lng = 3
rnd = 5


def start():
    print("The counting procedure is started")


def checkinout():
    print("Input applied")


def stop_button():
    win.destroy()
    win2.destroy()


win2 = tk.Tk()
win2.geometry("700x50")
win2.title("Live camera")

win = tk.Tk()
win.title("Pistachio Type Sorter")
label = tk.Label(win, text="Please adjust the parameters")

#Setting the windows Icons.
win.iconbitmap("ali.ico")
win2.iconbitmap("camera.ico")




#Designing the Menus

our_menu = tk.Menu(win)
win.config(menu=our_menu)
camera_setting = tk.Menu(our_menu)
our_menu.add_cascade(label='Camera Setting', menu=camera_setting)

filter_menu = tk.Menu(our_menu)
our_menu.add_cascade(label='Filters', menu=filter_menu)

Encoder_setting = tk.Menu(our_menu)
our_menu.add_cascade(label='Encoder Setting', menu=Encoder_setting)


button = tk.Button(win, text="Start", command=start, pady=15, padx=25, bg='green', fg='white', font=35)
button2 = tk.Button(win, text="Stop", fg="white", command=stop_button, pady=15, padx=25, font=35, bg='red')

#Showing the results

tex1 = "We have detected {} of JUMBO Pistachios".format(jmb)
tex2 = "We have detected {} of LONG Pistachios".format(lng)
tex3 = "We have detected {} of ROUND Pistachios".format(rnd)
label1 = tk.Label(win, text=tex1)
label2 = tk.Label(win, text=tex2)
label3 = tk.Label(win, text=tex3)

#Design a bar to define the parameters.

bar_label = tk.Label(win, text="Noise")
tresh = tk.Label(win, text="Threshold")
morph = tk.Label(win, text="Morph")

bar_label.grid(row=1, column=3)
tresh.grid(row=1, column=4)
morph.grid(row=1, column=5)

scale1 = tk.Scale(win, from_=0, to=255)
scale2 = tk.Scale(win, from_=0, to=255)
scale3 = tk.Scale(win, from_=0, to=255)

scale1.grid(row=2, column=3)
scale2.grid(row=2, column=4)
scale3.grid(row=2, column=5)








canvas = tk.Canvas(win2, width=2000, height=244)
canvas.grid(row=1, column=1)
img = ImageTk.PhotoImage(Image.open("3.jpg"))
canvas.create_image(20, 20, anchor='nw', image=img)


button.grid(row=2, column=1, sticky=tk.W)
button2.grid(row=3, column=1, sticky=tk.W)

label1.grid(row=8, column=2)
label2.grid(row=9, column=2)
label3.grid(row=10, column=2)

label.grid(row=0, column=2, columnspan=4)
#button.pack(side=tk.LEFT)
#button2.pack(side=tk.RIGHT)

#label1.pack(side=tk.LEFT)
#label2.pack(side=tk.LEFT)
#label3.pack(side=tk.LEFT)

#label.pack()
win.mainloop()
win2.mainloop()


