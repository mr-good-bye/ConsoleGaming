from loguru import logger as rat
from gameLogic.env import Map, Player
import keyboard
from time import sleep
DEBUG = False
# TODO Menu implementation
# TODO Interaction with env
# TODO Map switching
# TODO Inventory
# TODO NPC and dialogues

if __name__ == "__main__":
    rat.add("logs/info.log", level="INFO", rotation="100 KB")
    if DEBUG:
        rat.add("logs/debug.log", level="DEBUG", rotation="100 KB")
    rat.remove(0)
    matrix = [
        list("###########################################"),
        list("#          .                              #"),
        list("#          .    .                         #"),
        list("#          .   .                          #"),
        list("#          .  .                           #"),
        list("#            .                            #"),
        list("#          ..                             #"),
        list("#          ..                             #"),
        list("#          ..                             #"),
        list("#          ..                             #"),
        list("#          ..                             #"),
        list("#          ..                             #"),
        list("#          ..                             #"),
        list("#          ..                             #"),
        list("###########################################")
    ]
    matrix_tad = [
        list("%%%"),
        list("%%%"),
        list("%%%")
    ]
    m = Map(bitmap=matrix)
    #m.overlap((2, 2), matrix_tad)
    #m.show()
    p = Player(m)
    while 'you suck':
        try:
            if keyboard.is_pressed('a'):
                p.move('left')
            if keyboard.is_pressed('d'):
                p.move('right')
            if keyboard.is_pressed('w'):
                p.move('up')
            if keyboard.is_pressed('s'):
                p.move('down')
            if keyboard.is_pressed('q'):
                break
        except Exception as e:
            rat.debug(e)
        m.show()
