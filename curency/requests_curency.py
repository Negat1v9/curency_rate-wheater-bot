import requests
import json
from bs4 import BeautifulSoup
from datetime import datetime
from config import Config, load_config
from database.class_database import DataBase

def _load_curency() -> str:
    config: Config = load_config()
    url = config.curency.url
    r = requests.get(url=url)
    data = r.text
    return data

def get_curency() -> dict:
    db = DataBase('valut.db')
    now = datetime.now()
    date_string = now.strftime("%Y-%m-%d")#->time now
    # date_string = '2023-05-09'
    data: list = db.select_data('valut', ('curency',),
                                'data_column', date_string)
    curency: dict = {}
    if not data:
        text = _load_curency()
        curency: dict = _parse_data(text)#->geting dict curency
        _add_curency(curency, db, date_string)
    else:
        curency = json.loads(data[0][0])#->if curuncy already there
    return curency

def _add_curency(curency: dict, db: DataBase,
                       date_string: datetime) -> None:
    curency_text = json.dumps(curency)#-> geting text to db
    db.insert_data('valut', ('data_column', 'curency'),
                       (date_string, curency_text))#->add new curency
    db.close_conn()
        
def _parse_data(text: str) -> dict:
    soup = BeautifulSoup(text, 'html.parser')
    src = soup.find('div',id="w0")
    
    data: BeautifulSoup = src
    src: BeautifulSoup = data.find_all('td')
    curency_dict: dict = {}
    for i in range(0, len(src), 4):
        text = src[i].text
        if text:
            curency_dict[text] = [src[i+1].text, src[i+2].text]
    return curency_dict
    