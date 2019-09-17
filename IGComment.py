#import pyautogui as pag
#import webbrowser as wb
#from PIL import Image
#import urllib2 as urllib
#import io
##f.open("comments.txt", "r")

##wb.

#fd = urllib.urlopen("https://scontent-atl3-1.cdninstagram.com/vp/1628d7b714ebeb4fe8bcf8018cd229ca/5E0FA06B/t51.2885-15/e35/p1080x1080/65631387_338819513717481_4708872033228826505_n.jpg?_nc_ht=scontent-atl3-1.cdninstagram.com")
#image_file = io.BytesIO(fd.read())
#im = Image.open(image_file)

from PIL import Image
from StringIO import StringIO
import requests

r = requests.get("https://scontent-atl3-1.cdninstagram.com/vp/1628d7b714ebeb4fe8bcf8018cd229ca/5E0FA06B/t51.2885-15/e35/p1080x1080/65631387_338819513717481_4708872033228826505_n.jpg?_nc_ht=scontent-atl3-1.cdninstagram.com")
im = Image.open(StringIO(r.content))
im.size