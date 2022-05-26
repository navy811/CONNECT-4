import turtle

t=turtle.Turtle()

ostatni_ruch = 0
ostatnia_kolumna = 0
kolumny = 7
wiersze = 6

screen = turtle.Screen()
screen.setup(1000,700)

screen.bgcolor('lightblue')
t.penup()
t.setpos(-430,200)
wsp = []
wsp1 = [-430,200]

t.setpos(-130,-330)
t.write('aby wyjsc, naciśnij  klawisz 0',font=('Arial',15))

t.color('blue')
t.setpos(-400,-350)
t.write('CONNECT',font=('Arial',30,'bold'))

t.setpos(250,-350)
t.write('GAME',font=('Arial',30,'bold'))

t.color('white')
wsp_wiersze = dict.fromkeys([1,2,3,4,5,6,7],[])
licznik_wiersze = dict.fromkeys([1,2,3,4,5,6,7],0)

x = -310
t.speed(0)
t.setpos(-470,300)
t.color('blue')

for i in range(6):
    for kolory in('white','yellow','green','magenta'):
        t.color(kolory)
        t.pendown()
        t.circle(60)
        t.right(90)
        t.penup()
        t.forward(30)
        t.left(90)
        t.circle(60)
t.setpos(470,300)
for i in range(6):
    for kolory in('white','yellow','green','magenta'):
        t.color(kolory)
        t.pendown()
        t.circle(60)
        t.right(90)
        t.penup()
        t.forward(30)
        t.left(90)
        t.circle(60)

t.setpos(-470,300)
for i in range(10):
    for kolory in('white','yellow','green','magenta'):
        t.color(kolory)
        t.pendown()
        t.circle(60)
        t.forward(30)
        t.penup()






for j in range(1,8):
    t.color('white')
    t.pencolor('white')
    y = 200
    t.setpos(x,y)
    lista = []
    for i in range(7):
        t.begin_fill()
        t.pendown()
        t.circle(50)
        t.penup()
        wsp1 = [x,y]
        t.setpos(wsp1)
        t.end_fill()
        lista.append(wsp1)
        y -= 100
    wsp_wiersze[j] = lista


    x += 100
def jeden():
    licznik_wiersze[1]+=1
    kolorowanie(1)

def dwa():
    licznik_wiersze[2] += 1
    kolorowanie(2)

def trzy():
    licznik_wiersze[3] += 1
    kolorowanie(3)

def cztery():
    licznik_wiersze[4] += 1
    kolorowanie(4)

def piec():
    licznik_wiersze[5] += 1
    kolorowanie(5)
def szesc():
    licznik_wiersze[6] += 1
    kolorowanie(6)

def siedem():
    licznik_wiersze[7] += 1
    kolorowanie(7)

def wyjscie():
    exit()

def cofniecie():
    kolorowanie(ostatnia_kolumna,True)
    licznik_wiersze[ostatnia_kolumna] -= 1

def wartosci(x):
    licznik = 0
    for i in x.items():
        licznik += i[1]
    return licznik


def kolorowanie(x,czy_c=False):
    global ostatni_ruch,ostatnia_kolumna
    if czy_c:
        kolor_pisaka = 'white'
        ws= ostatni_ruch
        t.setpos(ws)
        t.color(kolor_pisaka)
        t.begin_fill()
        t.pendown()
        t.circle(50)
        t.penup()
        t.end_fill()
        return
    elif wartosci(licznik_wiersze) % 2 == 0:
        kolor_pisaka = 'red'
    else:
        kolor_pisaka = 'black'
    t.begin_fill()
    a = licznik_wiersze[x]
    print(0-a-1)
    print(wsp_wiersze)
    ws = wsp_wiersze[x][-a-1]
    t.setpos(ws)
    ostatni_ruch = ws
    ostatnia_kolumna = x
    t.color(kolor_pisaka)
    t.begin_fill()
    t.pendown()
    t.circle(50)
    t.penup()
    t.end_fill()
#TODO dodać ograniczenie przed wyjściem poza skale

turtle.listen()

turtle.onkey(jeden,'1')
turtle.onkey(dwa,'2')
turtle.onkey(trzy,'3')
turtle.onkey(cztery,'4')
turtle.onkey(piec,'5')
turtle.onkey(szesc,'6')
turtle.onkey(siedem,'7')
turtle.onkey(wyjscie,'0')
turtle.onkey(cofniecie,'c')
turtle.mainloop()