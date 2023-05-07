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
        data = db.select_data('users', None, self.userid)#->checking user in db
        if not data:
            db.insert_data('users', ('userid',), (self.userid,))#->if not -> add
            db.close_conn()
            
    def _update_user_list(self, data: str, db: DataBase) -> None:
        db.update_info('users', 'userid', ('uservalut',), self.userid, (data,))
        db.close_conn()
            
    def add_user_valut(self, valut: str) -> bool:
        db: DataBase = DataBase(self.userdb)
        data_text = db.select_data('users', ('uservalut',), self.userid)
        data_list: list = self._create_list(data_text)
        if valut not in data_list:
            data_list.append(valut)
            data_text = self._create_text(data_list)
            self._update_user_list(data_text, db)
            return True
        else:
            return False
            
    
    def _create_list(text: str | None) -> list:
        if text[0]:
            for txt in text:
                data = json.loads(txt)
                return data
        else:
            return []
                
            
    def _create_text(valut: list) -> str:
        text_list = json.dumps(valut)
        return text_list