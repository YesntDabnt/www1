from turtle import *
color('purple', 'black')
begin_fill()
while True:
    forward(200)
    left(170)
    right(15)
    if abs(pos()) < 1:
        break
end_fill()
done()
