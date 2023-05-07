from database.class_database import DataBase
from config import Config, load_config

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