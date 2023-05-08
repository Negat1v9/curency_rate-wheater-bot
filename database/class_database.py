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
        
    def select_data(self, table_name: str, colums= tuple | None,
                    name_search_column = str, conditions = int | str | None):
        colums_str = "*" if not colums else ", ".join(colums)
        query = f"SELECT {colums_str} FROM {table_name}"
        if conditions:
            query += f" WHERE {name_search_column} = ?"
            #if user now where he search
            self.cur.execute(query, (conditions,))
        else:
            #if user want select all
            self.cur.execute(query)
        rows = self.cur.fetchall()
        return rows
    
    def update_info(self, table_name: str, search_column: str,
                    what_up: tuple, primary_key, data: tuple):
        
        for_up = " ".join([upd+"=?" for upd in what_up])#->updating column
        search_column = search_column+"=?"
        
        updating_inf = data + (primary_key,)#->tuple in sql query
        query = f"""UPDATE {table_name} SET {for_up} WHERE {search_column}"""
        
        self.cur.execute(query, updating_inf)
        self.conn.commit()
        
    
    def close_conn(self):
        self.conn.commit()
        self.conn.close()