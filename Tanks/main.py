import missile_collection
from tkinter import*
import world
import tanks_collection
import texture

KEY_UP = 38
KEY_DOWN = 40
KEY_LEFT = 37
KEY_RIGHT = 39

KEY_W = 87
KEY_S = 83
KEY_A = 65
KEY_D = 68

FPS = 60

def update():
    tanks_collection.update()
    missile_collection.update()
    player = tanks_collection.get_player()
    world.set_camera_xy(player.get_x() - world.SCREEN_WIDTH // 2 + player.get_size() // 2, player.get_y() - world.SCREEN_HEIGHT // 2 + player.get_size() // 2)
    world.update_map()
    w.after(1000//FPS, update)

def key_press(event):
    player = tanks_collection.get_player()

    if player.is_destroyed():
        return

    if event.keycode == KEY_W:
        player.forvard()
    elif event.keycode == KEY_S:
        player.backward()
    elif event.keycode == KEY_A:
        player.left()
    elif event.keycode == KEY_D:
        player.right()
    elif event.keycode == KEY_UP:
        world.move_camera(delta_x = 0, delta_y = -5)
    elif event.keycode == KEY_DOWN:
        world.move_camera(delta_x = 0, delta_y = 5)
    elif event.keycode == KEY_RIGHT:
        world.move_camera(delta_x = 5, delta_y = 0)
    elif event.keycode == KEY_LEFT:
        world.move_camera(delta_x = -5, delta_y = 0)

    elif event.keycode == 32:
        player.fire()

def load_textures():
    texture.load('tank_up', '../img/tank_up.png')
    texture.load('tank_down', '../img/tank_down.png')
    texture.load('tank_left', '../img/tank_left.png')
    texture.load('tank_right', '../img/tank_right.png')

    texture.load('tank_up_player', '../img/tank_up_player.png')
    texture.load('tank_down_player', '../img/tank_down_player.png')
    texture.load('tank_left_player', '../img/tank_left_player.png')
    texture.load('tank_right_player', '../img/tank_right_player.png')

    texture.load(world.BRICK, '../img/brick.png')
    texture.load(world.WATER, '../img/water.png')
    texture.load(world.CONCRETE, '../img/wall.png')
    texture.load(world.MESSLE, '../img/Bonus_Ammo.png')
    texture.load(world.PETROL, '../img/Bonus_Petrol.png')

    texture.load('missile_up', '../img/missile_up.png')
    texture.load('missile_down', '../img/missile_down.png')
    texture.load('missile_left', '../img/missile_left.png')
    texture.load('missile_right', '../img/missile_right.png')

    texture.load('0_hp', '../img/0.png')
    texture.load('20_hp', '../img/20.png')
    texture.load('40_hp', '../img/40.png')
    texture.load('60_hp', '../img/60.png')
    texture.load('80_hp', '../img/80.png')
    texture.load('100_hp', '../img/100.png')

    texture.load('destroy', '../img/tank_destroy.png')
    print(texture._frames)

w = Tk()
load_textures()
w.title('Танки на минималках 2.0')
canv = Canvas(w, width = world.SCREEN_WIDTH, height = world.SCREEN_HEIGHT, bg="ForestGreen")
canv.pack()

world.initialize(canv)
tanks_collection.initialze(canv)
missile_collection.initialize(canv)

w.bind('<KeyPress>', key_press)

update()
w.mainloop()