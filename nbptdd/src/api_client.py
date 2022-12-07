from dataclasses import dataclass
from typing import Optional
from requests import get


@dataclass
class ApiClient():

    response: str = None


    def get(self, resource_uri: str) -> int:
        self.response = get(resource_uri)
        return self.response.status_code


    def getDictData(self) -> Optional[dict]:
        if self.response:
            return self.response.json()[0]
        else:
            return self.response
