from admin import Admin
from girl import Girl
from security import Security
from user import User

print("Приветствуем вас на нашем сайте\nВведите, под каким пользователем вы хотите войти:")
print("1. Админ\n2. Девушка\n3. Охранник\n4. Клиент")
choice = int(input("Введите цифру: "))

if choice == 1:
    admin = Admin()
elif choice == 2:
    girl = Girl()
elif choice == 3:
    security = Security()
elif choice == 4:
    user = User()
else:
    print("Неверный выбор")
