import sys
from io import BytesIO
import requests
from PIL import Image
from scale import get_coord


def get_image(ll, spn):
    if not ll:
        return "Адрес не найден"
    map_params = {
        "ll": ll,
        "spn": spn,
        "l": "map",
        "pt": ll
    }
    map_api_server = "http://static-maps.yandex.ru/1.x/"
    response = requests.get(map_api_server, params=map_params)

    Image.open(BytesIO(
        response.content)).show()
    return "Адрес найден"


def main():
    address = sys.argv[1:]
    print(get_image(*get_coord(address)))


if __name__ == "__main__":
    main()