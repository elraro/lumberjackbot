from threading import Thread

from pymouse import PyMouse
import time
import quickgrab as qg

clicks = list()
click = dict()
click["x"] = 660 + 381
click["y"] = 180 + 762
clicks.append(click)
clicks.append(click)

print("Bot started...")
time.sleep(3)

m = PyMouse()

# m.click(660+302,180+759)
time.sleep(0.1)
print("Lets go!")


def get_clicks(self, arr):
    while True:
        try:
            clickt = clicks.pop()
            print(clickt)
            m.click(clickt["x"], clickt["y"])
            time.sleep(0.5)
            clickt = clicks.pop()
            print(clickt)
            m.click(clickt["x"], clickt["y"])
            time.sleep(0.5)
        except IndexError:
            continue

thread1 = Thread(target=get_clicks, args=clicks)
thread1.start()

while True:
    time.sleep(0.25)
    if qg.get_arbol_der() == 4378 and qg.get_arbol_izq() == 14754:
        # el arbol está a la izquierda
        click = dict()
        click["x"] = 660 + 381
        click["y"] = 180 + 762
        # print(click)
        clicks.append(click)
        clicks.append(click)
        print("izq")
    if qg.get_arbol_der() == 16631 and qg.get_arbol_izq() == 2753:
        # el arbol está a la derecha
        click = dict()
        click["x"] = 660 + 215
        click["y"] = 180 + 762
        clicks.append(click)
        clicks.append(click)
        print("der")