from database.class_database import DataBase
from config import Config, load_config
import json
class User():
    def __init__(self, userid: int):
        self.userid = userid
        _user_config: Config = load_config()
        self.userdb = _user_config.database.database
        
    def init_user(self) -> None:
        db: DataBase = DataBase(self.userdb)
        data = db.select_data('users', None, 'userid', self.userid)#->checking user in db
        if not data:
            db.insert_data('users', ('userid',), (self.userid,))#->if not -> add
            db.close_conn()
            
    def _update_user_list(self, data: str, db: DataBase) -> None:
        db.update_info('users', 'userid', ('users_wh',), self.userid, (data,))
        db.close_conn()
        
    def del_user_city(self, data: list[str] | list[None]) -> None:
        db: DataBase = DataBase(self.userdb)
        data_text = self._create_text(data)
        self._update_user_list(data_text, db=db)
            
    def add_user_city(self, city: str) -> None:
        db: DataBase = DataBase(self.userdb)
        data_text = db.select_data('users', ('users_wh',),
                                   'userid', self.userid)
        data_list: list = self._create_list(data_text[0])
        #added new city in list
        data_list.append(city)
        #creating json list to select in db
        data_text = self._create_text(data_list)
        #updating new city in db
        self._update_user_list(data_text, db)
        
    def get_user_city(self) -> list:
        db: DataBase = DataBase(self.userdb)
        data_text: list = db.select_data('users', ('users_wh',),
                                   'userid', self.userid)
        data_list: list = self._create_list(data_text[0])
        
        return data_list
            
    
    def _create_list(self, text: tuple) -> list:
        if text[0]:
            text_data = text[0]
            data = json.loads(text_data)
            return data
        else:
            return []
                
            
    def _create_text(self, city: list) -> str:
        text_list = json.dumps(city)
        return text_list