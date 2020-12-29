import pyautogui, PIL, webcolors

#define cursorpixel, returns coords of pixel
#cursor is on
def cursorpixel():
    x,y = pyautogui.position()
    pixel = (x,y,x+1,y+1)
    return pixel

#define determinecolor
#returns most present color on cursors pixel
def determinecolor(square, max_colors=256):
    img=PIL.ImageGrab.grab(square)
    color = img.getcolors(max_colors)
    maxocc, mostpres = 0, 0
    for c in color:
        if c[0] > maxocc:
            (maxocc, mostpres) = c
    givencolor = getcolor(mostpres)
    return givencolor

#define getcolor
#returns the closest matching name of color x
#following css3 names
def getcolor(x):
    minclr = {}
    for key, name in webcolors.css3_hex_to_names.items():
        r_r, g_r, b_r = webcolors.hex_to_rgb(key)
        rd = (r_r - x[0]) ** 2
        gd = (g_r - x[1]) ** 2
        bd = (b_r - x[2]) ** 2
        minclr[(rd + gd + bd)] = name
    col = minclr[min(minclr.keys())]
    return col

def main():
    print(determinecolor(cursorpixel()))

while __name__ == "__main__":
    main()
