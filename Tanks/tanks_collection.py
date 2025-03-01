from tkinter import NW
from random import randint
from units import Tank
import world
from missile_collection import check_missiles_collision

_tanks = []
_canvas = None

id_screen_text = 0

def initialze(canv):
    global _canvas, id_screen_text
    _canvas = canv

    player = spawn(False)
    enemy = spawn(True).set_target(player)
    enemy = spawn(True).set_target(player)
    enemy = spawn(True).set_target(player)
    enemy = spawn(True).set_target(player)
    spawn(True).set_target(player)

    id_screen_text = _canvas.create_text(10, 10, text = _get_screen_text(), font = ('TkDefaultFont', 20), fill = _get_color(), anchor = NW)

    print(_tanks)

def _update_color():
    _canvas.itemconfig(id_screen_text, fill = _get_color())

def _get_color():
    if get_player().is_destroyed():
        return 'red'
    if len(_tanks) == 1:
        return 'yellow'
    return 'white'.format(len(_tanks) - 1)

def _update_screen_text():
    _canvas.itemconfig(id_screen_text, text = _get_screen_text())

def _get_screen_text():
    if get_player().is_destroyed():
        return '!GAME OVER!'
    if len(_tanks) == 1:
        return '!WIN!'
    return 'Осталось {}'.format(len(_tanks) - 1)

def get_player():
    return _tanks[0]

def update():
    _update_screen_text()
    start = len(_tanks) - 1
    for i in range(start, -1, -1):
        if _tanks[i].is_destroyed() and i != 0:
            del _tanks[i]
        else:
            _tanks[i].update()
            check_collishion(_tanks[i])
            check_missiles_collision(_tanks[i])

def check_collishion(tank):
    for other_tank in _tanks:
        if tank == other_tank:
            continue
        if tank.intersect(other_tank):
            return True
    return False

def spawn(is_bot=True):
    cols = world.get_cols()
    rows = world.get_rows()

    while True:
        col = randint(1, cols - 1)
        row = randint(1, rows - 1)
        if world.get_block(row, col) != world.GROUND:
            continue

        t = Tank(_canvas, row, col, bot = is_bot)
        if not check_collishion(t):
            _tanks.append(t)
            return t