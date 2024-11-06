import geopy
import geopy.distance

def distances(latitude_1, longitude_1, latitude_2, longitude_2):
    coordinates_1 = (latitude_1, longitude_1)
    coordinates_2= (latitude_2, longitude_2)
    distance = round(geopy.distance.distance(coordinates_1,coordinates_2).km,2)
    return distance