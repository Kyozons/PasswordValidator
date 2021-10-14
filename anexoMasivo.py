import pyautogui as pg
import time


def auto_anexo(phone):
    time.sleep(1)
    # print(pg.position())
    pg.click(2312, 101)
    pg.moveTo(2328, 178, duration = 0.3)
    pg.click(pg.position())
    pg.typewrite(phone)
    pg.typewrite(["tab"])
    pg.typewrite(phone)
    pg.typewrite(["tab"])
    pg.typewrite(phone)
    pg.typewrite(["tab"])
    pg.typewrite(phone)
    pg.typewrite(["tab"])
    pg.typewrite(["tab"])
    pg.typewrite(phone)
    pg.typewrite(["tab"])
    pg.typewrite(["tab"])
    pg.typewrite(["tab"])
    pg.typewrite(["tab"])
    pg.typewrite(["down"])
    pg.typewrite(["tab"])
    pg.typewrite(["space"])
    time.sleep(1)
    pg.moveTo(2296, 138, duration = 0.3)
    pg.click(pg.position())
    pg.moveTo(2185, 336, duration = 0.3)
    pg.click(pg.position())
    pg.typewrite(phone)
    pg.scroll(-200)
    pg.moveTo(2401, 812)
    pg.click(pg.position())
    pg.click(pg.position())



cant = int(input('Cuantos anexos?: '))
phone = int(input('Anexo inicial: '))

for i in range(cant):
        auto_anexo(str(phone))
        phone += 1

