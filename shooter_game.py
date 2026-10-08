#Создай собственный Шутер!

from pygame import *
import random


window = display.set_mode((700, 500))#создания игрового окна
display.set_caption('пинг-понг')#устанавливаем название окну
background = transform.scale(image.load('fon.jpg'),(700, 500))


clock = time.Clock()#создаем игровой таймер 
FPS = 60#частотa обновления экрана

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, w, h):
        super().__init__()#Вызов конструктора супер класса для активации функций спрайта
        self.image = transform.scale(image.load(player_image),(w, h))#открываем картинку и скейлим под нужные нам размеры
        self.speed = player_speed
        self.rect = self.image.get_rect()# Получение прямоугольника границ из картинки игрока для управления его позицией
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):#отобразить на экране
        window.blit(self.image,(self.rect.x, self.rect.y))#размещаешь на окне картинку и указываем в каких координатах она должна находиться

class Player(GameSprite):
    def update_left(self):#update нужен для того, чтобы обновлять состояние персонажа (его координаты и действия) на каждом кадре игры.
        keys_pressed = key.get_pressed()#сохраняет состояние всех клавиш 
        if keys_pressed[K_w] and self.rect.y >= 0:
            self.rect.y -= self.speed
        
        if keys_pressed[K_s]and self.rect.y <= 410:
            self.rect.y += self.speed

    def update_right(self):#update нужен для того, чтобы обновлять состояние персонажа (его координаты и действия) на каждом кадре игры.
        keys_pressed = key.get_pressed()#сохраняет состояние всех клавиш 
        if keys_pressed[K_UP] and self.rect.y >= 0:
            self.rect.y -= self.speed
        
        if keys_pressed[K_DOWN]and self.rect.y <= 410:
            self.rect.y += self.speed

player_l = Player('player.png', 20, 410, 6 , 70, 90 )#экземпляр класса
player_r = Player('player.png', 610, 410, 6 , 70, 90 )
meteorit = GameSprite('meteorit.png', 320, 220, 0, 50,70)
# mixer.init()#подключаем и настраиваем звуковую систему
# mixer.music.load('vmprr.mp3')#Загружает файл jungles.ogg в память как фоновую музыку
# mixer.music.play()#Сразу начинает играть загруженную музыку
# fire_ = mixer.Sound('fire.ogg')#Эта строка загружает короткий звук удара в память, чтобы его можно было быстро запустить в любой момент

font.init()
font1 = font.SysFont('Arial', 70)#Font нужен для того, чтобы выводить текст на игровой экран
font2 = font.SysFont('Arial', 30) 


finish = False
game = True#переключатель который удерживает игру в активном состоянии



while game:#отвечает за непрерывную отрисовку графики на экране, пока игра активна
    for e in event.get():#для каждого события в списке событий совершаемых пользователем
        if e.type == QUIT:#проверяет нажал ли игрок на крестик 
            game = False#если да, меняет флаг game на False
        

    if finish != True:
        window.blit(background,(0,0))#рисует фоновое изображение 
        player_l.update_left()
        player_l.reset()#рисует игрока на экране в нужных координатах
        player_r.update_right()
        player_r.reset()
        meteorit.reset()

    clock.tick(FPS)#цикл вайл выполнился 60 раз за секунду
    display.update()#обновляем содержимое окна
