import json
import turtle
import urllib.request
import time
import webbrowser
import geocoder

url = "http://api.open-notify.org/astros.json"
response = urllib.request.urlopen(url)
result = json.loads(response.read())
file = open("iss.txt", "w")
file.write("There are currently " + str(result["number"]) + " astronauts on the ISS: \n\n")
people = result["people"]
for person in people:
    file.write(person['name'] + " - on board\n")
# print long and lat
g = geocoder.ip('me')
file.write('\nYour current lat / long is: ' + str(g.latlng))
file.close()
webbrowser.open("iss.txt")

# setup world  map in turtle module
screen = turtle.Screen()
screen.setup(1280, 720)
screen.setworldcoordinates(-180, -90, 180, 90)

# load world map image
screen.bgpic("Global Map.gif")
screen.register_shape("iss.gif")
iss = turtle.Turtle()
iss.shape("iss.gif")
iss.penup()

while True:
    # Load current status of iss
    url = "http://api.open-notify.org/iss-now.json"
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())

    # extract iss location
    location = result["iss_position"]
    lat = location["latitude"]
    lon = location["longitude"]

    # output to terminal
    lat = float(lat)
    lon = float(lon)
    print("\nLatitude: " + str(lat))
    print("\nLongitude: " + str(lon))

    # update iss location on map
    iss.goto(lon, lat)

    # refresh each 5 seconds
    time.sleep(5)
    

input('stop')