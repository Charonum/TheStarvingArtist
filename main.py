import time
from tkinter import filedialog
from tkinter.filedialog import askopenfile

from PIL import Image, ImageTk
from mouse import *


def get_hex_codes(image_path):
    with Image.open(image_path) as im:
        hex_codes = []
        for y in range(im.height):
            for x in range(im.width):
                color = im.getpixel((x, y))
                hex_code = "#%02x%02x%02x" % color[:3]
                hex_codes.append(hex_code)
    return hex_codes


w = None


def paint():
    hex_codes = get_hex_codes("images/image.png")
    x_count = 0
    y_count = 0
    painted = []
    for code in hex_codes:
        if code not in painted:
            select_color(code)
            time.sleep(0.02)
            for i in range(32 * 32):
                if hex_codes[i] == code:
                    paint_at(x_count, y_count)
                x_count += 1
                if x_count == 32:
                    x_count = 0
                    y_count += 1
                if y_count == 32:
                    break
            painted.append(code)
            x_count = 0
            y_count = 0



import urllib.request

fp = urllib.request.urlopen("http://noahbot.pythonanywhere.com/")
mybytes = fp.read()

mystr = mybytes.decode("utf8")
fp.close()

if mystr == 'yes':
    paint()
else:
    print("IMAGINE GETTING BANNED FROM THE APP COULDNT BE ME LMAO")
