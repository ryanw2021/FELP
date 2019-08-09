import urllib.parse
import urllib.request
import json

yelpURL = "https://api.yelp.com/v3/businesses/gR9DTbKCvezQlqvD7_FzPw"
headers = {'User-Agent' : 'Mozilla/5.0',
            'Authorization' : 'Bearer VObfC-uB4FN4ChiP32DlyX2Q035NOH4z3MUKGNpmG49RtQaVmTAeTx3hhcNgOqfPLoPB97DvVdpsukJ0l8jInGI-KoS7nG40Vb0LW_L7ZOb-LcTb0oxGz3ZyVTRMXXYx'}
req = urllib.request.Request(yelpURL, None, headers)
response = urllib.request.urlopen(req)
#print(response.read())

data = json.loads(response.read())
rating = data["rating"]
latitude = data["coordinates"]["latitude"]
longitude = data["coordinates"]["longitude"]
print("Rating: "+str(rating)+" Latitude: "+str(latitude)+" Longitude: "+str(longitude))