from PIL import Image, ImageDraw, ImageFont

def writeOnImage(text, position, fontPath, fontSize, fontColor):
    font = ImageFont.truetype(fontPath, fontSize)
    draw.text(position, text, font=font, fill=fontColor)
    


# generate 22 char unique number
def generateUniqueNumber(count):
    import random
    import string
    return ''.join(random.choices(string.digits, k=count))




date_time = [
    {
        "time": "09:29 AM",
        "date": "14 Apr 2024"
    },
     {
        "time": "10:13 AM",
        "date": "16 Apr 2024"
    },
     {
        "time": "10:21 AM",
        "date": "18 Apr 2024"
    },
     {
        "time": "08:56 AM",
        "date": "20 Apr 2024"
     }, 
       {
             "time": "10:32 AM",
        "date": "23 Apr 2024"

       },
        {
             "time": "09:49 AM",
        "date": "25 Apr 2024"
        },
    {
         "time": "10:42 AM",
        "date": "27 Apr 2024"
    }
]




for i in date_time:
    image = Image.open('blank_bill.jpg')
    draw = ImageDraw.Draw(image)
    writeOnImage(i["time"]+ ' on ' +i["date"], (228, 125), 'Roboto-Regular.ttf', 38, '#ffffff')
    writeOnImage('T'+str(generateUniqueNumber(22)), (77, 355), 'Roboto-Regular.ttf', 42, '#ffffff')
    writeOnImage(str(generateUniqueNumber(12)), (357, 1094), 'Roboto-Regular.ttf', 42, '#ffffff')
    image.save('out/'+i["date"]+'.png')
    