import instagram_explore as ie
import webbrowser, requests, time, os
import pyautogui as pag
import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image
import urllib2 as urllib
import io

from win32api import GetSystemMetrics

WIDTH = GetSystemMetrics(0)
HEIGHT = GetSystemMetrics(1)
IMG_DIMENSIONS = 400

# Padding
body_pad_x = 20
body_pad_y = 10
frame_center = (WIDTH/2) - (IMG_DIMENSIONS/2) - body_pad_x # 
frame_pad_y = 40

#image = ie.media_image('B0ota_DnqoU').data
#print(image)

#response = requests.get(image)
#img = Image.open(BytesIO(response.content))

#self = Tk()
#self.grid()
#self.geometry("+250+150")
#self.title("IG Explore")

#spacer_frame = ttk.Frame(self)
#spacer_frame.grid(pady=10)

#body_frame = ttk.Frame(self)
#body_frame.grid(padx=20, pady=10)

#header_div = ttk.Frame(body_frame)
#header_div.grid()
#Label(header_div, text = "Yuuurd", font = "System 16 bold").grid()

#ones_div = ttk.Frame(body_frame)
#ones_div.grid()

#print(image)
#webbrowser.open(image)


# Search tag name
#res = ie.media('Bz61klMHuRn').data
#print(res)

def popup():
    f = open("comments.txt", "a")
    f.write(comment_e.get() + "\n")


root = Tk()
root.grid()
root.title("Tkinter window")
root.geometry("1920x1080")

body_frame = ttk.Frame(root)
body_frame.grid(padx=body_pad_x, pady=body_pad_y)

img_frame = ttk.Frame(body_frame)
img_frame.grid(padx= frame_center, pady=frame_pad_y)

fd = urllib.urlopen("")
image_file = io.BytesIO(fd.read())
im = Image.open(image_file)

load = Image.open('C:/Users/wooda/Desktop/Wowdee/comicbrand.jpg')
load = load.resize((IMG_DIMENSIONS, IMG_DIMENSIONS), Image.ANTIALIAS)
render = ImageTk.PhotoImage(load)
img = Label(img_frame, image=render)
img.image = render
img.grid()

comment_e = ttk.Entry(body_frame, width=60)
comment_e.grid()
comment_e.focus()

submit = ttk.Button(body_frame, text="Submit", width=20, command=popup)
cancel = ttk.Button(body_frame, text="Cancel", width=20)

submit.grid(row=3)


root.mainloop()

#def list_after_every(string, keyword): 
#    li = list(string.split(keyword)) # Split the string at every occurence of keyword
#    return li

#newres = list_after_every(res, 'shortcode')[1:] # Remove the element before any shortcodes
#shortcodes = []

#for substring in newres:
#    shortcodes.append(substring[4:15]) # Pull shortcode substring without starting quotations 

#for codes in shortcodes:
#    if shortcodes.count(codes) > 1: # If there is < 1 occurence of shortcode... 
#        shortcodes.remove(codes) # ...remove an occurence of shortcode 
#print("shortcodes:\n", shortcodes)

#for posts in shortcodes:
#    post_data = str(ie.media(posts).data)



# Search user name
#res = ie.user('plus.ultron').data
#print(res)

## Next page
#data, cursor = ie.user('plus.ultron', res.cursor)

## Image only
#images = ie.user_images('plus.ultron').data

#print(res.count('\''))
#print(res.index('shortcode'))
## Next page
#data, cursor = ie.tag('wamdrawthis', res.cursor)

## Image only
#images = ie.tag_images('wamdrawthis').data

#res = ie.media('B0ota_DnqoU').data
#print(res)




