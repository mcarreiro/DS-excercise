import requests


class RestClient:

    def get(self, url):
        r = requests.get(str(url))
        if r.status_code == requests.codes.ok:
            return r.json()
        else:
            return r.raise_for_status()
