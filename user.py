from data import Data
class User(Data):
    def __init__(self):
        print("У вас есть уже аккаунт \n1.Да\n2.Нет")
        choice = int(input())
        if choice == 1:
            self._login = input("Введите ваш логин")
            self._password = input("Введите ваш пароль")
            super().__init__()
            self.getUserId(tableName="administration",login = self._login,password= self._password)
            self.choiceGirl()
        elif choice == 2:
            self._login =  input("Введите логин:")
            self._password = input("Введите пароль:")
            self._email = input("Введите эмайл:")
        
            self.__proverkapassword()
            self.choiceGirl()
    def __proverkapassword(self):
        if len(self._password) < 4:
            raise ValueError('слабый пароль')
        else:
            self.register()
    
    def register(self):
        Data.__init__(self = Data)
        columns = tuple(input("Введите название колонок через пробел: ").split(" "))
        Data.insertData(self,data=(self._login, self._password, self._email,), tableName="girls", columnName=columns)
            
    def choiceGirl(self):
        Data.__init__(self = Data)
        data = "girls"
        data2 = tuple(input("Введите название ID девушки, которую вы хотите заказать: "))
        Data.deleteData(self,data,data2)

x = User()