import os
import platform
import copy

print(platform.system())
if platform.system() == "Linux":
    if platform.architecture()[0] == "64bit":
        os.environ["RAYLIB_BIN_PATH"] = "Deps/Linux64"
    elif platform.architecture()[0] == "32bit":
        os.environ["RAYLIB_BIN_PATH"] = "Deps/Linux32"

from raylibpy import *

def main():

    # Initialization
    # ---------------------------------------------------------------
    # Raylib stuff
    screen_width = 1024 #512 256 128 64
    screen_height = 560 #280 140 70 35

    init_window(screen_width, screen_height, "Shortline Railroad - Remastered")

    spacing = 0

    camera = Camera2D()

    camera.offset = Vector2(0, 0)
    camera.target = Vector2(20, 20)
    camera.rotation = 0.0
    camera.zoom = 1.0

    set_target_fps(60)
    # ---------------------------------------------------------------
    # Game counters & Flags:
    # ---------------------------------------------------------------
    # Debug mode: Enable dev tools/cheats (maybe give this as a reward for beating year 2000?)
    debug = False

    # What year the player is at
    current_year = 1800

    # Cash is internally counted as 1's, but displayed as 1000's
    # Defaults to 100
    current_cash = 100

    # How many trains the player has successfully gotten to a station
    trains_stationed = 0

    # What "level" the player is on
    # Defaults to 15
    level = 15

    # List of entrances open to the player
    # Will be filled with a dictionary of entrances, the key being color and content being the state of the entrance
    entrances = []

    # Grid information
    column = [170, 340, 500, 670, 830]
    row = [100, 140, 180, 220, 260, 300, 340, 380, 420, 460]
    # List of the game tiles, it's ok to generate a static number of these as there should never be more than 25
    t1 = Tile(1, Vector2(column[1], row[0]))
    t2 = Tile(2, Vector2(column[3], row[0]))
    t3 = Tile(3, Vector2(column[0], row[1]))
    t4 = Tile(4, Vector2(column[2], row[1]))
    t5 = Tile(5, Vector2(column[4], row[1]))
    t6 = Tile(6, Vector2(column[1], row[2]))
    t7 = Tile(7, Vector2(column[3], row[2]))
    t8 = Tile(8, Vector2(column[0], row[3]))
    t9 = Tile(9, Vector2(column[2], row[3]))
    t10 = Tile(10, Vector2(column[4], row[3]))
    t11 = Tile(11, Vector2(column[1], row[4]))
    t12 = Tile(12, Vector2(column[3], row[4]))
    t13 = Tile(13, Vector2(column[0], row[5]))
    t14 = Tile(14, Vector2(column[2], row[5]))
    t15 = Tile(15, Vector2(column[4], row[5]))
    t16 = Tile(16, Vector2(column[1], row[6]))
    t17 = Tile(17, Vector2(column[3], row[6]))
    t18 = Tile(18, Vector2(column[0], row[7]))
    t19 = Tile(19, Vector2(column[2], row[7]))
    t20 = Tile(20, Vector2(column[4], row[7]))
    t21 = Tile(21, Vector2(column[1], row[8]))
    t22 = Tile(22, Vector2(column[3], row[8]))
    t23 = Tile(23, Vector2(column[0], row[9]))
    t24 = Tile(24, Vector2(column[2], row[9]))
    t25 = Tile(25, Vector2(column[4], row[9]))

    tiles = [t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25]

    # ---------------------------------------------------------------
    # Main game loop
    while not window_should_close():

        # Update
        # -----------------------------------------------------------
        mouse_pos = get_mouse_position()
        # -----------------------------------------------------------

        # Draw
        # -----------------------------------------------------------
        begin_drawing()

        clear_background(Color(85, 170, 0, 255))

        begin_mode2d(camera)

        end_mode2d()

        draw_rectangle(0, 0, 1024, 79, BLUE) # Menu
        draw_rectangle(0, 560-25, 1024, 25, LIGHTGRAY) # Status

        # Interactable Tiles
        for tile in tiles:
            tile.draw()

        if(is_mouse_button_pressed(MOUSE_LEFT_BUTTON)):
            print("X: {0}\nY: {1}".format(mouse_pos.x, mouse_pos.y)) # Mouse POS

        end_drawing()
        # -----------------------------------------------------------

    # De-Initialization
    # ---------------------------------------------------------------
    close_window()       # Close window and OpenGL context
    # ---------------------------------------------------------------

# Class for a track on the grid
class Tile():
    def __init__(self, id, location = Vector2(0,0), type = 0b00000000):
        # Tile ID
        self.id = id

        # Vectors for drawing the Tile
        self.v1 = location
        self.v2 = location
        self.v3 = location
        self.v4 = location

        # Function that creates the Vectors
        self.tile_vector_generator(location)

        print(self.v1)
        print(self.v2)
        print(self.v3)
        print(self.v4)

        # Track type data is an 8-bit value
        #   0000 0000 = Nothing
        #   0000 0001 = Obstical
        #   1000 0001 = Track Sloped Downwards
        #   1000 0010 = Track Curved Downwards
        #   1000 0100 = Track Curved to the Left
        #   1000 1000 = Track Sloped Upwards
        #   1001 0000 = Track Curved Upwards
        #   1010 0000 = Track Curved to the Right
        # Combine these values to get a combination of tracks
        self.type = type

        # List of hazards this tile's track has
        self.hazards = []

    # Function that handles the spawning of hazards on the track
    def hazard_controller(self, hazard_progress, id):
        # Hazard Progress determines where on the track a hazard is located (same as a train)
        # Should be a float for a percentage
        hazard_progress = hazard_progress

        # Create a dictionary to make each hazard unique
        hazard = {id: hazard_progress}

        # Append the hazard to the list of hazards
        self.hazards.append(hazard)
        return

    def tile_vector_generator(self, location):
        # Use v1 as the reference point and generate the other vectors based on that
        tile_v1 = copy.deepcopy(location)
        print(tile_v1)

        tile_v2 = copy.deepcopy(location)
        tile_v2.x -= 105
        tile_v2.y += 30
        print(tile_v2)

        tile_v3 = copy.deepcopy(location)
        tile_v3.x += 115
        tile_v3.y += 30
        print(tile_v3)

        tile_v4 = copy.deepcopy(location)
        tile_v4.y += 55
        print(tile_v4)

        self.v1 = tile_v1
        self.v2 = tile_v2
        self.v3 = tile_v3
        self.v4 = tile_v4

    def draw(self, color = BLACK):
        #print("Hello")
        #print(self.v1)
        #print(self.v2)
        #print(self.v3)
        #print(self.v4)
        draw_triangle(self.v1, self.v2, self.v3, color)
        draw_triangle(self.v2, self.v4, self.v3, color)

# Class for a Train
class Train():
    def __init__(self, color, direction, type, tile = 0, components = None, speed = 0):

        # What color the train is
        self.color = color

        # What tile the train is currently on
        self.tile = tile

        # What kind of train is this train
        self.type = type

        # What cars are attached to the train (should be a list or None)
        self.components = components

        # How far along the train is along the current track (0% is start, 100% is end)
        self.progress = 0.0

        # What direaction the train is facing (0 or 1)
        self.direction = direction

        # How fast the train is moving (negative speed makes a train go backwards)
        self.speed = speed


if __name__ == '__main__':
    main()
