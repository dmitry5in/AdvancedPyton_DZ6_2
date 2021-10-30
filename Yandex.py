import requests
from config import token


def create_dir(dir_name):
    response = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                            headers={'Authorization': token}, params={'path': dir_name})
    code = response.status_code
    return code
