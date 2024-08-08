from time import sleep


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:

    def __init__(self):  #videos and users -> class Video, class User
        self.current_user = None
        self.videos = [] #Video
        self.users = [] #class User

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == hash(password):
                self.current_user = user
                print(f'{nickname} вошел в систему')

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f'Пользователь {nickname} уже существует')
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user
        print(f'{nickname} зарегистрирован и вошел в систему')

    def log_out(self):
        self.current_user = None

    def add(self, *videos): #Video
        for video in videos:
            if not any(v.title == video.title for v in self.videos):
                self.videos.append(video)
                print(f'{video.title} добавлено')
            else:
                print(f'видео {video.title} уже существует')

    def get_videos(self, search_word):
        res = []
        for v in self.videos:
            if search_word.lower() in v.title.lower():
                res.append(v.title)
        return res

    def watch_video(self, title):
        if self.current_user == None:
            print('войдите в систему')
            return

        for v in self.videos:
            if title == v.title:
                if v.adult_mode and self.current_user.age < 18:
                    print('вам нет 18, сначала подрастите')
                    return
                print(f'начинаем просмотр {title}')
                for i in range(v.time_now, v.duration + 1):
                    print(i, end=' ')
                    sleep(1)
                print('конец видео')
                return
        print('видео не найдено')


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