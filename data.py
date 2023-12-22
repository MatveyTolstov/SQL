import sqlite3
class Data:
    def __init__(self):
        self.conn = sqlite3.connect('bordel.db')
        self.cursor = self.conn.cursor()
        
    def insertData(self, data, tableName, columnName):
        querry = f"INSERT INTO {tableName} {columnName} VALUES {data}"
        print(querry)
        self.cursor.execute(querry)
        print("Данные успешно добавленные")
        self.conn.commit()
        
    def upadateData(self, data, tableName, columName, id):
        querry = f"UPDATE {tableName} SET {columName} = {data} WHERE id = {id}"
        self.cursor.execute(querry)
        print("Данные успешно обновленны")
        self.conn.commit()
        
    def deleteData(self,id,tableName):
        querry = f"DELETE FROM {tableName} WHERE id = {id}"
        self.cursor.execute(querry)
        print("Данные успешно удалены")
        self.conn.commit()
        
    def getData(self, tableName):
        return self.cursor.execute(f"SELECT * FROM {tableName}").fetchall()
    
    def getUserId(self, tableName, login, password):
        querry = f"SELECT * FROM {tableName} WHERE login = ? AND password = ?"
        user = self.cursor.execute(querry, [login, password]).fetchone()
        return user
    