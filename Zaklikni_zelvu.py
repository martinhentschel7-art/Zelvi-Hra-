import turtle
import random

# Nastavení okna
okno = turtle.Screen()
okno.title("🐢 Zaklikni želvu!")
okno.bgcolor("#c7f0bd")
okno.setup(width=800, height=600)

# Želva (cíl)
zelva = turtle.Turtle()
zelva.shape("turtle")
zelva.color("#2e8b57")
zelva.turtlesize(2)
zelva.penup()
zelva.speed(0)

# Text skóre
skore = 0
cas_zbyva = 30
hra_bezi = False   # dokud není odpočet, hra neběží

zobrazovac = turtle.Turtle()
zobrazovac.hideturtle()
zobrazovac.penup()
zobrazovac.color("black")
zobrazovac.goto(0, 260)
zobrazovac.write("Skóre: 0   Čas: 30", align="center", font=("Tahoma", 20, "bold"))

# Aktualizace skóre a času
def aktualizuj_text():
    zobrazovac.clear()
    zobrazovac.goto(0, 260)
    zobrazovac.write(f"Skóre: {skore}   Čas: {cas_zbyva}",
                     align="center", font=("Tahoma", 20, "bold"))

# Kliknutí na želvu
def klik(x, y):
    global skore
    if hra_bezi and cas_zbyva > 0:
        skore += 1
        aktualizuj_text()
        pohni_zelvou()

# Pohyb želvy na náhodné místo
def pohni_zelvou():
    x = random.randint(-350, 350)
    y = random.randint(-250, 250)
    zelva.goto(x, y)

# Časový odpočet během hry
def odpocet():
    global cas_zbyva, hra_bezi
    if cas_zbyva > 0:
        cas_zbyva -= 1
        aktualizuj_text()
        okno.ontimer(odpocet, 1000)
    else:
        hra_bezi = False
        konec_hry()

# Konec hry
def konec_hry():
    zelva.hideturtle()
    zobrazovac.goto(0, 0)
    zobrazovac.color("#2e2e2e")
    zobrazovac.write(f"🎉 Konec hry!\nTvůj výsledek: {skore} bodů",
                     align="center", font=("Tahoma", 24, "bold"))

# -------------------------------
# ODPOČÍTÁVÁNÍ 3 - 2 - 1 - TEĎ
# -------------------------------
odpoctovy_text = turtle.Turtle()
odpoctovy_text.hideturtle()
odpoctovy_text.penup()
odpoctovy_text.color("black")

def start_odpocet(cislo=3):
    odpoctovy_text.clear()
    odpoctovy_text.goto(0, 20)

    if cislo > 0:
        odpoctovy_text.write(str(cislo), align="center", font=("Tahoma", 48, "bold"))
        okno.ontimer(lambda: start_odpocet(cislo - 1), 1000)
    else:
        odpoctovy_text.write("Teď!", align="center", font=("Tahoma", 48, "bold"))
        okno.ontimer(zacni_hru, 700)

def zacni_hru():
    global hra_bezi
    odpoctovy_text.clear()
    hra_bezi = True
    pohni_zelvou()
    odpocet()

# Spuštění hry
zelva.onclick(klik)
start_odpocet()   # místo okamžitého startu hry

turtle.done()