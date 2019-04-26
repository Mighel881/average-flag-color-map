from bs4 import BeautifulSoup
import os 
import colorsys
from PIL import Image
import json

#Getting a list of all the flag's paths
images = ["flags/"+x for x in os.listdir("flags/")]

#initializing dictionary
flagAvgs = {}

#iterating through each image
for flagPath in images:

    #getting the state name
    flagName = flagPath.split("/")[1][:-4]

    #loading the image
    img = Image.open(flagPath).convert('RGB')

    #getting the colors
    colors = img.getcolors(img.size[0] * img.size[1])

    #Averaging the rgb values
    avgrgb = [0,0,0]
    
    for color in colors:
        for a in range(3):
            avgrgb[a] += color[1][a]*color[0]
            
    avgrgb = tuple([x/sum([a[0] for a in colors]) for x in avgrgb])
    
    #creating new list, of rgb converted to hsv
    hsvcolors = [(w,colorsys.rgb_to_hls(*[y/255. for y in x])) for w,x in colors]

    #Averaging the hsv values
    avghsv = [0,0,0]
    
    for color in hsvcolors:
        for a in range(3):
            avghsv[a] += color[1][a]*color[0]
    
    avghsv = [x/sum([a[0] for a in colors]) for x in avghsv]

    #creating new value that has the same average hue, but with full value and saturation
    avghue = (avghsv[0],1.0,1.0)

    #converting hsv back to rgb
    avghsv = colorsys.hsv_to_rgb(*avghsv)
    avghsv = tuple([int(x*255) for x in avghsv])
    
    #converting hue back to rgb
    avghue = colorsys.hsv_to_rgb(*avghue)
    avghue = tuple([int(x*255) for x in avghue])
    
    #assigning average colors to dict
    flagAvgs[flagName] = {}
    flagAvgs[flagName]["rgb"] = tuple(avgrgb)
    flagAvgs[flagName]["hsv"] = avghsv
    flagAvgs[flagName]["hue"] = avghue
    flagAvgs[flagName]["common"] = sorted(colors,reverse=True)[0][1]

#two separate scripts were combined, this makes it so I don't have to change the variable names
colors = flagAvgs

#loading world svg
with open("svgs/usa-states.svg","r") as f:
    worldMap = BeautifulSoup(f.read(),"html.parser")

worldMap.svg["style"] = "background-color: #ececec;"
worldMap.find("g",id="DC").decompose()

#creating a list of the colortypes, rgb, hsv, hue, etc.
colorTypes = list(colors["Alaska"])

#iterating through the colortypes
for colorType in colorTypes:

    #each state has it's own path object
    for path in worldMap.find_all("path"):

        #getting the state id
        state = path.text.strip()

       
        

        #if the id matches a flag
        if colors.get(state):

            print state

            #converting the rgb value to hex - i know that I could probably just do rgb() but why not make it hex??
            hexStr = "#"
            for part in colors.get(state)[colorType]:
                hexStr+= str(hex(part))[2:].zfill(2)

            #Assigning the new style to the path
            path["style"] = "fill:{};fill-rule:evenodd".format(hexStr)

    #saving the svg file
    with open("states-{}.svg".format(colorType),"w") as f:
        f.write(str(worldMap))
