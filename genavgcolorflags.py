import os 
import colorsys
from PIL import Image
import json

images = ["../images2/"+x for x in os.listdir("../images2/")]

flagAvgs = {}

for flagPath in images:
	flagName = flagPath.split("/")[2][:-4]
	img = Image.open(flagPath)
	img=img.convert('RGB')
	colors = img.getcolors(img.size[0] * img.size[1])
	avgrgb = [0,0,0]
	
	for color in colors:
		for a in range(3):
			avgrgb[a] += color[1][a]*color[0]
	avgrgb = tuple([x/sum([a[0] for a in colors]) for x in avgrgb])
	
	
	hsvcolors = [(w,colorsys.rgb_to_hls(*[y/255. for y in x])) for w,x in colors]
	avghsv = [0,0,0]
	for color in hsvcolors:
		for a in range(3):
			avghsv[a] += color[1][a]*color[0]
	
	avghsv = tuple([x/sum([a[0] for a in colors]) for x in avghsv])
	avghue = (avghsv[0],1.0,1.0)
	
	avghsv = colorsys.hsv_to_rgb(*avghsv)

	avghsv = tuple([int(x*255) for x in avghsv])
	
	
	avghue = colorsys.hsv_to_rgb(*avghue)
	avghue = tuple([int(x*255) for x in avghue])
	
	
	
	flagAvgs[flagName] = {}
	flagAvgs[flagName]["rgb"] = tuple(avgrgb)
	flagAvgs[flagName]["hsv"] = avghsv
	flagAvgs[flagName]["hue"] = avghue

with open("flag-avg-color.txt","w")as f:
	f.write(json.dumps(flagAvgs, indent = 4,sort_keys=True))
	 
