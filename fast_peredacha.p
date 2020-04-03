from PIL import Image, ImageDraw, ImageGrab
import pygame
import time
img = ImageGrab.grab()
img.save("screen.jpg", "JPEG")
image = Image.open('screen.jpg')
draw = ImageDraw.Draw(img)  # Создаем инструмент для рисования
width = img.size[0]  # Определяем ширину
height = img.size[1]  # Определяем высоту
pix = img.load()  # Выгружаем значения пикселей
print(width)
print(height)
x=0
y=0

str='ж'
def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'
ttb=text_to_bits(str)
str1=list(map(int,ttb))

def bright_white(x, y,dr):
    r = min(pix[x, y][0] + 100, 255)  # узнаём значение красного цвета пикселя
    g = min(pix[x, y][1] + 100, 255)  # зелёного
    b = min(pix[x, y][2] + 100, 255)  # синего
    dr.point((x, y), (r, g, b))

def bright_black(x, y,dr):
    r = max(pix[x, y][0] - 100, 0)  # узнаём значение красного цвета пикселя
    g = max(pix[x, y][1] - 100, 0)  # зелёного
    b = max(pix[x, y][2] - 100, 0)  # синего
    dr.point((x, y), (r, g, b))

def four_polos():
    img_copy = img.copy()
    t1_draw = ImageDraw.Draw(img_copy)
    for y in range(height):
        for x in range(width):
            if x % 2 == 0 and (0 <= y < 200 or 400 <= y < 600):
                bright_white(x, y,t1_draw)
            elif x % 2 == 1 and (200 <= y < 400 or 600 <= y < height):
                bright_white(x, y,t1_draw)
            else:
                bright_black(x, y,t1_draw)
    img_copy.save("nechet_0.jpg", "JPEG")  # сохранить изображение
    
def eight_polos():
    img_copy = img.copy()
    t2_draw = ImageDraw.Draw(img_copy)
    for y in range(height):
        for x in range(width):
            if x % 2 == 0 and (0 <= y < 100 or 200 <= y < 300 or 400 <= y < 500 or 600 <= y < 700):
                bright_white(x, y,t2_draw)
            elif x % 2 == 1 and (100 <= y < 200 or 300 <= y < 400 or 500 <= y < 600 or 700 <= y < height):
                bright_white(x, y,t2_draw)
            else:
                bright_black(x, y,t2_draw)
    img_copy.save("nechet_1.jpg", "JPEG")  # сохранить изображение
    
def ten_polos():
    img_copy = img.copy()
    t3_draw = ImageDraw.Draw(img_copy)
    for y in range(height):
        for x in range(width):
            if x % 2 == 0 and (0 <= y < 80 or 160 <= y<240 or 320 <= y < 400 or 480 <= y < 560 or 640 <= y < 720):
                bright_white(x, y,t3_draw)
            elif x % 2 == 1 and (80 <= y < 160 or 240 <= y < 320 or 400 <= y < 480 or 560 <= y < 640 or 720 <= y < height):
                bright_white(x, y,t3_draw)
            else:
                bright_black(x, y,t3_draw)
    img_copy.save("chet_0.jpg", "JPEG")  # сохранить изображение
    
def sixteen_polos():
    img_copy = img.copy()
    t4_draw = ImageDraw.Draw(img_copy)
    for y in range(height):
        for x in range(width):
            if x % 2 == 0 and (0 <= y < 50 or 100 <= y < 150 or 200 <= y < 250 or 300 <= y < 350 or 400 <= y < 450 or 500 <= y < 550 or 600 <= y < 650 or 700 <= y < 750):
                bright_white(x, y,t4_draw)
            elif x % 2 == 1 and (50 <= y < 100 or 150 <= y < 200 or 250 <= y < 300 or 350 <= y < 400 or 450 <= y < 500 or 550 <= y < 600 or 650 <= y < 700 or 750 <= y < height):
                bright_white(x, y,t4_draw)
            else:
                bright_black(x, y,t4_draw)
    img_copy.save("chet_1.jpg", "JPEG")  # сохранить изображение

four_polos()
eight_polos()
ten_polos()
sixteen_polos()

clock = pygame.time.Clock()
def screen():
    _JPEG_IMAGE1 = 'screen.jpg'
    time.sleep(1)
    pygame.display.init()
    img = pygame.image.load(_JPEG_IMAGE1)
    screen = pygame.display.set_mode(img.get_size(), pygame.FULLSCREEN)
    screen.blit(img, (0, 0))
    pygame.display.flip()

def polos_nechet_0():
    im1 = Image.open('screen.jpg')
    im2 = Image.open('nechet_0.jpg')
    im1.paste(im2, (0, 0))  # Последний параметр — альфаканал, используемый для наложения
    im1.save('result2.jpg')
    _JPEG_IMAGE = 'result2.jpg'
    time.sleep(1)
    pygame.display.init()
    img = pygame.image.load(_JPEG_IMAGE)
    screen = pygame.display.set_mode(img.get_size(), pygame.FULLSCREEN)
    screen.blit(img, (0, 0))
    pygame.display.flip()

def polos_nechet_1():
    im1 = Image.open('screen.jpg')
    im3 = Image.open('nechet_1.jpg')
    im1.paste(im3, (0, 0))  # Последний параметр — альфаканал, используемый для наложения
    im1.save('result3.jpg')
    _JPEG_IMAGE = 'result3.jpg'
    time.sleep(1)
    pygame.display.init()
    img = pygame.image.load(_JPEG_IMAGE)
    screen = pygame.display.set_mode(img.get_size(), pygame.FULLSCREEN)
    screen.blit(img, (0, 0))
    pygame.display.flip()

def polos_chet_0():
    im1 = Image.open('screen.jpg')
    im4 = Image.open('chet_0.jpg')
    im1.paste(im4, (0, 0))  # Последний параметр — альфаканал, используемый для наложения
    im1.save('result4.jpg')
    _JPEG_IMAGE = 'result4.jpg'
    time.sleep(1)
    pygame.display.init()
    img = pygame.image.load(_JPEG_IMAGE)
    screen = pygame.display.set_mode(img.get_size(), pygame.FULLSCREEN)
    screen.blit(img, (0, 0))
    pygame.display.flip()

def polos_chet_1():
    im1 = Image.open('screen.jpg')
    im5 = Image.open('chet_1.jpg')
    im1.paste(im5, (0, 0))  # Последний параметр — альфаканал, используемый для наложения
    im1.save('result5.jpg')
    _JPEG_IMAGE = 'result5.jpg'
    time.sleep(1)
    pygame.display.init()
    img = pygame.image.load(_JPEG_IMAGE)
    screen = pygame.display.set_mode(img.get_size(), pygame.FULLSCREEN)
    screen.blit(img, (0, 0))
    pygame.display.flip()

for i1,i in enumerate(str1):
        if i==0 and i1%2==0:
            screen()
            polos_chet_0()
        elif i==1 and i1%2==0:
            screen()
            polos_chet_1()
        elif i==0 and i%2==1:
            screen()
            polos_nechet_0()
        elif i==1 and i%2==1:
            screen()
            polos_nechet_1()

isRunning = True
while isRunning:
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRunning = False
pygame.quit()
