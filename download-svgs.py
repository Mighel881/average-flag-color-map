import urllib
import os

#creating dir
if not os.path.isdir("svgs/"):
    os.mkdir("svgs/")

#US Counties - not needed
#urllib.urlretrieve("https://upload.wikimedia.org/wikipedia/commons/5/5f/USA_Counties_with_FIPS_and_names.svg","svgs/usa-counties.svg")

#US States
urllib.urlretrieve("https://upload.wikimedia.org/wikipedia/commons/1/1a/Blank_US_Map_%28states_only%29.svg","svgs/usa-states.svg")

#World Map - might fail because of cloudflare
urllib.urlretrieve("https://simplemaps.com/static/demos/resources/svg-library/svgs/world.svg","svgs/world-map.svg")
