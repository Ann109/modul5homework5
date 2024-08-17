from time import sleep
import time
import re



# Класс User представляет пользователя на платформе.
class User:   #класс пользователя, содержащий атрибуты: имя пользователя, пароль, возраст
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def print(self, users):  # - метод для вывода информации о пользователях, в виде списка, на экран!
        str1 = []
        for i in users:
            str1.append({i.nickname: [i.password, i.age]})
        print(str1)
# Класс UrTube представляет платформу и включает методы для взаимодействия с пользователями и видео.

# Класс Video представляет видео на платформе.
class Video:
    time_now = 0
    def __init__(self, title, duration, adult_mode):
        self.duration = duration
        self.title = title
        self.adult_mode = False
# Атриубуты: title(заголовок, строка), duration(продолжительность, секунды), time_now(секунда остановки (изначально 0)), adult_mode(ограничение по возрасту, bool (False по умолчанию))


class UrTube:
    current_user = None

    def __init__(self, users, videos):
        self.users = users
        self.videos = videos
    def log_in(self, login, password):  # -  вход в учетную запись

        for i in range(len(self.users)):
            if login not in self.users[i].nickname:
                continue
            else:
                if hash(password) == hash(self.users[i].password):  # - сравниваем пароли по Hash!!!
                    UrTube.current_user = self.users[i]
                    return True  # - полное совпадение по имени и паролю!!!

    def register(self, nickname, password, age):
        if (len(password) <= 8):
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
        new_user = User(nickname, hashpass, age)  # передали в юзер как аргументы
        self.users.append(new_user)
        self.current_user = new_user  # текущий пользователь приравнивается к новому пользователю
        print(f'Пользователь {nickname} зарегестрирован')

    def log_out(self):  # -  выход из текущей учетной записи
        self.current_user = None

    def print_videos(self):  # - вывод информации о видео, в виде списка, на экран!
        str2 = []
        for i in self.videos:
            str2.append({i.title: i.duration})
        print(*str2)

    def users(self):  # - вывод информации о пользователях, в виде списка, на экран!
        str1 = []
        for i in self.users:
            str1.append({i.nickname: [i.password, i.age]})
        print(*str1)
    def add(self, *args): # метод который добавляет видео на платформу
        for movie in args:
            if movie not in self.videos:
                self.videos.append(movie)

    def get_videos(self, find_name): # Метод get_videos, который принимает поисковое слово и возвращает список названий всех видео, содержащих поисковое слово.
        j = 0  # - счетчик совпадений фрагмента в названиях фильмов
        find_videos = []  # - список всех видео, где содержится искомый фрагмент текста
        while True:
            for i in range(len(self.videos)):
                if find_name.upper() in str(self.videos[i].title).upper():
                    find_videos.append(self.videos[i].title)
                    j += 1
            if j == 0:
                print("Фильмы с подобными названиями отсутствуют!!")
            else:
                print(f"список фильмов, где встречается искомый фрагмент: \n{find_videos}")
            return

    def watch_video(self, name_film):  # поиск фильма
        for i in videos:
            if name_film.upper() in i.title.upper():
                if ur.current_user == None:
                    print("Вы не вошли в аккаунт")
                else:
                    if int(ur.current_user.age) < 18:
                        print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    else:
                        print(f"Запускаем просмотр фильма: {i.title}")
                        for i in range(int(i.duration)):
                            time.sleep(1)
                            print(i + 1)
                        print("---!!!Конец видео!!!---")


videos = []  # - список объектов видео
users = []  # - список объектов пользователей
ur = UrTube(users, videos)
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
V3 = Video("Лара Крофт: расхитительница гробниц", 7200)
V4 = Video("Смешные видео с котиками", 120)
V5 = Video("Как строить дом",500)

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




if __name__ == "__main__":
    print('Добро пожаловать на платформу "Свой YouTube"!!! ')
    while True:
        print("\n-------------- ГЛАВНОЕ МЕНЮ -------------------- \n1 - Войти в учетную запись \n2 - Зарегистрироваться\n"
                           "3 - Найти фильмы по фрагменту названия \n4 - выйти из приложения")
        choice = int(input("Введите номер действия: "))
        if choice == 1:  #  -  попытка входа в учетную запить
            print(nickname1 := input("Введите Имя: "), password1 := input("Введите пароль: "))
            if ur.log_in(nickname1, password1) == True:
                print("\n---Текущий пользователь: ___", ur.current_user.nickname,"___!!!---")
                while ur.current_user != None:
                    print("\n1 - добавить новый фильм в список \n2 "
                                       "- найти фильм по названию (для просмотра) \n3 - Найти фильмы по фрагменту "
                                        "названия\n4 - Выйти из текущего аккаунта\n5 - выйти из приложения\n")
                    choice2 = int(input("Выбери, что нужно сделать: "))
                    if choice2 == 1:
                        ur.add(V3, V4, V5)
                        print(f"Текущий список видео: ")
                        ur.print_videos()
                    elif choice2 == 2:
                        ur.watch_video(input("введите точное название фильма для просмотра: "))
                    elif choice2 == 3:
                        ur.get_videos(input("Напишите фрагмент названия для поиска подходящих фильмов в нашем списке:"))
                    elif choice2 == 4:
                        ur.log_out()
                    else:
                        exit()
            else:
                print("Такой пользователь не найден!!")
        elif choice == 2:  # - регистрация нового пользователя!
            user = User(input("Введите Имя: "), input("Введите пароль: "), input("введите ваш возраст: "))
            ur.register(user.nickname, user.password, user.age)
            print("текущий список пользователей:")
            ur.users()
            print("\n---Текущий пользователь: !!!___", ur.current_user.nickname,"___!!!---")
            while ur.current_user != None:
                print("1 - добавить новый фильм в список \n2 "
                                       "- найти фильм по названию (для просмотра) \n3 - Найти фильмы по фрагменту "
                                        "названия\n4 - Выйти из текущего аккаунта\n5 - выйти из приложения")
                choice2 = int(input("Выбери, что нужно сделать: "))
                if choice2 == 1:
                    ur.add(V3, V4, V5)
                    print("Текущий список видео: ")
                    ur.print_videos()
                elif choice2 == 2:
                    ur.watch_video(name_film=input("введите точное название фильма для просмотра: "))
                elif choice2 == 3:
                    ur.get_videos(input("Напишите фрагмент названия для поиска подходящих фильмов в нашем списке: "))
                elif choice2 == 4:
                    ur.log_out()
                else:
                    exit()
        elif choice == 3:
            ur.get_videos(input("Напишите фрагмент названия для поиска подходящих фильмов в нашем списке: "))
        elif choice == 4:
            print("До новых встреч!!!")
            exit()
