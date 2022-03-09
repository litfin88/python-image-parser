from PIL import Image

im = Image.open(input("File Name (with extension): "))
width, height = im.size
px = im.load()

satir = 1
cell = 0

i = 0

f=open("output.txt", 'w')
f.write("START|")

while True:
    cell += 1
    if cell == width:
        cell = 0
        satir += 1
    else:
        coordinate = x, y = cell, satir
        f.write(str(cell) + '-' + str(satir) + '|' + str(im.getpixel(coordinate)) + '|')
        print (int((width * (satir)) / (width * height) * 100), "% - Please Wait.")
        i+=1

    if satir == height and cell == width - 1:
        f.write(str(cell) + '-' + str(satir) + '|' + str(im.getpixel(coordinate)) + '|')
        f.write("FINISH")
        break
