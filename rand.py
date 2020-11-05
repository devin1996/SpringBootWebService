import requests
from requests.exceptions import HTTPError

try:
    url = "http://localhost:8080/random?bound=15&origin=1&size=100"
    response = requests.get(url)

    json = response.json()
    print("Random number from web service")
    print(json)

    randNums = json['numArray']
    sum = 0
    for num in randNums:
        print(num)
        sum = sum + num
    print("sum of numbers + ", sum)
except HTTPError as http_err:
    print(f'Http error occurred: {http_err}')
#except Exception as err:
