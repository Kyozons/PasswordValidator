import pyautogui as pg
import time

def otro_anexo():
    print('Crear otro anexo? (s/n)')
    return input().lower().startswith('s')

def auto_anexo(phone):
    time.sleep(10)
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

while True:
    if otro_anexo():
        phone=''
        phone=input('Numero de anexo a crear: ')
        if phone.startswith('0') or len(phone) != 4:
            print('Anexo no valido. Saliendo...')
            break
        else:
            auto_anexo(phone)
    else:
        break

