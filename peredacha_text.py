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
# print(ttb)
# print(text_from_bits(ttb))
str1=list(map(int,ttb))

def bright_white ():
    r = pix[x, y][0] + 100  # узнаём значение красного цвета пикселя
    g = pix[x, y][1] + 100  # зелёного
    b = pix[x, y][2] + 100  # синего
    if (r < 0):
        r = 0
    if (g < 0):
        g = 0
    if (b < 0):
        b = 0
    if (r > 255):
        r = 255
    if (g > 255):
        g = 255
    if (b > 255):
        b = 255
    draw.point((x, y), (r, g, b))
def bright_black():
    r = pix[x, y][0] - 100  # узнаём значение красного цвета пикселя
    g = pix[x, y][1] - 100  # зелёного
    b = pix[x, y][2] - 100  # синего
        # r1 = round(r * 0.299)
        # g1 = round(g * 0.587)
        # b1 =round(b * 0.114)
    if (r < 0):
        r = 0
    if (g < 0):
        g = 0
    if (b < 0):
        b = 0
    if (r > 255):
        r = 255
    if (g > 255):
        g = 255
    if (b > 255):
        b = 255
    draw.point((x, y), (r, g, b))


for i1 in range(2):
    for i in str1:
        if i1%2==1 and i==0:
            # крупные полосы 4 штуки
            for y in range(height):
                for x in range(width):
                    bright_black()

            for y in range(0, 200, 1):
                for x in range(width):
                    if x % 2 == 0:
                        bright_white()

            for y in range(200, 400, 1):
                for x in range(width):
                    if x % 2 == 1:
                        bright_white()

            for y in range(400, 600, 1):
                for x in range(width):
                    if x % 2 == 0:
                        bright_white()

            for y in range(600, height, 1):
                for x in range(width):
                    if x % 2 == 1:
                        bright_white()
            img.save("nechet_0.jpg", "JPEG")  # сохранить изображение
        elif i1%2==1 and i==1:

            # крупные полосы 8 штук
            for y in range(height):
                for x in range(width):
                    bright_black()

            for y in range(0, 100, 1):
                for x in range(width):
                    if x % 2 == 0:
                        bright_white()

            for y in range(100, 200, 1):
                for x in range(width):
                    if x % 2 == 1:
                        bright_white()

            for y in range(200, 300, 1):
                for x in range(width):
                    if x % 2 == 0:
                        bright_white()

            for y in range(300, 400, 1):
                for x in range(width):
                    if x % 2 == 1:
                        bright_white()

            for y in range(400, 500, 1):
                for x in range(width):
                    if x % 2 == 0:
                        bright_white()

            for y in range(500, 600, 1):
                for x in range(width):
                    if x % 2 == 1:
                        bright_white()

            for y in range(600, 700, 1):
                for x in range(width):
                    if x % 2 == 0:
                        bright_white()

            for y in range(700, height, 1):
                for x in range(width):
                    if x % 2 == 1:
                        bright_white()

            img.save("nechet_1.jpg", "JPEG")  # сохранить изображение
        elif i1%2==0 and i==0:

            # крупные полосы 10 штук
            for y in range(height):
                for x in range(width):
                    bright_black()

            for y in range(0, 80, 1):
                for x in range(width):
                    if x % 2 == 0:
                        bright_white()

            for y in range(80, 160, 1):
                for x in range(width):
                    if x % 2 == 1:
                        bright_white()

            for y in range(160, 240, 1):
                for x in range(width):
                    if x % 2 == 0:
                        bright_white()

            for y in range(240, 320, 1):
                for x in range(width):
                    if x % 2 == 1:
                        bright_white()

            for y in range(320, 400, 1):
                for x in range(width):
                    if x % 2 == 0:
                        bright_white()

            for y in range(400, 480, 1):
                for x in range(width):
                    if x % 2 == 1:
                        bright_white()

            for y in range(480, 560, 1):
                for x in range(width):
                    if x % 2 == 0:
                        bright_white()

            for y in range(560, 640, 1):
                for x in range(width):
                    if x % 2 == 1:
                        bright_white()

            for y in range(640, 720, 1):
                for x in range(width):
                    if x % 2 == 0:
                        bright_white()

            for y in range(720, height, 1):
                for x in range(width):
                    if x % 2 == 1:
                        bright_white()

            img.save("chet_0.jpg", "JPEG")  # сохранить изображение
        elif i1%2==0 and i==1:
             # крупные полосы 16 штук
            for y in range(height):
                for x in range(width):
                    bright_black()

            for y in range(0, 50, 1):
                for x in range(width):
                    if x % 2 == 0:
                        bright_white()

            for y in range(50, 100, 1):
                for x in range(width):
                    if x % 2 == 1:
                        bright_white()

            for y in range(100, 150, 1):
                for x in range(width):
                    if x % 2 == 0:
                        bright_white()

            for y in range(150, 200, 1):
                for x in range(width):
                    if x % 2 == 1:
                        bright_white()

            for y in range(200, 250, 1):
                for x in range(width):
                    if x % 2 == 0:
                        bright_white()

            for y in range(250, 300, 1):
                for x in range(width):
                    if x % 2 == 1:
                        bright_white()

            for y in range(300, 350, 1):
                for x in range(width):
                    if x % 2 == 0:
                        bright_white()

            for y in range(350, 400, 1):
                for x in range(width):
                    if x % 2 == 1:
                        bright_white()

            for y in range(400, 450, 1):
                for x in range(width):
                    if x % 2 == 0:
                        bright_white()

            for y in range(450, 500, 1):
                for x in range(width):
                    if x % 2 == 1:
                        bright_white()

            for y in range(500, 550, 1):
                for x in range(width):
                    if x % 2 == 0:
                        bright_white()

            for y in range(550, 600, 1):
                for x in range(width):
                    if x % 2 == 1:
                        bright_white()

            for y in range(600, 650, 1):
                for x in range(width):
                    if x % 2 == 0:
                        bright_white()

            for y in range(650, 700, 1):
                for x in range(width):
                    if x % 2 == 1:
                        bright_white()

            for y in range(700, 750, 1):
                for x in range(width):
                    if x % 2 == 0:
                        bright_white()

            for y in range(750, height, 1):
                for x in range(width):
                    if x % 2 == 1:
                        bright_white()

            img.save("chet_1.jpg", "JPEG")  # сохранить изображение


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

        if i==0 and i%2==1:
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
