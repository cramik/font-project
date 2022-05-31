from PIL import *
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import os

currentfolder=os.listdir('.')
message="Cramik"
fontinc=1
total=0

for file in currentfolder:
    if file.endswith(".ttf") or file.endswith(".otf"):
        total=total+1

totalHeight=12*total
img = Image.new('RGB',(60,totalHeight),color='white')

for file in currentfolder:
    if file.endswith(".ttf") or file.endswith(".otf"):
        try:
            font = ImageFont.truetype(file,size=11)
            
            imgDraw = ImageDraw.Draw(img)
            textWidth, textHeight = imgDraw.textsize(message, font=font)
            xText = (60 - textWidth) / 2
            yText = 11*fontinc
            imgDraw.text((xText, yText), message, font=font, fill=(0, 0, 0))
        except:
            print(f"Failed on {file}")
        fontinc=fontinc+1

img.save('output1.png')