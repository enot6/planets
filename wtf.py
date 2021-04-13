import pygame
import math
import random
import time

background_colour = (255, 214, 187)
color_planets = [(181, 98, 65), (207, 155, 143), (199, 126, 97)]
screen = pygame.display.set_mode((1800, 1000))
pygame.display.set_caption('андрей лапух')  # всякий хлам
my_particles = []

turn_on_borders = True
collides = True
number_of_particles = 9
G = 6.67408 / 100000000   # 100000000

running = True

class Trail:

    def __init__(self, clr, pos1, pos2):
        self.color = clr
        self.pose1 = pos1
        self.pose2 = pos2

    def drawLine(self):
        pygame.draw.aaline(screen, self.color, self.pose1, self.pose2)

class Particle: # создает планету
    def __init__(self, x, y, size, mass):  # тут хранятся ее параметры
        self.destroyed = False
        self.speedX = 0
        self.speedY = 0
        self.x = x
        self.y = y
        self.poses = [(self.x, self.y)]
        self.size = size
        self.mass = mass
        self.colour = random.choice(color_planets)
        self.my_trail = []



    def display(self):  # отображение планеты

        pygame.draw.circle(screen, self.colour, (self.x, self.y), self.size)

        for t in self.my_trail:
            t.drawLine()

    def move(self):
        self.x += math.pi / 3 * self.speedX
        self.y += math.pi / 3 * self.speedY

        x = max(math.fabs(self.poses[-1][0]), math.fabs(self.x)) - min(math.fabs(self.poses[-1][0]), math.fabs(self.x))
        y = max(math.fabs(self.poses[-1][1]), math.fabs(self.y)) - min(math.fabs(self.poses[-1][1]), math.fabs(self.y))
        if x > 5 or y > 5:
            self.poses.append((self.x, self.y))

            trail = Trail(self.colour, (self.poses[-2][0], self.poses[-2][1]), (self.poses[-1][0], self.poses[-1][1]))
            self.my_trail.append(trail)
            if len(self.my_trail) >= 15:
                self.my_trail.pop(0)



randomMass = 10000000000
randomSize = randomMass * 0.0001 * random.randint(7, 9) / 200000
x = 900
y = 500
particle = Particle(x, y, randomSize, randomMass)
particle.speedX = 0
particle.speedY = 0
my_particles.append(particle)


def collide(p1, p2):
    dx = p1.x - p2.x
    dy = p1.y - p2.y

    distance = math.hypot(dx, dy)
    if distance <= p1.size + p2.size and collides == True: # врезались

        if p1.destroyed == False and p2.destroyed == False and p1.mass >= p2.mass:
            p1.mass += p2.mass * 0.9
            p1.size += p2.mass * 0.9 * random.randint(7, 9) / 50000
            p2.destroyed = True
        elif p1.destroyed == False and p2.destroyed == False and p2.mass >= p1.mass:
            p2.mass += p1.mass * 0.9
            p2.size += p1.mass * 0.9 * random.randint(7, 9) / 50000
            p1.destroyed = True



for n in range(number_of_particles):  # создание планет и запись их в массив
    randomMass = random.randint(2000, 8000)
    randomSize = randomMass * random.randint(7, 9) / 5000

    a = random.randint(1, 4)
    if a == 1:  # STANDART SPAWN
        x = random.randint(450, 700)
        y = random.randint(200, 300)
        particle = Particle(x, y, randomSize, randomMass)
        my_particles.append(particle)
        particle.speedY = -100 / 100  # -0.4
        particle.speedX = 1 / 100  # 0.83
    elif a == 2:
        x = random.randint(1100, 1350)
        y = random.randint(200, 300)
        particle = Particle(x, y, randomSize, randomMass)
        my_particles.append(particle)
        particle.speedY = 100 / 100  # -0.4
        particle.speedX = -1 / 100  # 0.83
    elif a == 3:
        x = random.randint(1100, 1350)
        y = random.randint(700, 800)
        particle = Particle(x, y, randomSize, randomMass)
        my_particles.append(particle)
        particle.speedY = 100 / 100  # -0.4
        particle.speedX = -1 / 100  # 0.83
    elif a == 4:
        x = random.randint(450, 700)
        y = random.randint(700, 800)
        particle = Particle(x, y, randomSize, randomMass)
        my_particles.append(particle)
        particle.speedY = -100 / 100  # -0.4
        particle.speedX = 1 / 100  # 0.83


def Test2():
    print('im working!')

while running:

    for i in range(len(my_particles)):

        for k in range(len(my_particles)):
            if i != k:
                x1 = my_particles[i].x
                x2 = my_particles[k].x
                y1 = my_particles[i].y
                y2 = my_particles[k].y
                m1 = my_particles[i].mass
                m2 = my_particles[k].mass
                speedX = my_particles[i].speedX
                speedY = my_particles[i].speedY
                dstrd1 = my_particles[i].destroyed
                dstrd2 = my_particles[k].destroyed

                if ((y1 > -10 and y1 < 1010) and (x1 > -10 and x1 < 1810) \
                        and dstrd1 == dstrd2 == False) or turn_on_borders == False:         #!!!!!!!!!!!!!!!!!!!!! не просчитывет движение объекта за пределами экрана
                    Fx = 0
                    Fy = 0

                    rx = x1 - x2
                    ry = y1 - y2

                    if 30 > rx >= 0:
                        rx = 30
                    elif rx > -30 and rx < 0:
                        rx = -30
                    if 30 > ry >= 0:
                        ry = 30
                    elif ry > -30 and ry < 0:
                        ry = -30

                    F = G * ((m1 * m2) / math.hypot(ry, rx) ** 2)

                    if y1 > y2:
                        my_particles[i].speedY -= F / m1
                    if y1 <= y2:
                        my_particles[i].speedY += F / m1

                    if x1 > x2:
                        my_particles[i].speedX -= F / m1
                    if x1 <= x2:
                        my_particles[i].speedX += F / m1



    pygame.display.flip()  # обновление экрана
    screen.fill(background_colour)

    for i, particle in enumerate(my_particles): # отображение планет и перемешение

        if ((particle.y > -10 and particle.y < 1010) and (particle.x > -10 and particle.x < 1810) \
                and particle.destroyed == False) or turn_on_borders == False:  #!!!!!!!!!!!!!!!!!!!!! не просчитывет движение объекта за пределами экрана
            particle.move()
            particle.display()
            for particle2 in my_particles[i + 1:]:
                collide(particle, particle2)

    for event in pygame.event.get():  # выход из программы
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            (mouseX, mouseY) = pygame.mouse.get_pos()
            randomMass = random.randint(2000, 8000)
            randomSize = randomMass * random.randint(7, 9) / 5000
            particle = Particle(mouseX, mouseY, randomSize, randomMass)
            my_particles.append(particle)
            if mouseY > 500:
                particle.speedY = -100 / 100  # -0.4
            else:
                particle.speedY = 100 / 100  # -0.4
            if mouseX > 900:
                particle.speedX = -1 / 100  # 0.83
            else:
                particle.speedX = 1 / 100  # 0.83