from turtle import *
color('purple', 'black')
begin_fill()
while True:
    speed(10)
    forward(200)
    left(170)   
    right(15)
    back(3)
    forward(100)
    if abs(pos()) < 1:
        break
end_fill()
done()

left(300)

color('pink', 'black')
begin_fill()
while True:
    speed(10)
    forward(200)
    left(170)   
    right(15)
    back(3)
    forward(100)
    if abs(pos()) < 1:
        break
end_fill()
done()


