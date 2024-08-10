from time import sleep
from time import time
from random import choice
import re

# Класс User представляет пользователя на платформе.
class User:   #класс пользователя, содержащий атрибуты: имя пользователя, пароль, возраст
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age
        if age < "18":
            print("Вам нет 18 лет, пожалуйста, покиньте страницу.")
            return


    def eg(self, other):
        return self.nickname == other.nickname  #функция проверки пользователя по имени пользователя

# Класс UrTube представляет платформу и включает методы для взаимодействия с пользователями и видео.
class UrTube:

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, login, password):
        hashpass = hash(password)
        for user in self.users:
            if (user.nickname == login) and (user.password == hashpass):
                self.current_user = user

    def add(self, *args):
        for movie in args:
            if movie not in self.videos:
                self.videos.append(movie)


    def register(self, nickname, password, age):
        if (len(password)<=8):
            return "Пароль должен содержать больше 8 символов"

        if not re.search("[0-9]", password):
            return "Пароль должен содержать цыфры от 0 до 9"
        if not re.search("[A-Z]", password):
            return "Пароль должен содержать латинские буквы от А до Z"

        hashpass = hash(password)
        is_new_user = True
        for user in self.users:
            if (user.nickname == nickname):
                print(f"Пользователь {nickname} уже существует")
                return
            # если никнейм не найден в списке происходит регистрация
        new_user = User(nickname, hashpass, age) # передали в юзер как аргументы
        self.users.append(new_user)
        self.current_user = new_user  # текущий пользователь приравнивается к новому пользователю
        print(f'Пользователь {nickname} зарегестрирован')

#u = UrTube()
#u.register('Andrey','Password123','18')
#print(u.users[0].password)

# Класс Video представляет видео на платформе.
class Video:
    def __init__(self, title: str, duration: int, time_now: int, adult_mode: bool = False):
        self.duration = duration
        self.title = title
        self.time_now = 0
        self.adult_mode = adult_mode

    def __eq__(self, other):
        return self.title.lower() == other.title.lower()

    def __contains__(self, item):
        return item in self.title

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')



