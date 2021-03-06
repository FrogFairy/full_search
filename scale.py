import requests


def get_coord(address):
    toponym = geocode(address)
    if not toponym:
        return (None, None)
    toponym_coodrinates = toponym["Point"]["pos"]
    toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")
    ll = ",".join([toponym_longitude, toponym_lattitude])
    left, bottom = toponym["boundedBy"]["Envelope"]["lowerCorner"].split(" ")
    right, top = toponym["boundedBy"]["Envelope"]["upperCorner"].split(" ")
    dx = abs(float(left) - float(right)) / 2.0
    dy = abs(float(top) - float(bottom)) / 2.0
    spn = f"{dx},{dy}"
    return ll, spn


def geocode(address):
    toponym_to_find = " ".join(address)
    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": toponym_to_find,
        "format": "json"}
    response = requests.get(geocoder_api_server, params=geocoder_params)
    if not response:
        return None
    json_response = response.json()
    return json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]