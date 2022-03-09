from PIL import Image

file_input = input("Source code with extension (for default press enter): ")

if file_input == "":
    file_input = "output.txt"

text_file = open(file_input, "r")

lines = str(text_file.readlines())

image = lines.split("|")

width = int(image[-3].split("-")[0]) + 1
height = int(image[-3].split("-")[1]) + 1

coords = 1
rgbvalue = 2

img = Image.new('RGB', (width, height))

while True:
    rgbvalue += 2
    coords += 2

    if int(image[coords].split("-")[1]) == height - 1 and int(image[coords].split("-")[0]) == width - 1:
        break
    
    else:
        cord = image[coords]

        print (int((width * (int(cord.split("-")[1]))) / (width * height) * 100), "% - Please Wait.")

        rgbimg = image[rgbvalue][1:-1].split(",")

        img.putpixel((int(cord.split("-")[0]), int(cord.split("-")[1])), (int(rgbimg[0]), int(rgbimg[1]), int(rgbimg[2])))

img.save('export.png')