from data import Data
class Admin(Data):
    def __init__(self):
        print("У вас есть уже аккаунт \n1.Да\n2.Нет")
        choice = int(input())
        if choice == 1:
            self._login = input("Введите ваш логин")
            self._password = input("Введите ваш пароль")
            super().__init__()
            self.getUserId(tableName="administration",login = self._login,password= self._password)
            self.choice()
            
        elif choice == 2:
            self._login =  input("Введите логин:")
            self._password = input("Введите пароль:")
            self._email = input("Введите эмайл:")
            self._name = input("Введите имя:")
            

            self.change()
            
    def choice(self):
        print("Вебирете действия которые хотите сделать\n1. Добавить данные пользователей\n 2. Удалить данные пользователей") 
        choice = int (input())
        if choice == 1:
            self.change()
        elif choice == 2:
            self.update()
        elif choice == 3:
            self.deleteData()
    def change(self):
        Data.__init__(self = Data)
        columns = tuple(input("Введите название колонок через пробел: ").split(" "))
        Data.insertData(self,data=(self._login, self._password, self._email, self._name), tableName=input("Введите название таблицы:"), columnName=columns)
    def update(self):
         Data.__init__(self = Data)
         columns = tuple(input("Введите название колонок через пробел: ").split(" "))
    def deleteData(self):
        Data.__init__(self = Data)
        data = tuple(input("Введите название таблицы: "))
        data2 = tuple(input("Введите название ID пользователя: "))
        Data.deleteData(self,data2,data)

ad = Admin()