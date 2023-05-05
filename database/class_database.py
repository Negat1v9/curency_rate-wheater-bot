import sqlite3


class DataBase():
    def __init__(self, name):
        self.db_name = name
        self.conn = sqlite3.connect(name)#-->connect with database
        self.cur = self.conn.cursor()#-->creat cursor
    
    def insert_data(self, table_name: str, columns: tuple, data: tuple) -> None:
         #creating place for column
        column = ", ".join(columns)#->str
        #creating place for data in Isert
        place_data = ", ".join(["?" for _ in range(len(data))])#-->str
        #creating req text
        query = f"""INSERT INTO {table_name} ({column}) VALUES ({place_data})"""
        self.cur.execute(query, data)
        self.conn.commit()
        
    def select_data(self, table_name, colums= tuple | None, conditions = tuple | None):
        colums_str = "*" if not colums else ", ".join(colums)
        query = f"SELECT {colums_str} FROM {table_name}"
        if conditions:
            query += f" WHERE {conditions}"
        self.cur.execute(query)
        rows = self.cur.fetchall()
        return rows
    
    def close_conn(self):
        self.conn.commit()
        self.conn.close()