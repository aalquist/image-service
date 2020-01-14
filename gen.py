from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

im = Image.new('RGBA', (500,500) )

draw = ImageDraw.Draw(im)

font = ImageFont.truetype(font="fonts/Roboto-Bold.ttf", size=20)

now = datetime.now()
date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

printList = ["Hello", "World", "Ted", date_time]

increment = 25
pos = 20
for txt in printList:
    pos = pos + increment
    draw.text((20, pos), txt, font=font)

#draw.text((20, 20), "Hello", font=font)
#draw.text((20, 45), "World", font=font)
#draw.text((20, 70), date_time, font=font)



im.save("hello-world-timestamp.png")