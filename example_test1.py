from pydojo import *

# create game display
screen(1280, 720)

dyno = Actor('example_library/dinosaur1.png')
dyno.scale(0.2)
dyno.goto(500, 300)
dyno.rotation = 'flip'

star = Actor('example_library/seastar1.png', 'felice')
star.load('example_library/seastar2.png', 'triste')
star.scale(200, 200)
star.goto(600, 500)

testo = Text('ciao', color=GREEN, italic=True)
print((testo.costumes))
testo.setfontsize(48)
testo.setbold(True)
testo.goto(100, 100)

# dyno.rotate = False

hey = Sound('example_library/hey.wav')

print((actorsInfo.actorsList))

while True:

    # print(actorsInfo.drawList)

    if dyno.click():
        print('funziona')
        hey.play()
        print((dyno.getcostume()))

    if keydown(RIGHT):
        print('destra')
        star.point(90)
        star.forward(5)

    if keydown(LEFT):
        print('sinistra')
        star.point(-90)
        star.forward(5)

    # dyno.direction = 90
    # dyno.left(1)
    testo.right(1)
    # dyno.point(MOUSE)
    # dyno.forward(3)
    if keydown(G):
        dyno.pendown()
        dyno.gorand()
        dyno.glide(testo)

    if keydown(W):
        print((dyno.x, dyno.y))

    star.left(1)
    # print(dyno.direction)

    if dyno.collide(star):
        # print(dyno.collide(star))
        star.setcostume(1)
        print('dyno ha toccato star')
        # hey.play()
        # dyno.hide(2)

    if dyno.collide(testo):
        testo.write('toccato')

    if keydown(F):
        star.setcostume('felice')

    if keydown(D):
        dyno.show()

    fill(PINK)

    # update screen and events queue
    update()
