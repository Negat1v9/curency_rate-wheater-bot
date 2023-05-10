from config import Config, load_config
import requests
from lexicon.lexicon_wheather import LEXICON_WH
from .utilits import TOKENWH
#получение данных с сервера
def get_wheather(cityname: str) -> dict:
    config: Config = load_config()
    response = requests.get(
        f'{TOKENWH}{cityname}&lang=ru&appid={config.wheather.token}&units=metric')
    wheathet_data: dict = {
        'message': None,
        'error': None,
        'status_code': response.status_code
    }
    if _response_server(response):
        data = response.json()
        wheathet_data['message'] = _get_string_data(data)
    else:
        wheathet_data['error'] = LEXICON_WH['error_msg']
        
    return wheathet_data
#парсинг данных с серавера в словарь
def _get_string_data(response: dict) -> str:
    result: dict = {}
    #temperature in city
    result['temp'] = int(response['main']['temp'])
    #type wheather suny rany ...
    result['description'] = response['weather'][0]['description']
    #name city
    result['city'] = response['name']
    string_msg = f"сейчас в {result['city']} {result['temp']} " \
        f"градусов - {result['description']}"
    return string_msg

def parse_msg(message: str) -> str:
    parse = message.strip().split()
    return str(parse[-1]).capitalize()

#проверка сервера на ответ
def _response_server(request) -> bool:
    return request.status_code == 200