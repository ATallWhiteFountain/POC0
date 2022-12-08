from dataclasses import dataclass
from requests import get


@dataclass
class ApiClient():

    response: str = None

    def get(self, resource_uri: str) -> int:
        self.response = get(resource_uri)
        return self.response.status_code


    def getJsonDictData(self) -> dict:
        if ('json' in self.response.headers.get('Content-Type') or
         'json' in self.response.headers.get('content-type')):
            return self.response.json()[0]
        else:
            return None
