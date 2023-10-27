from pprint import pprint
import json
import requests

if __name__ == '__main__':
    import requests

    r = requests.get('https://baconipsum.com/api/?type=meat-and-filler')

    r = json.loads(r.content)

    print(r[0])
