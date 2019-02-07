# This python script extracts the thumbnail from youtube video

import requests
from Tkinter import *
from PIL import Image


window = Tk()
window.title("Youtube Thumbnail Gen")
window.geometry('200x200')

lbl = Label(window, text="Enter Url")
lbl.grid(column=3, row=0)

txt = Entry(window, width=10)
txt.grid(column=3, row=1)


def parse_video_string(url):
    video_id = url[32:]
    print video_id
    return video_id


def get_video_thumbnail(video_id):
    url = "https://img.youtube.com/vi/" + video_id + "/0.jpg"
    print url
    img = Image.open(requests.get(url, stream=True).raw)
    img.show()


def clicked():
    get_video_thumbnail(parse_video_string(txt.get()))


btn = Button(window, text="Download the Thumbnail", command=clicked)
btn.grid(column=3, row=3)

window.mainloop()








