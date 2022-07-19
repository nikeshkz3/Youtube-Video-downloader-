from fileinput import filename
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter.tix import IMAGE
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube

import shutil


#Functions
def select_path():
    #allows user to select a path from the explorer
    path = filedialog.askdirectory()
    path_label.config(text=path)



def download_file():
    #get user path
    get_link = link_field.get()
    #get selected path
    user_path = path_label.cget("text")
    screen.title('Downloading...')
    #Download Video
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    vid_clip = VideoFileClip(mp4_video)
    vid_clip.close()
    #move file to selected directory
    shutil.move(mp4_video, user_path)
    screen.title('Download Complete! ...')

    def exit():
        screen.exit()
    


screen = Tk()
title = screen.title('Youtube Downloader')
canvas = Canvas(screen, bg='grey', width=500, height=500)
my_img = PhotoImage(file='C:\\Users\\nikes\\Desktop\\yt_downloader-master\\yt_downloader-master\\png1.png')
canvas.create_image(200, 275, image=my_img)
canvas.pack()

#logo
logo_img = PhotoImage(file='C:\\Users\\nikes\\Desktop\\yt_downloader-master\\yt_downloader-master\\yt.png')
#resize
logo_img = logo_img.subsample(2, 2)
canvas.create_image(250, 80, image=logo_img)


#link field
link_field = Entry(screen, width=40, font=('Arial', 15) )
link_label = Label(screen, text="Enter Download Link: ", font=('Arial', 15))

#Select Path for saving the file
path_label = Label(screen, text="Select Path For Download", font=('Arial', 15))
select_btn =  Button(screen, text="Select Path", bg='red', padx='22', pady='5',font=('Arial', 15), fg='#fff', command=select_path)
#Add to window
canvas.create_window(250, 280, window=path_label)
canvas.create_window(250, 330, window=select_btn)

#Add widgets to window 
canvas.create_window(250, 170, window=link_label)
canvas.create_window(250, 220, window=link_field)

#Download btns
download_btn = Button(screen, text="Download File",bg='green', padx='22', pady='5',font=('Arial', 15), fg='#fff', command=download_file)
#add to canvas
canvas.create_window(250, 390, window=download_btn)

#exit
exit_btn = Button(screen, text="Exit",bg='orange', padx='15', pady='3',font=('Arial', 12), fg='#fff', command=exit)
#add to canvas
canvas.create_window(450, 470, window=exit_btn)

screen.mainloop()