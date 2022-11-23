#Author:Chipo Chibbamulilo
#date:10/9/2022
#Purpose: Lab 1 

from cs1lib import*
W=20
H=80
x1=0
y1=0
x2=380
y2=320
circle_x=200
circle_y=200
v_x=5
v_y=5
R=10
amount_change=10
WIDTH=400
HEIGHT=400
spacebar=" "
apressed=False
zpressed=False
kpressed=False
mpressed=False
game_start=False
qpressed=False
spacepressed=False

#assigning keys
def my_kpress(value):
    global x1,y1,x2,y2, apressed,zpressed,kpressed,mpressed,game_start,qpressed,spacepressed

    if value=="a":
        apressed=True

    if value=="z":
        zpressed=True

    if value=="k":
        kpressed=True

    if value=="m":
        mpressed=True

    if value=="a"or"z"or"k"or"m":#so that any key pressed can start the game
        game_start=True

    if value=="q":
        qpressed=True

    if value==spacebar:
        spacepressed=True

def my_krelease(value):
    global apressed,zpressed,kpressed,mpressed,spacepressed
    if value=="a":
        apressed=False

    if value=="z":
        zpressed=False

    if value=="k":
        kpressed=False

    if value=="m":
        mpressed=False

    if value==spacebar:
        spacepressed=False

def ball():
    global game_start,circle_x,circle_y,v_x,v_y
    set_stroke_color(0,0,0)
    set_fill_color(0,0,0)
    draw_circle(circle_x, circle_y, R)

    if game_start==True:
        circle_x= circle_x + v_x
        circle_y= circle_y + v_y

    if spacepressed==True:
        circle_x=200
        circle_y=200
        circle_x = circle_x + v_x
        circle_y = circle_y + v_y

def has_collided_vertical():
    global circle_x,R
    if circle_x>400-R or circle_x<R:
        return False

def has_collided_horizontal():
    global circle_y
    if circle_y > 400-R:
        return False
    if circle_y < R:
        return False

def has_collided_paddle_R():
    global circle_x
    if circle_x > 400-W-R and y2 < circle_y < y2+H:
        return False

def has_collided_paddle_L():
    global circle_y
    if circle_x < W + R and y1 < circle_y < y1+H:
        return False


def atari_pong():
    global x1,y1,x2,y2,apressed,zpressed,kpressed,mpressed,spacepressed,v_x,v_y,circle_x,game_start
    set_clear_color(1,0,1)#set background to purple
    clear()

#Creating Paddles
    set_stroke_color(0,0,0)#setting stroke color to black
    set_fill_color(1,0,0)#filling rectangles with red
    draw_rectangle(x1, y1, W, H)
    draw_rectangle(x2, y2, W, H)

    ball()

    if has_collided_horizontal()==False:
        v_y = -v_y

    if has_collided_paddle_R()==False:
        circle_x= circle_x - 10
        v_x = -v_x

    if has_collided_paddle_L()==False:
        circle_x= circle_x + 10
        v_x = -v_x

    if  has_collided_vertical() ==False:
        spacepressed=True#ensure that game be restarted by pressing space after losing
        game_start=True

    if apressed==True:
        if y1>=0:
            y1 = y1 - amount_change

    if zpressed==True:
        if y1<=400-H:
            y1 = y1 + amount_change

    if kpressed==True:
        if y2>=0:
            y2 = y2 - amount_change

    if mpressed==True:
        if y2<=400-H:
            y2 = y2 + amount_change

    if spacepressed==True:
        y1 = 0
        y2 = 400-H

    if qpressed == True:
        quit()


start_graphics(atari_pong,key_press=my_kpress,key_release=my_krelease,width=WIDTH,height=HEIGHT)
