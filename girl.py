from data import Data
class girl(Data):
    def __init__(self):
        try:
            self.name = input("Введите ваше имя:")
            self.age = int(input("Введите ваш возраст"))
            self.size_boobs = int(input("Введите размер ваших boobs"))
          
            self.register()
        except(ValueError):
            print("Ошибка")
            
    def register(self):
        Data.__init__(self = Data)
        columns = tuple(input("Введите название колонок через пробел: ").split(" "))
        Data.insertData(self,data=(self.name, self.age, self.size_boobs,), tableName="girls", columnName=columns)
        
girl = girl()
    
        