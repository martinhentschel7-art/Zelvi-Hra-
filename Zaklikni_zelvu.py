import turtle
import random

okno=turtle.Screen()
okno.title("Zaklikni zelvu")
okno.bgcolor("#c7f0bd")
okno.setup(width=800, height=600)

zelva=turtle.Turtle()
zelva.shape("turtle")
zelva.color("#2e8b57")
zelva.penup()
zelva.speed(0)

skore=0
cas_zbyva=30

zobrazovac= turtle.Turtle()
zobrazovac.hideturtle()
zobrazovac.penup()
zobrazovac.color("black")
zobrazovac.goto(0,260)
zobrazovac.write("Skóre: 0   Čas: 30", align="center", font=("Tahoma", 20, "bold"))

def aktualizuj_text():
    zobrazovac.clear()
    zobrazovac.write(f"Skóre: {skore}   Čas: {cas_zbyva}",
                     align="center", font=("Tahoma", 20, "bold"))

def klik(x,y):
    global skore
    if cas_zbyva > 0:
        skore+=1
        aktualizuj_text()
        pohni_zelvou()

def pohni_zelvou():
    x=random.randint(-350,350)
    y=random.randint(-250,250)
    zelva.goto(x,y)

def odpocet():
    global cas_zbyva
    if cas_zbyva > 0:
        cas_zbyva-=1
        aktualizuj_text()
        okno.ontimer(odpocet,1000)
    else:
        KONEC_HRY()

def KONEC_HRY():
    zelva.hideturtle()
    zobrazovac.goto(0,0)
    zobrazovac.color("black")
    zobrazovac.write(f"🎉 Konec hry!\nTvůj výsledek: {skore} bodů",
                     align="center", font=("Tahoma", 24, "bold"))

zelva.onclick(klik)
pohni_zelvou()
odpocet()
turtle.done()